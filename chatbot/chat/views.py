from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
import chatbot.settings
from django.core.files.storage import FileSystemStorage
from chat.models import LOGIN, DETAILS, PROFILE, FILES
# Create your views here.
def index(request):
    return render(request,'index.html')
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def user_register(request):
    d=DETAILS()
    d.username=request.POST.get('uname')
    d.Name=request.POST.get('name')
    d.Ph_no=request.POST.get('ph')
    d.Email=request.POST.get('email')
    d.password=request.POST.get('pswd')
    d.save()
    l=LOGIN()
    l.username=request.POST.get('uname')
    l.password=request.POST.get('pswd')
    l.type="user"
    l.save()
    return render(request,'login.html')
def user_login(request):
    data=LOGIN.objects.all()
    us=request.POST.get('uname')
    ps=request.POST.get('pswd')
    flag=0
    for da in data:
        if us == da.username and ps == da.password:  
            T=da.type
            flag=1
            if T == 'admin':
                return render(request,'admin_h.html')
            elif T == 'user':
                return render(request,'user_h.html')
    if flag == 0:
        return HttpResponse("incorrect username or password")

def profile(request):
    d=PROFILE()
    d.adhaarNO=request.POST.get('ano')
    d.PanNO=request.POST.get('pno')
    d.driveNO=request.POST.get('dno')
    d.voterNO=request.POST.get('vno')
    d.address=request.POST.get('address')
    d.fname=request.POST.get('fname')
    d.mname=request.POST.get('mname')
    d.dob=request.POST.get('dob')
    d.focc=request.POST.get('focc')
    d.mocc=request.POST.get('mocc')
    d.save()
    return render(request,'files.html')

def file(request):
    f=FILES()
    fs=FileSystemStorage()

    a1=request.FILES['adhaar']
    adhaar=fs.save(a1.name,a1)
    f.adhaar=fs.url(adhaar)

    a2=request.FILES['pan']
    pan=fs.save(a2.name,a2)
    f.pan=fs.url(pan)

    a3=request.FILES['voterid']
    voterid=fs.save(a3.name,a3)
    f.voterid=fs.url(voterid)

    a4=request.FILES['drlics']
    drlics=fs.save(a4.name,a4)
    f.drlics=fs.url(drlics)

    a5=request.FILES['rcard']
    rcard=fs.save(a5.name,a5)
    f.rcard=fs.url(rcard)

    a6=request.FILES['sslc']
    sslc=fs.save(a6.name,a6)
    f.sslc=fs.url(sslc)

    a7=request.FILES['plustwo']
    plustwo=fs.save(a7.name,a7)
    f.plustwo=fs.url(plustwo)

    a8=request.FILES['fsslc']
    fsslc=fs.save(a8.name,a8)
    f.fsslc=fs.url(fsslc)

    f.save()
    return HttpResponse('Success')


