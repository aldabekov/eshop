from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Category, Item
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.
class HomeView(TemplateView):
    template_name = 'eshop/index.html'
    model = Category
    alias = 'slug'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(*kwargs)
        context['category'] = Category.objects.all()
        return context

class CategoryView(DetailView):
    template_name = 'single.html'
    model = Category
    alias = 'slug'

class SingleGoodView(DetailView):
    template_name = 'eshop/index.html'
    model = Item
    alias = 'slug'

    def get_context_data(self, **kwargs):
        context = super(SingleGoodView, self).get_context_data(*kwargs)
        context['good'] = Item.objects.all()
        return context

def red(request):
    pa = Item.objects.all()
    return render(request, 'eshop/index.html', {'tort': pa})

def goods(request):
    tovars = Item.objects.all()
    context = {
        'tovars': tovars
    }
    return HttpResponse(render_to_string('eshop/index.html'), context)

# class SingleGoodView(DetailView):
#     template_name = 'single-good.html'
#     model = Item
#     slug_field = 'pk'
#
#     def get_context_data(self, **kwargs):
#         context = super(SingleGoodView, self).get_context_data(**kwargs)
#         context['sizes'] = ItemModel.objects.all()
#         return context
