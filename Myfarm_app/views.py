from cgitb import html
from dataclasses import field, fields
from typing import Text
from venv import create
from rest_framework.response import Response
from django.shortcuts import render, redirect
from .forms import  FileUploadForm2, ImageUploadForm
from .models import  FileUpload2, ImageModel,Person
from .serializers import PersonSerializer

import io
from PIL import Image as im
import torch

from django.views.generic.edit import CreateView
from rest_framework import viewsets



# Create your views here.

def index(request):
    return render(request, 'Myfarm_app/main.html')

#이미지 업로더
def fileUpload2(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        img = request.FILES["imgfile"]
        fileupload2 = FileUpload2(
            title=title,
            content=content,
            imgfile=img,
        )
        
        fileupload2.save() 
        return render(request, 'Myfarm_app/success.html')
    
    else:
        fileuploadForm2 = FileUploadForm2
        context = {
            'fileuploadForm2': fileuploadForm2,
        }
        return render(request, 'Myfarm_app/fileupload.html', context)
#yolo test _20220810
def yolodetect(request):
    if request.method == 'POST':
        img = request.FILES["image"]
        print("[1]",img)
        img_instance= Person(
            image=img,
        )   
        img_instance.save()
        print("[2]",img)
        print("[3]",img_instance)
        
        uploaded_img_qs = Person.objects.filter().last()
        print("[4]")
        img_bytes = uploaded_img_qs.image.read()
        print("[5]")
        img = im.open(io.BytesIO(img_bytes))
        print("[6]")
        
        # uploaded_img_qs = ImageModel.objects.filter().last()
        # img_bytes = uploaded_img_qs.image.read()
        # img = im.open(io.BytesIO(img_bytes))
        
        path_hubconfig = "yolov5_code"
        path_weightfile = "yolov5_code/weight/pepper/best.pt"  # 커스텀 모델
        model = torch.hub.load(path_hubconfig, 'custom',path=path_weightfile, source='local')

        results = model(img, size=640)
        print('result',results)
        results.render()
        for img in results.imgs:
            img_base64 = im.fromarray(img)
            img_base64.save("media/yolo_out/image1.jpg", format="JPEG")
            
        return render(request, 'Myfarm_app/success.html')
        
    
    else:
        return print('실패')


# AI모델 적용 전용

class UploadImage(CreateView):
    model = ImageModel
    template_name = 'Myfarm_app/imagemodel_form.html'
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)

        if form.is_valid():
            img = request.FILES.get('image')
            img_instance = ImageModel(
                image=img
            )
            img_instance.save()
            print("[1]" , request)
            
            print("[2]" , request.POST)
            print("[3]" , request.FILES)
            print("[3.5]",img)
            print("[3.6]",img_instance)
            print("[4]" , type(request.POST))
            print("[5]" , type(request.FILES))
            
            uploaded_img_qs = ImageModel.objects.filter().last()
            img_bytes = uploaded_img_qs.image.read()
            img = im.open(io.BytesIO(img_bytes))
            print("[6]" , ImageModel.objects)
            print("[7]" , uploaded_img_qs)
            # Change this to the correct path
            path_hubconfig = "yolov5_code"
            path_weightfile = "yolov5_code/weight/pepper/best.pt"  # 커스텀 모델

            model = torch.hub.load(path_hubconfig, 'custom',path=path_weightfile, source='local')

            results = model(img, size=640)
            results.render()
            for img in results.imgs:
                img_base64 = im.fromarray(img)
                img_base64.save("media/yolo_out/image0.jpg", format="JPEG")

            inference_img = "/media/yolo_out/image0.jpg"

            form = ImageUploadForm()
            context = {
                "form": form,
                "inference_img": inference_img
            }
            return render(request, 'Myfarm_app/imagemodel_form.html', context)

        else:
            form = ImageUploadForm()
        context = {
            "form": form
        }
        return render(request, 'Myfarm_app/imagemodel_form.html', context)
    
    

#테스트용  #todo 받은 이미지로 ai모델
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer




# 원하는 IP와 포트로 서버 열기
# TODO : python manage.py runserver 192.168.0.76:8080
#! Flutter <-> Django Connect (수정 중)
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .serializers import RegistrationSerializer
# from rest_framework.authtoken.models import Token

# @api_view(['POST'])
# @permission_classes([AllowAny])
# def registration_view(request):
#     print("got here first")

#     if request.method == 'POST':
#         print("got here")
#         serializer = RegistrationSerializer(data=request.data)
#         data = {}
#         if serializer.is_valid():
#             print("got valid")
#             user = serializer.save()
#             data['response'] = "succesfully registered a new user."
#             data['email'] = user.email
#             data['username'] = user.username
#             token = Token.objects.get(user=user).key
#             data['token'] = token
#         else:
#             data = serializer.errors
#         return Response(data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def logout_view(request):
#     cToken = Token.objects.get(user=request.user)
#     cToken.delete()


