from datetime import datetime
from decimal import Decimal

from django.shortcuts import render
from django.views.generic import View

from servers.models import Compute
from instance.models import Instance, RunningInstanceTime
from organizations.models import UserOrganization


class DashboardView(View):
    
    def get(self, request):
    	user = request.user
    	response = []
        total_instances = 0
        total_monthly_time = Decimal(0.0000)
        total_daily_time = Decimal(0.0000)
    	user_organization = UserOrganization.objects.get(user=user)
        organization = user_organization.organization
        print organization
        computes = Compute.objects.filter(organization = organization)
        for compute in computes :
            print compute.id
            instances = Instance.objects.filter(compute = compute)
            for instance in instances:
                running_time = RunningInstanceTime.objects.get(instance=instance,date=datetime.now().date().replace(day=1))
                data = {"instance":instance,"daily_time":running_time.daily_time,"total_time":running_time.total_time}
                response.append(data)
                total_monthly_time += running_time.total_time
                total_daily_time += running_time.daily_time
                total_instances += 1
        print response
        return render(request, 'dashboard/dashboard.html',{"data":response,"total_monthly_time":total_monthly_time,"total_daily_time":total_daily_time,"total_instances":total_instances})

dashboard_view = DashboardView.as_view()


