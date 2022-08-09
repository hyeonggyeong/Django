from email.policy import default
from itertools import product
from operator import truediv
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
    test_image = models.ImageField(_("image"), upload_to='images')
    
    


#TODO:  Flutter <-> Django Connect (수정 중)
# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token

# class MyUserManager(BaseUserManager):
#     def create_user(self, email, username, first_name, last_name,password=None):
#         if not email:
#             raise ValueError("Users must have an email address.")
#         if not username:
#             raise ValueError("Users must have a username.")
#         if not first_name:
#             raise ValueError("Users must have a first name.")
#         if not last_name:
#             raise ValueError("Users must have a last name.")

#         user = self.model(
#             email=self.normalize_email(email),
#             username=username,
#             first_name=first_name,
#             last_name=last_name
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, username, password, first_name, last_name):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name
#         )
#         user.is_admin = True
#         user.is_staff = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user


# class User(AbstractBaseUser):
#     email = models.EmailField(verbose_name="email", max_length=80, unique=True)
#     first_name = models.CharField(verbose_name="first name", max_length=80)
#     last_name = models.CharField(verbose_name="last name", max_length=80)
#     tap_coins = models.IntegerField(default=0)
#     username = models.CharField(max_length=80, unique=True)
#     date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
#     last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
#     is_admin = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)

#     USERNAME_FIELD = "email"
#     REQUIRED_FIELDS = ["username", "first_name", "last_name"]

#     objects = MyUserManager()

#     def __str__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         return self.is_admin

#     def has_module_perms(self, app_label):
#         return True

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)






#! Dart
# import 'package:TapCoinsApp/api/api.dart';
# import 'package:TapCoinsApp/screens/profile.dart';
# import 'package:flutter/material.dart';
# import 'package:provider/provider.dart';
# import './screens/register.dart';

# void main() {
#   runApp(MyApp());
# }

# class MyApp extends StatelessWidget {
#   // This widget is the root of your application.
#   @override
#   Widget build(BuildContext context) {
#     return MultiProvider(
#       providers: [
#         ChangeNotifierProvider(create: (context) => UserProvider()),
#         // ChangeNotifierProvider(create: (context) => BankProvider())
#       ],
#       child: MaterialApp(
#         title: 'Flutter Demo',
#         theme: ThemeData(
#           primarySwatch: Colors.blue,
#           visualDensity: VisualDensity.adaptivePlatformDensity,
#         ),
#         home: HomePage(),
#       ),
#     );
#   }
# }

# class HomePage extends StatefulWidget {
#   @override
#   _HomePageState createState() => _HomePageState();
# }

# class _HomePageState extends State<HomePage> {
#   @override
#   Widget build(BuildContext context) {
#     final userP = Provider.of<UserProvider>(context);
#     // final bankP = Provider.of<BankProvider>(context);
#     int prizeCoins = 0;
#     int coinsTapped = 0;
#     return MaterialApp(
#       home: SafeArea(
#         child: DefaultTabController(
#           length: 2,
#           child: Scaffold(
#             appBar: TabBar(
#               tabs: [
#                 Tab(icon: new Icon(Icons.home)),
#                 Tab(icon: new Icon(Icons.person_outline_rounded)),
#               ],
#               labelColor: Colors.red,
#               unselectedLabelColor: Colors.yellow,
#               indicatorSize: TabBarIndicatorSize.label,
#               indicatorPadding: EdgeInsets.all(5.0),
#               indicatorColor: Colors.red,
#             ),
#             backgroundColor: Colors.purple,
#             body: Stack(
#               children: <Widget>[
#                 TabBarView(children: [
#                   new Scaffold(
#                     backgroundColor: Colors.purple,
#                     floatingActionButton: FloatingActionButton(
#                       onPressed: () {
#                         Navigator.of(context).push(MaterialPageRoute(
#                             builder: (ctx) => RegisterUser()));
#                       },
#                     ),
#                   ),
#                   ProfilePage(),
#                 ]),
#               ],
#             ),
#           ),
#         ),
#       ),
#     );
#   }
# }