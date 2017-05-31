from django.conf.urls import *
import blog.views

urlpatterns = [
	url(r'^$',blog.views.archive),
	url(r'^create/',blog.views.create_article),
	]
	