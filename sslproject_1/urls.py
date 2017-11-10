
from django.conf.urls import include, url
from django.contrib import admin
# from home.core import views as core_views
from home import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^departments/', include('fpagecse.urls')),
    # url(r'^$', include('home.urls')),
    url(r'^$', views.homepage),
    # url(r'login/$', views.login),
    url(r'login/$', views.login),
    url(r'signup/$', views.add_model),
    # url(r'search/$', views.submit),
    # url(r'^signup/$', core_views.signup, name='signup'),
    # url(r'signup/$', views.add_model, name='form'),
]
