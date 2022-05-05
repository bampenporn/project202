from django.contrib import admin
from django.urls import path
from myapp.views import StudentCreateView
from myapp.views import StudentListView
from myapp.views import StudentDetailView
from myapp.views import StudentUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', StudentCreateView.as_view(),name='student_create'),
    path('student/<int:pk>/', StudentDetailView.as_view(),name='student'),
    path('', StudentListView.as_view(),name='students'),
    path('studentupdate/<int:pk>',StudentUpdateView.as_view(),name='studentupdate'),
]