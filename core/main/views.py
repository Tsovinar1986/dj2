from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Shoes, Brand
# Create your views here.


class CategoryListView(ListView):
    template_name = 'home.html'

    def get(self, request):
        categorys = Category.objects.all()
        return render(request, self.template_name, {'categorys':categorys})

class CategoryDetailView(DetailView):
    template_name = 'home_detail.html'

    def get(self, request, category_id):
        shoes = Shoes.objects.get(pk=category_id)
        return render(request, self.template_name, {'shoes':shoes})