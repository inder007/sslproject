from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='home'),
    # url(r'^login/$', views.UserFormView.as_view(), name='register'),
]