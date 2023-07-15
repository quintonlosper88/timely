from django.forms import ModelForm
from .models import WarehouseModel
class ToolForm(ModelForm):
    print("Warehouse Form model called")
    class Meta:
        model = WarehouseModel
        fields = '__all__'  # Use this to include all fields or manually list them
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['item_photo'].widget.attrs.update({'class': 'form-control-file'})