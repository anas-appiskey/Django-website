from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Question, Choice
# Create your views here.

#note 
#request is pass whenever you do anything

#this function will display whatever in the index()
class IndexView(generic.ListView):
    
    template_name = 'polls/index.html'
    #you can change this question_list by using this variable
    
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five pub"""
        return Question.objects.order_by('-pub_date')[:5]

    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    
    # #this context pass the variable latest_qstn_list to the template 
    # # index.html file throught render 
    # #the thing we are accessing is the context dict key 
    # context = {
    #     'latest_question_list' : latest_question_list,
    # }
    # return render(request ,'polls/index.html', context)
    
"""in this case the id is the PK"""

class DetailsView(generic.DetailView):
    # try:
    #     question = Question.objects.get(pk = question_id)
    # except Question.DoesNotExist:
    #     raise Http404("question does not match")
   
    # question = get_object_or_404(Question ,pk = question_id)
    # return render(request , 'polls/details.html', {'question': question})
    model = Question
    template_name = 'polls/details.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

    # question = get_object_or_404(Question , pk = question_id)
    # return render(request , 'polls/results.html',{'question' : question})

def vote(request, question_id):

    question = get_object_or_404(Question, pk= question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    
    #doesnotexist not have exists
    except (KeyError, Choice.DoesNotExist):
        #Redisplay the question voting form
        return render(request, 'polls/details.html',{
            'question' : question,
            'error_message' :"you didn't select a choice ",
        })
    else:
        selected_choice.votes +=1
        selected_choice.save()
    
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        
        #2.13.58
        return HttpResponseRedirect(reverse('polls:results', args =(question.id,)))
















