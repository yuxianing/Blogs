# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# 伪视图
# from django.shortcuts import render_to_response
# from datetime import datetime
# from blog.models import BlogArticle
# Create your views here.

# def archive(request):
# 	post = BlogArticle(title = 'mocktitle', body = 'mockbody', timestamp = datetime.now())
# 	return render_to_response('archive.html', {'articles':[post]})

# 真实视图
from django.http import HttpResponse
from django.template import loader, Context, RequestContext
from blog.models import BlogArticle, BlogForm
from django.shortcuts import *
from datetime import datetime
from django.views.generic import TemplateView

def archive(request):
	articles = BlogArticle.objects.all()
	
	return render(request, 'archive.html', {'articles':articles, 'form': BlogForm()})

def create_article(request):
	if request.method == 'POST':
		print request.POST
		form = BlogForm(request.POST)
		if form.is_valid():
			post = form.save(commit = False)
			post.timestamp = datetime.now()
			post.save()
	return HttpResponseRedirect('/blog/')