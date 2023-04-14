from django.db import models

# Create your models here.

class Ques(models.Model):
    ques = models.CharField(max_length=100,blank=True, null=True)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.ques

class Choice(models.Model):
    ques = models.ForeignKey(Ques, on_delete=models.CASCADE)
    choice = models.CharField(max_length=100,blank=True, null=True)
    votes = models.IntegerField(default = 0)
    
    def __str__(self):
        return self.choice
