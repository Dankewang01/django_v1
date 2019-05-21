from django.conf.urls import include, url
from django.contrib import admin
from test_app import  views as vs
from test_app import test_app_urls
#from test_views import  views as v
from django.core.urlresolvers import reverse
urlpatterns = [
    # Examples:
    # url(r'^$', 'Danke_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^normalmap/', vs.do_normalmap),
    # ^ 后面是正则表达式
    #   ？P<xx> xx未参数
    url(r'^date/(?P<year>[0-9]{4})/(?P<month>[0,1][0-9])', vs.get_date),
    #子路由跳转
    url(r'^apps/', include(test_app_urls)),
    url(r'^book/(?:page-(?P<page_number>\d+)/)$', vs.do_pagenumber),
    url(r'^yourname/$',vs.extremparam,{'name':'danke'}),
  #反向解析URL
    #url(r'^mayiknowyourname/$',vs.revParse, name = 'askname' ),
   #  url(r'^test_views/$',v.test_viwes),
   # url(r'^erro/$',v.tetst_erro),

#重定向路由实例
    url(r'^v1_1',vs.v1_1),
    url(r'^v1_2',vs.v1_2),
    url(r'^v2',vs.v2,name='v2'),

   #字典类(QueryDict)URL查询
    # http://127.0.0.1:8000/v8/?name=wzp&age=18
    url(r'^v8',vs.v8),

    #get url
    url(r'^v9_get', vs.v9_get),
    #post url
    url(r'^v9_post', vs.v9_post),

    url(r'^render_test/$', vs.render_test1),
    url(r'^render_test2/$', vs.render_test2),
    url(r'^render_test3/$', vs.render_test3),
    url(r'^render_test4/$', vs.render_rsponse),

    url(r'^get_404/$', vs.get_404),


]
