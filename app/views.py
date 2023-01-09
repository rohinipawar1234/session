from django.shortcuts import render,HttpResponse

# Create your views here.
def set_session(request):
    request.session['name']='rohini'
    return render(request,'setsession.html')


def get_session(request):
    if 'name' in request.session:
        name=request.session.get('name')
        return render(request,'getsession.html',{'abc':name})
    else:
        return HttpResponse('your session is expired')    

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'delsession.html')   