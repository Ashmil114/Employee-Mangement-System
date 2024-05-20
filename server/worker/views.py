from django.shortcuts import render
from rest_framework.authtoken.models import Token
from .models import Worker
from rest_framework.response import Response


def GetUser(token):
    try:
        user_token = Token.objects.get(key=token)
    except Exception as e:
        return Response({'error':str(e)})
    try:
        try:
            user = Worker.objects.get(phone=user_token.user)
            return user
        except:
            return True
    except Exception as e:
        return Response({'error':str(e)})
