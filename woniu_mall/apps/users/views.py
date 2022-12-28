import re

from django.contrib.auth import login
from django.db import DatabaseError
from django.http import HttpRequest, HttpResponseForbidden, HttpResponse
from django.shortcuts import render
from django.views import View

from .models import User


# Create your views here.


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self, request: HttpRequest):
        user_name = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        mobile = request.POST.get('phone')
        allow = request.POST.get('allow')
        msg_code = request.POST.get('sms')
        pic_code = request.POST.get('pic_code')

        if all([user_name, pwd, cpwd, mobile, msg_code, allow]):
            return HttpResponseForbidden('hehe')

        if not re.match(r'^[0-9a-zA-Z-_]{5,20}$', user_name):
            return HttpResponseForbidden('length 5 - 20')

        if not re.match(r'^[0-9a-zA-Z-_]{8,20}$', pwd):
            return HttpResponseForbidden('length 8 - 20')

        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return HttpResponseForbidden('phone number not right')

        if not pwd == cpwd:
            return HttpResponseForbidden('password not equal')

        if allow != 'on':
            return HttpResponseForbidden('agree protocol')

        try:
            user = User.objects.create_user(username=user_name, password=pwd, mobile=mobile)
        except DatabaseError as e:
            return render(request, 'register.html',context={'error_msg':'server error'})
        login(request, user)

        return HttpResponse('register success')
