
from django.db import models
from django.utils.translation import gettext_lazy as _
import os


#테스트용
class ImageDetect(models.Model):
    name= models.TextField(max_length=40, null=True)
    image_file = models.ImageField(null=True, upload_to="", blank=True)

    def __str__(self):
        return self.title
    
# 이미지 업로드 모델   
class FileUpload2(models.Model):
    title = models.TextField(max_length=40, null=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
# AI모델 연동 전용 
class ImageModel(models.Model):
    image = models.ImageField(_("image"), upload_to='images')

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"

    def __str__(self):
        return str(os.path.split(self.image.path)[-1])
    

# 이미지 집어넣기
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField(_("image"), upload_to='images')
    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
    
    def __str__(self):
        return str(os.path.split(self.image.path)[-1])
    
    


