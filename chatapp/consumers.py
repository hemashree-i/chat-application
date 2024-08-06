# chat/consumers.py
import json
from . models import *
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["roomname"] # this room name and routing name should be same
        self.room_group_name = f"chat_{self.room_name}"
        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, 
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        print("Receive message from WebSocket")
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        roomname=text_data_json["roomName"]
        username=text_data_json["username"]
        self.save(message,roomname,username)
        # Send message to room group
        print(self.channel_layer.group_send)
        print(self.room_name)
        print(self.room_group_name)
        print("***")
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                "type": "chating.message_room",  #this is the method it call next
                "message": message,
                "room_name":roomname,
                "username":username,
                "group_msg":'group msg'
            }
        )  
        # after receiving the msg we chat_message
        self.send(text_data=json.dumps({"message": "message"}))  #this message is shared to chatSocket.onmessage on html page


    # Receive message from room group
    def chating_message_room(self, event):
        print("Receive message from room group")
        print(event)
        message = event["message"]
        username=event["username"]
        myname='hema'
        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message,"username":username ,"myname":myname}))  #this message is shared to chatSocket.onmessage on html page


    def save(self,message,roomname,username):
        chat_msg.objects.filter(rname=Room.objects.get(Room_name=roomname)).create(
            chat=message,
            room_chat=roomname,
            user_name=username
        )
        






