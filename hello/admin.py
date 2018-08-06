from django.contrib import admin
from hello.models import Member
from hello.models import Team

# Register your models here.
class MemberAdmin(admin.ModelAdmin): #讓後台管理可以顯示下列資料
   list_display=('id', 'mId', 'mName', 'mDepartment', 'mEmail', 'mPassword', 'mMoney')

class TeamAdmin(admin.ModelAdmin): #讓後台管理可以顯示下列資料
   list_display=('id', 'tId', 'tName', 'tMember1', 'tMember2','tDepartment', 'tGame1', 'tGame2',
                 'tGame3', 'tGame4', 'tGame5', 'tGame6', 'tGame7')

admin.site.register(Member, MemberAdmin) #需註冊model在此
admin.site.register(Team, TeamAdmin) #需註冊model在此