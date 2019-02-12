from django.db import models

class Bootcamp(models.Model):
	title = models.CharField(max_length = 100)
	code = models.CharField(max_length = 6, unique = True)

	def __str__(self):
		return self.title

class Student(models.Model):
	name = models.CharField(max_length = 50)
	bootcamp = models.ForeignKey(Bootcamp, on_delete = models.CASCADE, null = True, blank = True)

	def __str__(self):
		return self.name

class Idea(models.Model):
	name = models.CharField(max_length = 120)
	desc = models.TextField(blank = True, null = True)
	student = models.OneToOneField(Student, on_delete = models.CASCADE)

	def __str__(self):
		return self.name


class Choice(models.Model):
	student = models.ForeignKey(Student, on_delete = models.CASCADE)
	choice1 = models.ForeignKey(Idea, on_delete = models.CASCADE, related_name = 'choice1')
	choice2 = models.ForeignKey(Idea, on_delete = models.CASCADE, related_name = 'choice2')
	choice3 = models.ForeignKey(Idea, on_delete = models.CASCADE, related_name = 'choice3')

	def __str__(self):
		return self.choice1