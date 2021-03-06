"""timebox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from core import views
from rest_framework import routers
from api import views as api_views
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import(
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


class MyRegistrationView(RegistrationView):
    success_url = 'registration'


# Router for api url's
router = routers.DefaultRouter()
router.register('users', api_views.UserViewSet)
router.register('lists', api_views.ListViewSet)
router.register('tasks', api_views.TaskViewSet)


urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/password/reset/', PasswordResetView.as_view(), {'template_name': 'registration/password_reset_form.html'}, name="password_reset"),
    path('accounts/password/reset/done/', PasswordResetDoneView.as_view(), {'template_name': 'registration/password_reset_done.html'}, name="password_reset_done"),
    path('accounts/password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), {'template_name': 'registration/password_reset_confirm.html'}, name="password_reset_confirm"),
    path('accounts/password/done/', PasswordResetCompleteView.as_view(),
        {'template_name': 'registration/password_reset_complete.html'},
        name="password_reset_complete"),
    path('accounts/registration/', MyRegistrationView.as_view(), name='registration_register'),
    path('api/', include((router.urls, 'core'), namespace='api')),
    path('accounts/', include('registration.backends.simple.urls')),

]
