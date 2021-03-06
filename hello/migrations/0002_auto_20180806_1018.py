# Generated by Django 2.0.7 on 2018-08-06 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mId', models.CharField(max_length=20)),
                ('mName', models.CharField(max_length=20)),
                ('mDepartment', models.CharField(max_length=20)),
                ('mEmail', models.CharField(max_length=30)),
                ('mPassword', models.CharField(max_length=6)),
                ('mMoney', models.CharField(default='1000', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tId', models.CharField(max_length=6, unique=True)),
                ('tName', models.CharField(max_length=20)),
                ('tMember1', models.CharField(max_length=20)),
                ('tMember2', models.CharField(max_length=20)),
                ('tDepartment', models.CharField(default='', max_length=20)),
                ('tGame1', models.CharField(blank=True, default=' ', max_length=40, null=True)),
                ('tGame2', models.CharField(blank=True, default=' ', max_length=40, null=True)),
                ('tGame3', models.CharField(blank=True, default=' ', max_length=40, null=True)),
                ('tGame4', models.CharField(blank=True, default=' ', max_length=40, null=True)),
                ('tGame5', models.CharField(blank=True, default=' ', max_length=40, null=True)),
                ('tGame6', models.CharField(blank=True, default=' ', max_length=40, null=True)),
                ('tGame7', models.CharField(blank=True, default=' ', max_length=40, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
    ]
