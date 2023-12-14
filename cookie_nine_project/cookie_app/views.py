from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
# cookie set korar command
def home(request):
    response = render(request, 'home.html')
    response.set_cookie('name','arif')
    # response.set_cookie('name','minhaj uddin arif',max_age=60)# seconds ar jonno
    # response.set_cookie('name','minhaj uddin arif',expires=datetime.utcnow()+timedelta)# onekdin cache korte caile
    return response
# get korar command
def get_cookie(request):
    name = request.COOKIES.get('name')
    print(request.COOKIES)
    return render(request,'get_cookie.html',{'name':name})

# delete korar command
def delete_cookie(request):
    response = render(request, 'delete_cookie.html')
    response.delete_cookie('name')
    return response