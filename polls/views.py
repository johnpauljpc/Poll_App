from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
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


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'results.html', {'question': question})