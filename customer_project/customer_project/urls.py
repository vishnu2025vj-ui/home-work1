from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customers.urls')),
    path('', lambda request: redirect('add_customer')),  # 👈 redirect root to add_customer
]
