from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , Http404

from .models import Question
# Create your views here.

#note 
#request is pass whenever you do anything

#this function will display whatever in the index()
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    #this context pass the variable latest_qstn_list to the template 
    # index.html file throught render 
    #the thing we are accessing is the context dict key 
    context = {
        'latest_question_list' : latest_question_list,
    }
    return render(request ,'polls/index.html', context)

#in this case the id is the PK
def details(request, question_id):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExists:
    #     raise Http404("question does not match")
   
    question = get_object_or_404(Question ,pk = question_id)

    return render(request , 'polls/details.html', {'question': question})

def results(request, question_id):
    response = "you are looking at results of qstn %s. "
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("you are waiting on qstn %s. " % question_id)

