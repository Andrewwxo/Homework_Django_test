from django.views.generic import CreateView


from shopauth.forms import ShopUserCreateForm
from shopauth.models import ShopUser


class ShopUserCreateView(CreateView):
    model = ShopUser
    success_url = '/'
    form_class = ShopUserCreateForm
    # fields = ('username', 'password1', 'password2')