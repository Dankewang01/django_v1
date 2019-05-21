from django.shortcuts import render, render_to_response
from django.http import HttpResponse,Http404 ,HttpResponseRedirect
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.template import loader

# Create your views here.


def do_normalmap(request):
    print("in do_normalmap")
    return HttpResponse("this is normalmap")

def get_date(request,year,month):
    return HttpResponse("datetime is {0},{1}".format(year,month))

def do_app(r):
    print("in app")
    return HttpResponse("this is app route")

def do_pagenumber(r,page_number):
    return HttpResponse("page number is {0}".format(page_number))

def extremparam(r,name):
    #print("pass")
    return  HttpResponse("myname is {0}".format(name))

def revParse(r):
    print("in reParse")
    return redirect(reverse("askname",args=None))
    #return  HttpResponse("your requested URL is {0} ".format(reverse=("askname")))

def test(request):
    return render(request,"hello.html")

def test_erro(r):
    raise Http404
    return HttpResponse("OK")

def v1_1(r):
    return HttpResponseRedirect('/v11')
def v1_2(r):
    return  HttpResponseRedirect(reverse('/v11'))
def v2(r):
    return HttpResponse('/v2,重定向页面')

def v8(r):
    rst = ''
    for k,v in r.GET.items():
        rst += k + "-->" + v
        rst += " , "
    return HttpResponse("get value of R is {0}".format(rst))


def v9_get(request):
    #渲染模板
    return render_to_response("hello.html")

def v9_post(request):
    rst = ''
    #获取request.POST.items()获取form表单传递数据
    for k,v in request.POST.items():
        rst += k + "-->" + v
        rst += " , "
    return HttpResponse("get value of R is {0}".format(rst))

def render_test1(request):
    print("this is render 1 ")
#环境变量
    rsp = render(request,"render.html")
    #rsp = render_to_response("render.html")
    print(type(rsp))
    return rsp

def render_test2(request):
    print("this is render 2 ")
#环境变量
    c = dict()
    c['name']= 'danke'
    rsp = render(request,"render2.html" ,context=c)
    #rsp = render_to_response("render.html")
    print(type(rsp))
    return rsp

def render_test3(request):
    print("this is render 3 ")
    #手动加载模板
    t = loader.get_template("render3.html")
    #添加参数
    r = t.render({"name":"danke"})
    print(type(r))
    return HttpResponse(r)

def render_rsponse(request):

    rsp = render_to_response("render3.html", context={'name':'danke 2'})
    return  rsp

def get_404(request):
    from django.views import defaults
    return defaults.page_not_found(request,Exception)

