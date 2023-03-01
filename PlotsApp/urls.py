from django.urls import path
from . import views
urlpatterns = [
path('',views.index),
path('plots/',views.process_plots),
path('display_form/',views.display_form,name='display_form'),
]