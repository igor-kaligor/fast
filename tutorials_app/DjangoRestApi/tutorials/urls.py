from django.urls import path
from tutorials import views 
 
urlpatterns = [ 
    path(r'tutorials', views.tutorial_list),
    path(r'tutorials/<int:pk>', views.tutorial_detail),
    path(r'tutorials/published', views.tutorial_list_published),
    path(r'tutorials/twice', views.tutorials_twice)
]