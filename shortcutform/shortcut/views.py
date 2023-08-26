from django.shortcuts import render
from django.http import HttpResponse
from .models import formdeets
# Create your views here.

def home(request):
    return render(request,'index.html',{'name': 'Mini'})

def formm(request):

    if request.method == 'POST':
        try:
            data = request.POST.dict()
            name = data['name']
            rno = data['rno']
            email = data['email']
            branch = data['branch']
            ans1 = data['ans1']
            ans2 = data['ans2']
            ans3 = data['ans3']
            ans4 = data['ans4']
            qualified = False
            if ans1 == '1' and ans2 == '1' and ans3 == '1' and ans4 == '1':
                qualified = True
            formdeets.objects.create(name=name, rno=rno, email=email, branch= branch,qualified=qualified, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4)
            if qualified == True :
                return render(request, 'qview.html', {'result' : 'Qualified'})
            else:
                return render(request, 'qview.html', {'result' : 'Oops'})
        except Exception as e:
            return render(request, 'qview.html', {'result': f"An error occurred. Please try again. Error : {e}"})
    else:
        return render(request, 'form.html')

def qviews(request):
     return render(request, 'qview.html', {'result' : 'Oops'})