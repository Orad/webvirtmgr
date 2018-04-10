import json
from inspect import isfunction

from rest_framework import status
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator

from django.contrib.auth.models import User


class _cbv_decorate(object):
    def __init__(self, dec):
        self.dec = method_decorator(dec)

    def __call__(self, obj):
        obj.dispatch = self.dec(obj.dispatch)
        return obj

def patch_view_decorator(dec):
    def _conditional(view):
        if isfunction(view):
            return dec(view)
        return _cbv_decorate(dec)(view)
    return _conditional

def token_required(verify_token):
    def wrapper(request, *args, **kwargs):
        if "HTTP_AUTHORIZATION" not in request.META:
            return HttpResponse(json.dumps({"data":{}, "message": "Token is not valid!"}),content_type="application/json",status=status.HTTP_404_NOT_FOUND)

        token = request.META["HTTP_AUTHORIZATION"]
        user_token = User.objects.all()[0].user_detail.token
        if token != user_token:
            return HttpResponse(json.dumps({"data":{}, "message": "Token is not valid!"}),content_type="application/json",status=status.HTTP_404_NOT_FOUND)
        return verify_token(request, *args, **kwargs)    
    return wrapper