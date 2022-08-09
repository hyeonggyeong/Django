
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

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 



#TODO: Flutter <-> Django Connect (수정 중)
# from django.urls import path
# from .views import registration_view, logout_view
# from rest_framework.authtoken.views import obtain_auth_token
# # from rest_framework.permissions import IsAuthenticated


# app_name = "backApp"

# urlpatterns = [
#     path('register', registration_view, name="register"),
#     path('login', obtain_auth_token, name="login"),
#     path('logout', logout_view, name="logout")
# ]


#setting.py에 접근가능한 ip지정 ['*'] 해놓으면 모든 사용자가 url접속 가능
# ALLOWED_HOSTS = ['***.***.***.***', 'localhost', '127.0.0.1']