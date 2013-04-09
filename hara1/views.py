# -*- coding: utf-8 -*-
from django import http
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login , logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect

def index(request):
	if request.user.is_authenticated():
		name = 'نام کاربری: '
		name += str(request.user)
		page_html_inc = 'home.html' 
		return render_to_response('index.html', locals(),context_instance=RequestContext(request) )
	else:
		return HttpResponseRedirect('/login/')  

def login_user(request):
    username = password = ''
    page_html_inc = 'login.html' 
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/')  
            else:
                error = "نام کاربری شما فعال نیست "
        else:
            error = "نام کاربری و یا رمز عبور صحیح نیست"
	#test
    return render_to_response('index.html', locals() ,context_instance=RequestContext(request))
		
def services(request):
    page_html_inc = 'services.html' 
    return render_to_response('index.html', locals() ,context_instance=RequestContext(request))
	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')
