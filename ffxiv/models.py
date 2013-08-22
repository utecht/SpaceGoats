from django.db import models
from django.contrib.auth.models import User
from django import forms
from goatnails.db.models import ImageWithThumbsField

class Character(models.Model):
    name = models.CharField(max_length=100)
    player = models.ForeignKey(User, related_name='ffxiv+')
    server = models.CharField(max_length=100)
    levels = models.ManyToManyField('Job', through='Level')
    picture = ImageWithThumbsField(upload_to = "uploads", blank=True)
    def __unicode__(self):
        return self.name

class Job(models.Model):
    name = models.CharField(max_length=20)
    abv = models.CharField(max_length=3)
    icon = ImageWithThumbsField(upload_to = "uploads", blank=True)
    def __unicode__(self):
        return self.abv

class Level(models.Model):
    character = models.ForeignKey(Character)
    job = models.ForeignKey(Job)
    level = models.IntegerField()
    def __unicode__(self):
        return "{} {} {}".format(self.character, self.job, self.level)

class Article(models.Model):
    author = models.ForeignKey(User, related_name='ffxiv+')
    title = models.CharField(max_length=50)
    text = models.TextField()
    creation_date = models.DateField(auto_now=True)
    def __unicode__(self):
        return title

class ArticleForm(forms.Form):
    title = forms.CharField(max_length=50)
    text  = forms.CharField(widget=forms.Textarea)

class Screenshot(models.Model):
    user = models.ForeignKey(User)
    caption = models.CharField(max_length=500, blank=True)
    creation_date = models.DateField(auto_now=True)
    image = ImageWithThumbsField(upload_to = "uploads", blank=True)
    def __unicode__(self):
        return self.caption

class ScreenshotForm(forms.Form):
    caption = forms.CharField(max_length=500)
    img = forms.ImageField()
