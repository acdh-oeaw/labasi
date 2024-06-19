from django.urls import re_path
from django_spaghetti.views import plate

app_name = 'django_spaghetti'

urlpatterns = [
    re_path(r'^$', plate, name='plate'),
]
