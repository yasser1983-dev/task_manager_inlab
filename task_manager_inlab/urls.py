from django.contrib import admin
from django.urls import path, include

from accounts.views import RegisterView, CustomLogoutView, CustomLoginView
from dashboard.views import dashboard
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', dashboard, name='dashboard'),
    path('projects/', include('projects.urls')),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
]