from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
from blog.models import *
def hello(request):
	return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
	string = "jzz3"
	return render(request, 'index.html', {'username' : string})
def blog(request):
    blog_list = Article.objects.all()
    return render_to_response('blog.html',{'blog_list':blog_list})
def test(request):
    blog_list = Article.objects.filter(writer="jzz")
    return render_to_response('test.html',{'blog_list':blog_list})
def writeblog(request):
	string = "jzz2016"
	return render(request, 'writeblog.html', {'authorname' : string})
def wbsub(request): 
	request.encoding='utf-8'
	if 'wb-title' in request.GET:
		wbtitle = request.GET['wb-title'].encode('utf-8')
		wbcontent = request.GET['wb-content'].encode('utf-8')
		test1 = Article(title=wbtitle,content=wbcontent)
		test1.save()
	else:
		message = 'null'
	return HttpResponse(wbtitle)