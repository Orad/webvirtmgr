from datetime import datetime
from decimal import Decimal

from django_cron import CronJobBase, Schedule

from servers.models import Compute
from instance.models import Instance, RunningInstanceTime, RunningHistory
from organizations.models import UserOrganization


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 minute
    RETRY_AFTER_FAILURE_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'dashboard.cron.my_cron_job'
    
    def do(self):
        now = datetime.utcnow()
        organizations = UserOrganization.objects.all()
        for organization in organizations:
            computes = Compute.objects.filter(organization = organization)
            for compute in computes :
                instances = Instance.objects.filter(compute = compute)
                for instance in instances:
                    paused = True 
                    today_paused = True 
                    end_time = 0
                    start_time = 0
                    today_end_time = 0
                    today_start_time = 0
                    total_time = Decimal(0.0000)
                    today_time = Decimal(0.0000)
                    is_first_record = True

                    running_histories = RunningHistory.objects.filter(instance = instance, created_at__month = now.date().month, created_at__year = now.date().year)
                    if running_histories:
                        for running_history in running_histories:
                            if running_history.event == 'VIR_DOMAIN_RUNNING' and paused == True:
                                start_time = running_history.created_at
                                paused = False
                            if running_history.event == 'VIR_DOMAIN_PAUSED' and paused == False:
                                end_time = running_history.created_at
                                paused = True
                            if start_time !=0 and end_time != 0 :
                                total_time = total_time + Decimal((end_time - start_time).total_seconds() / 60)
                                start_time = 0 
                                end_time = 0  

                            if now.date() == running_history.created_at.date():
                                if running_history.event == 'VIR_DOMAIN_RUNNING' and today_paused == True:
                                    today_start_time = running_history.created_at
                                    today_paused = False
                                if running_history.event == 'VIR_DOMAIN_PAUSED' and today_paused == False:
                                    today_end_time = running_history.created_at
                                    today_paused = True
                                if running_history.event == 'VIR_DOMAIN_PAUSED' and is_first_record == True:
                                    today_time += Decimal((running_history.created_at.replace(tzinfo=None) -  now.replace(minute=0, hour=0, second=0, microsecond=0)).total_seconds() / 60)
                                    is_first_record = False

                                if today_start_time !=0 and today_end_time != 0 :
                                    today_time += Decimal((today_end_time - today_start_time).total_seconds() / 60)
                                    today_start_time = 0 
                                    today_end_time = 0 
                                is_first_record = False

                        first_running_history = running_histories[0]
                        last_running_history = running_histories[len(running_histories)-1]
                        if first_running_history.event == 'VIR_DOMAIN_PAUSED':
                            total_time += Decimal((first_running_history.created_at.replace(tzinfo=None) - now.replace(day=1,minute=0, hour=0, second=0, microsecond=0)).total_seconds() / 60.0)

                        if last_running_history.event == 'VIR_DOMAIN_RUNNING':
                            total_time += Decimal(( now.replace(tzinfo=None) - last_running_history.created_at.replace(tzinfo=None)).total_seconds() / 60)
                            if now.date() == last_running_history.created_at.date():
                                today_time += Decimal((now - last_running_history.created_at.replace(tzinfo=None)).total_seconds() / 60)
                    else:
                        running_histories = RunningHistory.objects.filter(instance = instance)
                        if running_histories:
                            last_running_history = running_histories[len(running_histories)-1]
                            if last_running_history.event == 'VIR_DOMAIN_RUNNING':
                                total_time += Decimal(( now - now.replace(day=1,minute=0, hour=0, second=0, microsecond=0)).total_seconds() / 60)
                                today_time += Decimal((now - now.replace(minute=0, hour=0, second=0, microsecond=0)).total_seconds() / 60)

                    try:
                        running_instance = RunningInstanceTime.objects.get(instance = instance, date = now.date().replace(day=1))
                    except ObjectDoesNotExist:
                        running_instance = RunningInstanceTime(instance = instance, date = now.date().replace(day=1))

                    running_instance.total_time = total_time
                    running_instance.daily_time = today_time
                    running_instance.save()