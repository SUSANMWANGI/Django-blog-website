from django.urls import path
from . import views


urlpatterns = [
    
    path('travel',views.travel,name='travel'),
    path('politics',views.politics,name='politics'),
    path('entertainment',views.entertainment,name='entertainment'),
    path('business',views.business,name='business'),
    path('health',views.health,name='health'),  
    path('lifestyle',views.lifestyle,name='lifestyle'),
    path('education',views.education,name='education'),
    path('travelDetailed/<str:pk>',views.travelDetailed,name='travelDetailed'),
    path('politicsDetailed/<str:pk>',views.politicsDetailed,name='politicsDetailed'),
    path('entertainmentDetailed/<str:pk>',views.entertainmentDetailed,name='entertainmentDetailed'),
    path('businessDetailed/<str:pk>',views.businessDetailed,name='businessDetailed'),
    path('healthDetailed/<str:pk>',views.healthDetailed,name='healthDetailed'),
    path('lifestyleDetailed/<str:pk>',views.lifestyleDetailed,name='lifestyleDetailed'),
    path('educationDetailed/<str:pk>',views.educationDetailed,name='educationDetailed'),




]



