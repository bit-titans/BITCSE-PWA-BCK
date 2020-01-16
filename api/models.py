from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faculty(models.Model):
    fid = models.CharField(max_length=6)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    desg = models.CharField(max_length=20)
    quali = models.CharField(max_length=20)

    class Meta:
      db_table = "Faculty"
    def __str__(self):
        return self.name

class Subject(models.Model):
    subcode = models.CharField(max_length=10)
    subname = models.CharField(max_length=100)
    class Meta:
      db_table = "Subject"
    def __str__(self):
        return self.subcode+"-"+self.subname

class Slot(models.Model):
    time = models.CharField(max_length=20)
    class Meta:
      db_table = "Slot"
    def __str__(self):
        return self.time

class TT(models.Model):
    day = models.CharField(max_length=3)
    subject = models.ForeignKey(Subject,models.CASCADE,related_name='TT')
    faculty = models.ForeignKey(Faculty,models.CASCADE,related_name='TT')
    slot = models.ForeignKey(Slot,models.CASCADE,related_name='TT')
    semsec = models.CharField(max_length=2)
    room = models.IntegerField()
    class Meta:
      db_table = "TT"
    def __str__(self):
        return self.day+":"+self.slot.time+":"+self.subject.subname

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pid = models.CharField(max_length=10)
    class Meta:
      db_table = "Profile"
    def __str__(self):
        return self.pid