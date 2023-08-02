from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login

# Create your views here.





def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']

        myuser=User.objects.create_user(username,email,password)

        myuser.save()

        messages.success(request, "Your account has been succesfully created.")

        return redirect('login')
        
    return render(request,"authentication/page-register.html")




def login(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']


        user=authenticate(email=email, password=password)

        if user is not None:
            login(request,user)
            return render(request,'index.html')
        

        else:
             messages.error(request,"WRONG CREDENTIALS!")
             return redirect('home')

    return render(request,"authentication/page-login.html")




def home(request):
    return render(request,"index.html")
    