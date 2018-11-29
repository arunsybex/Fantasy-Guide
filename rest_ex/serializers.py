from django.contrib.auth.models import User, Group
from rest_ex.models import *
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('id', 'name', 'logo')

class MatchesSerializer(serializers.ModelSerializer):
	games = GamesSerializer()
	# match_at = serializers.DateTimeField(format='iso-8601', input_formats=None)
	class Meta:
		model = Matches
		fields = ('id','name','logo','match_at','games')

class SquadSerializer(serializers.ModelSerializer):
	matches = MatchesSerializer(read_only=True)
	class Meta:
		model = Squad
		fields = ('id','name','error','small_league','small_league','content','matches')