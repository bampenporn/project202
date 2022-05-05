from django.shortcuts import render
from myapp.models import Student
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.urls import reverse_lazy

class StudentCreateView(CreateView):
    model = Student
    template_name = 'student_create.html'
    fields = ['name','nick_name','email','phone_number']
    def get_success_url(self):
        return reverse('students')
        # kwargs={'pk': self.object.pk}

class StudentDetailView(DetailView):
    model = Student
    context_object_name = 'student'
    template_name = 'student.html'

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'
    paginate_by = 5
    #queryset=Student.objects.filter(type='mountain')
    template_name = 'student_list.html'
    
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name','nick_name','email','phone_number']
    template_name = 'student_create.html'
    success_url = reverse_lazy('students')
    