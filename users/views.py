from django.views.generic import View
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from users.models import UserInfo
from users.forms import UserInfoForm


class UserInfoView(View):
    
    def get(self, request):
        user = request.user
        try:
            phone_number = UserInfo.objects.get(user = user).phone_number
        except ObjectDoesNotExist:
            phone_number = ""
        response = {
            'form': UserInfoForm(instance=user,initial={"phone_number": phone_number})
        }
        return render(request,"users/userinfo.html",response)

    def post(self, request):
        response = {}
        form = UserInfoForm(request.POST)
        response['form'] = form
        if form.is_valid():
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            try:
                userinfo = UserInfo.objects.get(user=user)
                userinfo.phone_number = phone_number
            except ObjectDoesNotExist:
                userinfo = UserInfo(user = user, phone_number = phone_number)
            user.save()
            userinfo.save()
            response['message'] = "User Updated Seccess"
            return render(request,"users/userinfo.html",response)
        else:
            response['error_message'] = "Updation Failed"
            return render(request,"users/userinfo.html",response)

user_info_view = UserInfoView.as_view()


class AccountDeactivate(View):
    
    def get(self, request):
        return render(request,"users/userdeactivate.html")

    def post(self, request):
        user = request.user
        user.is_active = False
        user.save()
        logout(request)
        return redirect("/login/")

account_deactivate_view =  AccountDeactivate.as_view()