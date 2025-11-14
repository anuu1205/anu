# from django.urls import path
# from.import views
# urlpatterns=[
   
#    path('forms',views.contact_view,name='contact_view'),

    
    
#     ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact_view'),  # '' not 'forms'
]
