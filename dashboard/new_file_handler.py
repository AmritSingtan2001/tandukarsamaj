from django.core.exceptions import ValidationError
import os

def handle_uploaded_file(f):
    with open('media/homestayimages' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def validate_file(value):
    value= str(value)
    if value.endswith(".jpg") != True and value.endswith(".jpeg") != True and value.endswith(".png") != True and  value.endswith(".pdf") != True and value.endswith(".gif ") != True: 
        return False
    else:
        return True