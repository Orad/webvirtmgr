from decimal import Decimal
from datetime import datetime

from django.shortcuts import render
from django.views.generic import View
from django.core.exceptions import ObjectDoesNotExist

from servers.models import Compute
from organizations.models import UserOrganization
from instance.models import Instance, RunningInstanceTime


class DashboardView(View):
    
    def get(self, request):
    	user = request.user
    	response = []
        total_instances = 0
        total_monthly_time = Decimal(0.0000)
        total_daily_time = Decimal(0.0000)
    	user_organization = UserOrganization.objects.get(user=user)
        organization = user_organization.organization
        computes = Compute.objects.filter(organization = organization)
        for compute in computes :
            instances = Instance.objects.filter(compute = compute)
            for instance in instances:
                try:
                    running_time = RunningInstanceTime.objects.get(instance=instance,date=datetime.now().date().replace(day=1))
                    data = {"instance":instance,"daily_time":running_time.daily_time,"total_time":running_time.total_time}
                    response.append(data)
                    total_monthly_time += running_time.total_time
                    total_daily_time += running_time.daily_time
                except ObjectDoesNotExist:
                    pass
            total_instances += len(instances)
        return render(request, 'dashboard/dashboard.html',{"data":response,"total_monthly_time":total_monthly_time,"total_daily_time":total_daily_time,"total_instances":total_instances})

dashboard_view = DashboardView.as_view()


