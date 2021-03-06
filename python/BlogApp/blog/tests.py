# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.test import TestCase
from datetime import datetime
from django.test.client import Client
from blog.models import BlogArticle
# Create your tests here.

class BLogTest(TestCase):
	def test_obj_create(self):
		BlogArticle.objects.create(title='raw title',
			body='raw body', timestamp = datetime.now())
		self.assertEqual(1, BlogArticle.objects.count())
		self.assertEqual('raw title', BlogArticle.objects.get(id=1).title)

	def test_home(self):
		response = self.client.get('/blog/')
		self.failUnlessEqual(response.status_code, 200)

	def test_slash(self):
		response = self.client.get('/')
		self.assertIn(response.status_code, (301, 302))

	def test_empty_create(self):
		response = self.client.get('/blog/create/')
		self.assertIn(response.status_code, (301,302))

	def test_post_create(self):
		response = self.client.post('/blog/create/', {
			'title' : 'post title',
			'body' : 'my baby',
		})
		self.assertIn(response.status_code, (301, 302))
		self.assertEqual(1, BlogArticle.objects.count())
		self.assertEqual('my baby', BlogArticle.objects.get(id=1).body)

