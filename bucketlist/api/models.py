# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bucketlist(models.Model):
	"""This class represents the bucketlist model. """
	name = models.CharField(max_length=255, blank=False, unique=True)
	date_created = models.DateTimeField(auto_now_add=True)
	date_modified = models.DateTimeField(auto_now=True)

	def _str_(self):
		"""Return a human readable representation of the model instance."""
		return "{}".format(self.name)
