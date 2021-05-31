from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('MyAPI',views.PredictionView)
urlpatterns = [
    path('',views.apiView,name='userform'),
]