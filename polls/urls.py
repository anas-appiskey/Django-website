from django.urls import path
from . import views

appname = 'polls'
urlpatterns = [
    #it displays the views file function index 
   # the 'name' value as called by the {% url %} template tag
    path('',views.index, name = "index"),
    #ex : polls/5
    path('<int:question_id>/',views.details, name = "details"),
    
    #ex : polls/5/results
    path('<int:question_id>/results',views.results, name = "results"),
   
    #ex : polls/5/vote
     path('<int:question_id>/vote',views.vote, name = "vote"),
 
]