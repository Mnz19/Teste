from django.views.generic import ListView, CreateView
from .models import Product
from django.urls import reverse_lazy
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "produtos"
    paginate_by = 10

class ProductCreateView(CreateView):
    model = Product
    template_name = "product_form.html"
    form_class = ProductForm
    success_url = reverse_lazy('product_list')