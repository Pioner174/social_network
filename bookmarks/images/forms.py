from django import forms
from .models import Image


class ImageCreateForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image', 'description', 'shooting', 'private')
        widgets = {'private': forms.CheckboxInput,
                   'shooting': forms.DateInput}


class SearchForm(forms.Form):
    query = forms.CharField(label='Поиск по заголовку, описанию и дате съемки')

