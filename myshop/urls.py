import django.urls
from django.views.generic import TemplateView

import myshop.views as myshop
app_name = 'myshop'

urlpatterns = [
    django.urls.path('', myshop.index, name='index'),
    django.urls.path('products/', myshop.product_list, name='product_list'),
    # django.urls.path('products/',
    #                  myshop.ProductsListView.as_view(),
    #                  name='product_list'),
    django.urls.path('products/create/',
                     myshop.ProductKindCreateView.as_view(),
                     name='product_create'),
    django.urls.path('about/', TemplateView.as_view(template_name='myshop/about.html'), name='about'),

]
