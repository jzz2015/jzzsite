from django.db import models
from django.http import HttpResponse

class user(models.Model):
    userno = models.CharField(max_length=11)
    username = models.CharField(max_length=30)
    age = models.CharField(max_length=11)
    def __unicode__(self):
    	return self.username

class visitor(models.Model):
	visitorno = models.CharField(max_length=11)
	visitorname = models.CharField(max_length=30)
	visitorage = models.CharField(max_length=11)
	def __unicode__(self):
		return self.visitorname
class Article(models.Model):
    title = models.CharField(u'title', max_length=256)
    content = models.TextField(u'content')
    writer = models.CharField(max_length=30)
    pub_date = models.DateTimeField(u'pubtime', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'updatetime',auto_now=True, null=True)
    def __unicode__(self):
        return self.title

def ArticleShow(request):
    response = ""
    response1 = ""
    list = Article.objects.all()
    for var in list:
        response1 += "title is"+ var.title + " and the content is:" + var.content + " "
    response = response1
    return HttpResponse("<p>" + response + "</p>")