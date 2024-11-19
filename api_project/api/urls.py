from django.contrib import admin
from django.urls import path, include  # Ensure `include` is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Ensure this line includes `api.urls`
]
