from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('login/',views.user_login,name="userlogin"),
    path('signup/',views.signup,name="usersignup"),
    path('logout/',views.user_logout,name="userlogout"),
    path('addcar/',views.Addcar,name="addcar"),
    path('contact/', views.contact, name="contact"),
    path('about/', views.about, name="about"),

]