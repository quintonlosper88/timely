from django.forms import ModelForm
from .models import UserModel
class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'  # Use this to include all fields or manually list them
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['profileImage'].widget.attrs.update({'class': 'form-control-file'})