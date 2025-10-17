from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/students/')),
    path('students/', views.student_list, name='student_list'),
]
