from django.db import models

# Create your models here.

class signin(models.Model):
    username=models.CharField(max_length=100 , primary_key=True)
    password=models.CharField(max_length=100)
    # usercode=models.IntegerField(max_length=100)
    

class Room(models.Model):
    Room_name=models.CharField(max_length=100 , primary_key=True)

class chat_msg(models.Model):
    chat=models.CharField(max_length=100)
    room_chat=models.CharField(max_length=100)
    user_name=models.CharField(max_length=100)
    rname=models.ForeignKey('Room', models.DO_NOTHING, db_column='Room_name' ,blank=True, null=True)
    username=models.ForeignKey('signin', models.DO_NOTHING, db_column='username' ,blank=True, null=True)

    

# class chatroom(models.Model):
#     chat=models.CharField(max_length=100)
#     room_chat=models.CharField(max_length=100)
#     username=models.CharField(max_length=100)
#     rname=models.ForeignKey('Room', models.DO_NOTHING, db_column='Room_name' ,blank=True, null=True)
#     username=models.ForeignKey('signin', models.DO_NOTHING, db_column='username' ,blank=True, null=True)



