from django import forms

from .models import Bootcamp, Idea, Student

class BootcampCreate(forms.ModelForm):
	class Meta:
		model = Bootcamp
		exclude = ['code',]


class IdeaCreate(forms.ModelForm):
	class Meta:
		model = Idea
		fields = '__all__'


class StudentCreate(forms.ModelForm):
	class Meta:
		model = Student
		fields = '__all__'


class BootcampAssign(forms.ModelForm):
	class Meta:
		model = Bootcamp
		fields = ['code',]