from django.shortcuts import render
from .forms import (
	BootcampCreate, 
	IdeaCreate, 
	StudentCreate
	)

from .generator import code_generator


def bootcamp_create(request):
	form = BootcampCreate()
	if request.method == 'POST':
		form = BootcampCreate(request.POST)
		if form.is_valid():
			bootcamp = form.save(commit = False)
			bootcamp.code = code_generator()
			bootcamp.save()


	context = {
	"form": form,
	}

	return render(request, 'bootcamp.html', context)


def idea_create(request):
	form = IdeaCreate()
	if request.method == 'POST':
		form = IdeaCreate(request.POST)
		if form.is_valid():
			form.save()


	context = {
	"form": form, 
	}

	return render(request, 'idea.html', context)



def student_create(request):
	form = StudentCreate()
	if request.method == 'POST':
		form = StudentCreate(request.POST)
		if form.is_valid():
			form.save()


	context = {
	"form": form, 
	}

	return render(request, 'student.html', context)


