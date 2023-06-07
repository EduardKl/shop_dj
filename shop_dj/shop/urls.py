from django.urls import path, re_path

from .views import *


app_name = 'shop'

urlpatterns = [
    path('', product_list, name='home'),
    path(r'^(?P<category_slug>[-\w]+)/$', product_list, name='product_list_by_category'),
    path('product_detail/<int:id>/<slug:slug>', product_detail, name='product_detail'),  # r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$'
]
