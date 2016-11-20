from django.shortcuts import render
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

  paginatior = Paginatior(questions, 10)
  page = paginator.page(page)

  return render(request, 'qa/question_main.html', {
    'questions': page.object_list,
    'page': page
  })

def question(request, slug):
  question = get_object_or_404(Question, slug=slug)
  return render(request, 'qa/question_details.html', {
    'question': question
  })
