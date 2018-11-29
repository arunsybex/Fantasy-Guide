from django.conf.urls import url, include
from rest_framework import routers
from rest_ex.views import *
from django.contrib import admin

# router = routers.DefaultRouter()
# router.register(r'users', GamesViewSet)
# # router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^games_list/', GamesViewSet.as_view()),
    url(r'^match_list/', MatchesViewSet.as_view()),
    url(r'^squad_list/', SquadViewSet.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]