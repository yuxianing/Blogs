# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class BlogArticle(models.Model):
	title = models.CharField(max_length=150)
	body = models.TextField()
	timestamp = models.DateTimeField()
	class Meta:
		ordering = ['-timestamp']

class BlogForm(forms.ModelForm):
	class Meta:
		model = BlogArticle
		exclude = ('timestamp',)
