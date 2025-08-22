from django.urls import path
from .views import analyze_view



urlpatterns = [
     path('', analyze_view, name='home'), 
    path('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', analyze_view, name="home"),]
