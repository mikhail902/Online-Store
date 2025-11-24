from django import forms

from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите название'
        })
        self.fields['pic'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете фото'
        })
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Напишите описание'
        })
        self.fields['category'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Выберете категорию'
        })
        self.fields['price'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите цену'
        })
        self.fields['created_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату создания'
        })
        self.fields['updated_at'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Введите дату последнего изменения'
        })
