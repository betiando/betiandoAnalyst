from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^data$', 'analyst.views.data', name='data'),
]
