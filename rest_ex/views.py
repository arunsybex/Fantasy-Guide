from django.contrib.auth.models import User, Group
from rest_framework import viewsets,generics
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_ex.serializers import *
from rest_ex.models import *
from rest_framework.response import Response
from rest_framework.views import APIView

class GamesViewSet(APIView):

	def get(self,request):
		queryset = Games.objects.all()
		gameserializer = GamesSerializer(queryset,many=True)
		return Response(gameserializer.data)

class MatchesViewSet(APIView):

	def get(self,request):
		game_id = request.GET.get('game',0)
		queryset = Matches.objects.filter(games_id = game_id)
		matchesserializer = MatchesSerializer(queryset,many=True)
		return Response(matchesserializer.data)

class SquadViewSet(APIView):

	def get(self,request):
		match_id = request.GET.get('match',0)
		queryset = Squad.objects.filter(matches_id = match_id)
		squadserializer = SquadSerializer(queryset,many=True)
		return Response(squadserializer.data)

# class GamesViewSet(viewsets.ModelViewSet):
# 	queryset = Games.objects.all()
# 	serializer_class = GamesSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)

# class MatchesViewSet(viewsets.ModelViewSet):
# 	queryset = Matches.objects.all()
# 	serializer_class = MatchesSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)

# class SquadViewSet(viewsets.ModelViewSet):
# 	queryset = Squad.objects.all()
# 	serializer_class = SquadSerializer
# 	permission_classes = (IsAuthenticatedOrReadOnly,)