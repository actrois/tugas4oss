# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from .views import getSystemHealthData

class ViewTest(TestCase):
	def test_get_data(self):
		self.assertIsNotNone(getSystemHealthData())

	def test_get_index(self):
		response = self.client.get('/serverhealth/')
		self.assertEqual(response.status_code, 200)
