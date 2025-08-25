from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # static HTML served
    path('api/', include('restaurant.urls')),
    path('api/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]