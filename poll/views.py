from django.shortcuts import render,get_object_or_404,reverse
from django.http import Http404,HttpResponseRedirect
from .models import Ques,Choice
# Create your views here.

def landing(request):
    return render(request,'polls/landing.html')
def index(request):
    list = Ques.objects.order_by('-pub_date')[:5]
    context = {'list': list}
    return render(request, 'polls/index.html', context)

    
def detail(request, ques_id):
    try:
        question = Ques.objects.get(pk = ques_id)
    except Ques.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Ques, pk = question_id)
    return render(request, 'polls/results.html', {'question': question})
    
def vote(request,question_id):
    question = get_object_or_404(Ques,pk = question_id)
    try:
        primary = request.POST['choice']
        select_choice = question.choice_set.get(pk = primary)
        
    except (KeyError,Choice.DoesNotExist):
      return render(request, 'polls / detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        select_choice.votes += 1
        select_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args =(question.id, )))