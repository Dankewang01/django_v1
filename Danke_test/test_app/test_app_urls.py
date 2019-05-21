from django.conf.urls import include, url
from django.contrib import admin
from . import views



urlpatterns = [
    # Examples:
    # url(r'^$', 'Danke_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # 子路由无需写查找总路由项APPS
    url(r'danke/', views.do_app),


]