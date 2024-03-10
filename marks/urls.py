from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
     path('',login1, name='login1'),
     path('data',data,name='data'),
     path('enter',enter,name='enter'),
     path('new',new,name='new'),
     path('newsubmition',newsubmition,name='newsubmition'),
     path('logout',logout,name='logout'),
     path('accounts/login/',logins,name='login'),
     path('reset_password',auth_views.PasswordResetView.as_view(),name="reset_password"),
     path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
     path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
     path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
     #path('submit',submit,name='submit'),
]