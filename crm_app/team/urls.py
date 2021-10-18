from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TeamViewSet, get_my_team, add_member


router = DefaultRouter()
router.register('teams', TeamViewSet, basename='teams')

urlpatterns = [
    path('teams/add_member/', add_member, name='add_member'),
    path('teams/get-my-team/', get_my_team, name='get-my-team'),
    path('', include(router.urls)),

]
