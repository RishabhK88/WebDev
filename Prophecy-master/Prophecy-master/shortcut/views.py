from django.shortcuts import render
from django.http import HttpResponse
from .models import formdeets
# Create your views here.

def home(request):
    return render(request,'landing.html',{'name': 'Rishabh'})

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
            if ans1.lower() == 'the prophecy' and ans2.lower() == 'recon' and ans3.lower() == 'noon' and ans4.lower() == 'talent unfolds prophecy':
                qualified = True
            formdeets.objects.create(name=name, rno=rno, email=email, branch= branch,qualified=qualified, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4)
            if qualified == True :
                return render(request, 'end.html', {'result' : 'Qualified'})
            else:
                return render(request, 'end.html', {'result' : 'Oops'})
        except Exception as e:
            return render(request, 'end.html', {'result': f"An error occurred. Please try again. Error : {e}"})
    else:
        return render(request, 'index.html')


# def qviews(request):
#      return render(request, 'end.html', {'result' : 'Oops'})

def qimage(request):
     return render(request, 'image.html')