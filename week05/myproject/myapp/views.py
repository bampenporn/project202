from django.shortcuts import render
from myapp.models import Image, Board, Pin
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse


class ImageCreateView(CreateView):
    model = Image
    template_name = 'image_create.html'
    fields = ['image']
    def get_success_url(self):
        return reverse('home')

class ImageListView(ListView):
    model = Image
    #queryset=Student.objects.filter(type='mountain')
    template_name = 'image_list.html'


class ImageDetailView(DetailView):
    model = Image
    template_name = 'image.html'
    context_object_name = 'image'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_gallery'] = Image.objects.all().filter(pk=self.object.pk)
        return context