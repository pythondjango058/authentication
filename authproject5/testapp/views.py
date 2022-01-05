from django.shortcuts import render,HttpResponseRedirect
from testapp.forms import Registration
from django.contrib.auth.decorators import login_required
# Create your views here.

def signup(request):
    form=Registration()
    if request.method=='POST':
        form=Registration(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'registration/regist.html',{'form':form})

@login_required
def login(request):
    return render(request,'registration/thanks.html')
