
from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect
from django.views.static import serve
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', lambda request: redirect('news/', permanent=False)),
  path('news/', include('main_app.urls')),
  path('sign/', include('sign.urls')),
  path('account/', include('allauth.urls')),
]



