# -*- coding: utf-8 -*-
from django import http
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login , logout
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from forms import *
from models import *
from query import *



def index(request):
	if request.user.is_authenticated():
		name = 'نام کاربری: '
		name += str(request.user)
		page_html_inc = 'home.html' 
		return render_to_response('index.html', locals(),context_instance=RequestContext(request) )
	else:
		return HttpResponseRedirect('/login_user/')  
	

def system_manage(request):
	if request.user.is_authenticated():
		name = 'نام کاربری: '
		name += str(request.user)
		page_html_inc = 'system_manage.html' 
		return render_to_response('index.html', locals(),context_instance=RequestContext(request) )
	else:
		return HttpResponseRedirect('/login_user/')  
	
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
                error = "نام کاربری شما فعال نیست"
        else:
            error = "نام کاربری و یا رمز عبور صحیح نیست"

    return render_to_response('index.html', locals() ,context_instance=RequestContext(request))
		
def services(request):
	if request.method == 'POST':
		if 'p' in request.POST and request.POST['p'] == "add_category_save" :
			saved_items = CategoryForm(request.POST)
			if saved_items.is_valid():
				if saved_items.save():
					return HttpResponseRedirect('/services/') 
			else:
				return HttpResponseRedirect('/services/?p=add_category&error=error')  
	else:
		page_title = 'مدیریت دسته بندی ها'
		add_category_form_content = CategoryForm()

		if 'p' in request.GET and request.GET['p'] == "delete_category" :
			cat_del_id = request.GET['category_id']
			cat_del = CategoryList.objects.get(id=cat_del_id)
			cat_del.delete()
			return HttpResponseRedirect('/services/') 

	page_html_inc = 'services.html'

	 
	CATS = []
	for cat in Category.objects.all().order_by('-id'):
		group_name = CategoryParents.objects.filter(id=cat.group_id)
		if cat.parent_id > 0 :
			parent_name = CategoryList.objects.filter(id=cat.parent_id)[0]
		else:
			parent_name = '----'
		delete_icon = "<a href='#' class='delete_category' cat_id='%(cat_id)s' cat_name='%(cat_name)s' ><img src='/static/images/delete.png'></a>" % {'cat_id':cat.id ,'cat_name':cat.name , }
		edite_icon = "<a href='' ><img src='/static/images/edite.png'></a>"
		if cat.enable =='1':
			enable_icon = "<img src='/static/images/tick.png'>"
		else:
			enable_icon = "<img src='/static/images/disable.png'>"
		CATS.append((cat.id,cat.name,cat.subscribe_key,group_name[0],parent_name,enable_icon,delete_icon+'&nbsp;&nbsp;'+edite_icon))
	return render_to_response('index.html', locals() ,context_instance=RequestContext(request))
		
def reports(request):
    page_html_inc = 'reports.html' 
    return render_to_response('index.html', locals() ,context_instance=RequestContext(request))
	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')
