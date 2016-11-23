from django import forms
from qa.models import Question, Answer
from django.contrib.auth.models import User

class AskForm(forms.Form):
  title = forms.CharField(max_length=255)
  text = forms.CharField(widget=forms.Textarea)

  def __init__(self, *args, **kwargs):
    super(AskForm, self).__init__(*args, **kwargs)

  def clean(self):
    return self.cleaned_data

  def save(self):
    question = Question(**self.cleaned_data)
    if self._user is not None and self._user.is_anonymous() == False:
      question.author = self._user
    question.save()
    return question


class AnswerForm(forms.Form):
  text = forms.CharField(widget=forms.Textarea)
  question = forms.ModelChoiceField(queryset = Question.objects.all() )

  def __init__(self, *args, **kwargs):
    super(AnswerForm, self).__init__(*args, **kwargs)

  def clean(self):
    return self.cleaned_data

  def save(self):
    answer = Answer(**self.cleaned_data)
    if self._user is not None and self._user.is_anonymous() == False:
      answer.author = self._user
    answer.save()
    return answer

class UserForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ('username', 'email', 'password')

  def clean(self):
    return self.cleaned_data

  def save(self):
    user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['password'])
    user.email = self.cleaned_data['email']
    user.set_password(self.cleaned_data['password'])
    user.save()
    return user