from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import Question, Choice

# Create your views here.

def index(request):
	lattest_questions = Question.objects.all().order_by('-pub_date')[:7]

	return render(request, 'index.html', {'questions':lattest_questions})
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

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)