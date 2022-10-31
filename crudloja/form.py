from django.forms import ModelForm
from crudloja.models import Produto

# Create the form class.
class ProdutoForm(ModelForm):
     class Meta:
         model = Produto
         fields = ['name', 'price', 'quantityStock']