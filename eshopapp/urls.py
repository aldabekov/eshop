from django.conf.urls import patterns, url
from .views import *
from eshopapp import views


urlpatterns = patterns('',
    url(r'^index/$', HomeView.as_view(), name='home'),
    url(r'^categories/$', CategoryView.as_view(), name='categories'),
    url(r'^singlegood/$', SingleGoodView.as_view(), name='all_categories_goods'),
    url(r'^singlegoods/$', views.red, name='red'),
)


# {% url 'categories' category.slug %}