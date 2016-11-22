from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from qa.models import Question
from qa.forms import AnswerForm, AskForm, UserForm
from django.contrib.auth import login
from django.contrib.auth.models import User
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
  form = AnswerForm()
  return render(request, 'qa/question_details.html', {
    'form': form,
    'question': question
  })

def answer_add(request):
  if request.method == "POST":
    form = AnswerForm(request.POST)

    if form.is_valid():
      answer = form.save()
      url = answer.get_url()
      return HttpResponseRedirect(url)

  else:
    form = AnswerForm()
  return render(request, 'qa/answer_add.html', {
    'form': form
  })

def question_add(request):
  if request.method == "POST":
    form = AskForm(request.POST)

    if form.is_valid():
      question = form.save()
      url = question.get_url()
      return HttpResponseRedirect(url)

  else:
    form = AskForm()
  return render(request, 'qa/question_add.html', {
    'form': form
  })

def sign_up(request):
  if request.method == "POST":
    form = UserForm(request.Post)
    if form.is_valid():
      user = User.objects.create(**form.cleaned_data)
      login(user)
      return HttpResponseRedirect('/')
  else:
    form = UserForm()
  return render(request, 'qa/sign_up.html', {
    'form': form
  })

def login(request):
  pass
