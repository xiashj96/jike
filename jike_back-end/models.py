from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Member(models.Model):
	password = models.CharField(max_length=200)
	name = models.CharField(max_length=100)
	phone = models.CharField(max_length=300)
	email = models.CharField(max_length=300)

class Courserecord(models.Model):
	cID = models.CharField(max_length=100)
	cName = models.CharField(max_length=100)
	uploadername = models.CharField(max_length=300)
	uploadTime = models.CharField(max_length=100)
	clickTime = models.IntegerField(default=0)
	fileAddress = models.CharField(max_length=300)

class News(models.Model):
	topic = models.CharField(max_length=100)
	nName = models.CharField(max_length=300)
	createTime = models.TimeField()
	activityTime = models.TimeField()
	Location = models.CharField(max_length=200)
	signURL = models.URLField()

class Discussion(models.Model):
	topic = models.CharField(max_length=100)
	postId = models.ForeignKey(Member)
	discussTime = models.TimeField()
	content = models.TextField()

class Jkuser(models.Model):
	id = models.IntegerField(max_length=20)
	username = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	credit = models.IntegerField(default=100)
	
class Jkother(models.Model):
	id = models.IntegerField(max_length=20)
	name = models.CharField(max_length=200)
	typeID = models.CharField(max_length=100)
	content = models.CharField(max_length=800)
	link = models.CharField(max_length=200)
	fileAddress = models.CharField(max_length=300)
	uploader = models.CharField(max_length=200)
	uploadtime = models.CharField(max_length=200)
	clicktime = models.IntegerField(default=0)

class Jkmooc(models.Model):
	id = models.IntegerField(max_length=20)
	name = models.CharField(max_length=200)
	school = models.CharField(max_length=200)
	typeID = models.CharField(max_length=100)
	content = models.CharField(max_length=3000)
	link = models.CharField(max_length=200)
	uploader = models.CharField(max_length=200)
	uploadtime = models.CharField(max_length=200)
	clicktime = models.IntegerField(default=0)
	teacher = models.CharField(max_length=200)
	img = models.CharField(max_length=200)

class Jkinterest(models.Model):
	username = models.CharField(max_length=200)
	interest = models.CharField(max_length=100)

class Jkmooccollection(models.Model):
	username = models.CharField(max_length=200)
	courseID = models.IntegerField(max_length=20)

class Jkothercollection(models.Model):
	username = models.CharField(max_length=200)
	otherID = models.IntegerField(max_length=20)

class Jkreport(models.Model):
	resourceID = models.IntegerField(max_length=20)
	resourceTitle = models.CharField(max_length=200)
	userName = models.CharField(max_length=200)
	context = models.CharField(max_length=800)


