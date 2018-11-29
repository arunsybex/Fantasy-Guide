# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Games(models.Model):
	name  = models.CharField(max_length=120, null=True, blank=True)
	logo  = models.CharField(max_length=120, null=True, blank=True)

	# def __str__(self):
	# 	return self.name		

class Matches(models.Model):
	games = models.ForeignKey(Games,related_name='games')
	name  = models.CharField(max_length=120, null=True, blank=True)
	logo  = models.CharField(max_length=120, null=True, blank=True)
	match_at =  models.DateTimeField(blank=True)


	# def __str__(self):
	# 	return self.name

class Squad(models.Model):
	matches = models.ForeignKey(Matches,related_name='matches')
	name = models.CharField(max_length=120, null=True, blank=True)
	error = models.CharField(max_length=120, null=True, blank=True)
	small_league = models.CharField(max_length=120, null=True, blank=True)
	grand_league = models.CharField(max_length=120, null=True, blank=True)
	content = models.CharField(max_length=250, null=True, blank=True)

	# def __str__(self):
	# 	return self.name