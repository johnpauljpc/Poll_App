from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Question, Choice
from django.views.generic import (CreateView, DetailView,
    ListView, View, UpdateView)

# Create your views here.

class index(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        return Question.objects.all().order_by('-pub_date')[:5]

class detail(DetailView):
    model = Question
    template_name = 'detail.html'
    #context_object_name = 'question'


'''
def detail(request, question_id):
    try:
        question = Question.objects.get(id = question_id)
        context = {
        'question':question
             }
    
    except Question.DoesNotExist:
        #raise Http404("Question does not exist....")
        return  render(request, 'index.html')

    return  render(request, 'detail.html', context)
'''



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    return HttpResponse("You're voting on question %s." % question_id)


class results(DetailView):
    model = Question
    template_name = 'results.html'
    context_object_name = 'question'