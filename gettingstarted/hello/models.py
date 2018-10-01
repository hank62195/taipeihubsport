from django.db import models

# Create your models here.
#class Greeting(models.Model):
 #   when = models.DateTimeField('date created', auto_now_add=True)

class Member(models.Model):
    mId = models.CharField(max_length = 20) #, null=False
    mName = models.CharField(max_length = 20)
    mDepartment = models.CharField(max_length = 20)
    mEmail = models.CharField(max_length = 30)
    mPassword = models.CharField(max_length = 6)
    mMoney = models.CharField(max_length = 10, default = '1000')

    def __str__(self):
        return self.mId

class Team(models.Model):
    tId = models.CharField(max_length = 6, unique = True)
    tName = models.CharField(max_length = 20)
    tMember1 = models.CharField(max_length = 20)
    tMember2 = models.CharField(max_length = 20)
    tDepartment = models.CharField(max_length = 20, default = '')
    tGame1= models.CharField(max_length = 40, null = True, blank = True, default = ' ') #gid
    tGame2= models.CharField(max_length = 40, null = True, blank = True, default = ' ')
    tGame3= models.CharField(max_length = 40, null = True, blank = True, default = ' ')
    tGame4= models.CharField(max_length = 40, null = True, blank = True, default = ' ')
    tGame5= models.CharField(max_length = 40, null = True, blank = True, default = ' ')
    tGame6= models.CharField(max_length = 40, null = True, blank = True, default = ' ')
    tGame7= models.CharField(max_length = 40, null = True, blank = True, default = ' ')

    def __str__(self):
        return self.tId