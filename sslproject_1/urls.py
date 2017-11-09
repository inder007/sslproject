
from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^departments/', include('fpagecse.urls')),
    url(r'^$', views.homepage),
    url(r'login/$', views.login),
]
