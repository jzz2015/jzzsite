from django.http import HttpResponse
def hello(request):
	return HttpResponse("Hello, world. You're at the polls index.")
def index(request):
	context         = {}
	return render(request, 'index.html', context)
