from django.shortcuts import render
from .models import PoliticsBlogs
from .models import TravelBlogs
from .models import EducationBlogs
from .models import EntertainmentBlogs
from .models import BusinessBlogs
from .models import LifestyleBlogs
from .models import HealthBlogs
# Create your views here.



def travel(request):
    travelBlogs = TravelBlogs.objects.all()
    context ={'travelBlogs':travelBlogs} 
    return render(request,'posts/travel.html',context)




def travelDetailed(request,pk):
    travelBlogs = TravelBlogs.objects.get(id=pk)
    context ={'travelBlogs':travelBlogs} 
    return render(request,'posts/travelDetailed.html',context)




def politics(request):
    politicsBlogs = PoliticsBlogs.objects.all()
    context ={'politicsBlogs':politicsBlogs} 
    return render(request,'posts/politics.html',context)




def politicsDetailed(request,pk):
    politicsBlogs=PoliticsBlogs.objects.get(id=pk)
    context={'politicsBlogs':politicsBlogs}
    return render(request,'posts/politicsDetailed.html',context)




def entertainment(request,):
    entertainmentBlogs = EntertainmentBlogs.objects.all()
    context ={'entertainmentBlogs':entertainmentBlogs} 
    return render(request,'posts/entertainment.html',context)





def entertainmentDetailed(request,pk):
    entertainmentBlogs = EntertainmentBlogs.objects.get(id=pk)
    context ={'entertainmentBlogs':entertainmentBlogs} 
    return render(request,'posts/entertainmentDetailed.html',context)




def business(request):
    businessBlogs = BusinessBlogs.objects.all()
    context ={'businessBlogs':businessBlogs} 
    return render(request,'posts/business.html',context)




def businessDetailed(request,pk):
    businessBlogs = BusinessBlogs.objects.get(id=pk)
    context ={'businessBlogs':businessBlogs} 
    return render(request,'posts/businessDetailed.html',context) 




def health(request):
    healthBlogs = HealthBlogs.objects.all()
    context ={'healthBlogs':healthBlogs} 
    return render(request,'posts/health.html',context)




def healthDetailed(request,pk):
    healthBlogs = HealthBlogs.objects.get(id=pk)
    context ={'healthBlogs':healthBlogs} 
    return render(request,'posts/healthDetailed.html',context)



def lifestyle(request):
    lifestyleBlogs = LifestyleBlogs.objects.all()
    context ={'lifestyleBlogs':lifestyleBlogs} 
    return render(request,'posts/lifestyle.html',context)




def lifestyleDetailed(request,pk):
    lifestyleBlogs = LifestyleBlogs.objects.get(id=pk)
    context ={'lifestyleBlogs':lifestyleBlogs} 
    return render(request,'posts/lifestyleDetailed.html',context)





def education(request):
    educationBlogs = EducationBlogs.objects.all()
    context ={'educationBlogs':educationBlogs} 
    return render(request,'posts/education.html',context)




def educationDetailed(request,pk):
    educationBlogs = EducationBlogs.objects.get(id=pk)
    context ={'educationBlogs':educationBlogs} 
    return render(request,'posts/educationDetailed.html',context) 

  