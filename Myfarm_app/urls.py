from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path("", views.UploadImage.as_view(), name="upload_image_url"),
    # path("test/", views.UploadImage2.as_view(), name="upload_image_url"),

]