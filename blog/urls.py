from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('post/<int:id>/',views.post_detail,name='post_detail'),
    path('post_details/<int:post_id>/',views.demo,name='demo'),
    path('indexhtml',views.indexhtml,name='indexhtml'),

    
    path('get/<int:slug>', views.post_detail, name='post_detail'),
    ]
    