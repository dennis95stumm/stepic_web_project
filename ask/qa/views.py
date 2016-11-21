from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from qa.models import Question
from django.core.paginator import Paginator

def test(request, *args, **kwargs):
  return HttpResponse('OK')

def question_list_main(request):
  page = request.GET.get('page', 1)
  questions = None
  if request.path == '/popular/':
    questions = Question.objects.popular()
  else:
    questions = Question.objects.new()

  paginator = Paginator(questions, 10)
  page = paginator.page(page)

  return render(request, 'qa/question_main.html', {
    'questions': page.object_list,
    'page': page
  })

def question_details(request, id):
  question = get_object_or_404(Question, id=id)
  return render(request, 'qa/question_details.html', {
    'question': question
  })
