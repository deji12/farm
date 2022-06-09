from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.core.mail import EmailMessage
from  django.conf import settings
from django.contrib import messages
from .models import post, comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    notes = post.objects.all()
    serializer = PostSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def post_detail(request, name):
    get_post = post.objects.get(title=name)
    serializer = PostSerializer(get_post)
    return Response(serializer.data)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        msg = request.POST['message']
        phone = request.POST['phone']

        email = EmailMessage(
            f'KingsVine Yard Farms: {subject}',
            f'Name: {name} \n \n Message: {msg} \n \n Phone: {phone} \n \n Email: {email}',
            settings.EMAIL_HOST_USER,
            ['adesolaayodeji18@gmail.com']
                )
        email.fail_silently = True
        email.send()
        return HttpResponse('Your message has been received')
    return HttpResponse('')
    