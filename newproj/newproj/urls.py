"""newproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from login import views
from .router import router

urlpatterns = [

    path('admin/', admin.site.urls),

    # registration with verification
    path('register/', views.showTemp.as_view(), name='hell'),  # pass email and password
    path('verify/', views.VerifyView.as_view(), name='hello'),  # API called for verification of mail

    # login
    path('auth/', views.authenticate_user),  # new token
    path('auth_refresh/', views.refresh_token),  # Refresh token

    # forgot password
    path('for_pass/', views.forgot_password),  # enter email so that a verification mail can be sent
    path('auth_for_pass/', views.auth_for_pass.as_view()),  # auth the user
    path('enter_pass/', views.enter_pass.as_view()),  # enter password to update it

    path('user_old/', views.UserList.as_view()),
    # path('user_old/(?P<fname>\w+)', views.UserList.as_view()),
    path('user/', include(router.urls), name='accounts'),
    path('add_account/', views.AccountList.as_view()),
    path('login/', views.login_page.as_view()),
    path('sendmail/', views.sending_mail),

    # path('product/$', views.getotp)

]
