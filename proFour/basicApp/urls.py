from django.urls import path
from . import views

# Templates taggong
app_name = 'basicApp'

urlpatterns = [
    path('other/',views.other,name='other'),
    path('relative/',views.relative,name='relative'),
]
