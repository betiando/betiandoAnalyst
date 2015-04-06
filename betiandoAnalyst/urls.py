from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'betiandoAnalyst.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'analyst.views.home', name='home'),
	url(r'^data$', 'analyst.views.data', name='data'),
	url(r'^data/all/(?P<data_id>[0-9]+)/$', 'analyst.views.dataallentries', name='dataallentries'),
    url(r'^admin/', include(admin.site.urls)),
]
