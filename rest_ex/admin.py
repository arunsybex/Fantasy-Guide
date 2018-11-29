# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from rest_ex.models import *

# Register your models here.

class GamesAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'logo')

class MatchesAdmin(admin.ModelAdmin):
	list_display = ('id', 'games','name', 'logo','match_at')

class SquadAdmin(admin.ModelAdmin):
	list_display = ('id','matches','matches','name')

admin.site.register(Games, GamesAdmin)
admin.site.register(Matches, MatchesAdmin)
admin.site.register(Squad, SquadAdmin)