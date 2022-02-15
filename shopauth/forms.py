from django.contrib.auth.forms import UserCreationForm

from shopauth.models import ShopUser


class ShopUserCreateForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field_obj in self.fields.items():
            field_obj.help_text = ''
            # field_obj.widget.attrs['class'] = 'form-control'
            # print(field_name, field_obj.help_text)