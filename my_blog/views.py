from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello(request):
	
	return HttpResponse("helo..its me again")
#def TestHello(request):
#	f=open("/home/anuxx/framework/src/my_blog/templates/test.html")
#	content=f.read()
#	return HttpResponse(content)
#def TestHello(request):
#	context={}
#	return render(request,'test1.html',context)
def TestHello(request):
	context = {'title':'My first blog - anuxx','content':'Hey there i am learning about Deploying the admin',
				'author':'anuxx'}
	return render(request,'test.html',context)