
from django.contrib import admin
from rest_framework import routers
from django.urls import path, include,re_path
from django.conf import settings 
from django.conf.urls.static import static 
import Myfarm_app.views

router = routers.DefaultRouter()
router.register(r'persons', Myfarm_app.views.PersonViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',Myfarm_app.views.index, name='index'),
    path('fileupload2/', Myfarm_app.views.fileUpload2, name="fileupload2"),
    path('yolo/', include("Myfarm_app.urls")),#app폴더 내 urls.py에 명시했을 때, 이렇게 사용
    re_path(r'^', include(router.urls)),
    re_path(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    path('def/',Myfarm_app.views.yolodetect, name='yolodetect'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 



