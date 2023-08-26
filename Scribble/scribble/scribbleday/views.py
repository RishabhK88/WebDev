from django.shortcuts import render
from scribbleday.models import Message
from django.contrib.auth.models import User
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MsgForm

@login_required
def index(request):
    msgs = Message.objects.all()
    m = []
    for msg in msgs:
        if(str(msg.reciever)==request.user.username):
            m.append(msg)
            # s.append(msg.sender)
            print(msg.message)
    return render(request, 'm.html', {'m': m})

@login_required
def msg(request):
    form = MsgForm(request.POST or None)
    u = User.objects.all()
    m = []
    for i in u:
        if(i.username!=request.user.username):
            m.append(i.username)
    context ={'m': m}
    if form.is_valid():
        
        form.instance.sender = request.user
        if request.method=="POST":
            data = request.POST.dict()
            u = User.objects.get(username=data['reciever'])
            print(data['reciever'])
            # x = User.objects.filter()
            form.instance.reciever = u
            # print(User.objects.get(reciever=data['reciever']))
        form.save()
        context ={'m': m, 'mes': f"Your message has been sent."}
        return render(request, "f.html", context)
    context['form']= form
    
    return render(request, "f.html", context)
    # return HttpResponse("Hello, world. You're at the polls index.")