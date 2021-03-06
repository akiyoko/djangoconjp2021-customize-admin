from django import forms
from django.forms.widgets import MultiWidget, TextInput


class PostalCodeWidget(MultiWidget):
    """郵便番号用ウィジェット"""
    template_name = 'admin/widgets/postal_code.html'

    def __init__(self, attrs=None):
        widgets = [
            TextInput(attrs={'size': '5', 'maxlength': 3}),
            TextInput(attrs={'size': '6', 'maxlength': 4}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        """画面表示用にハイフンで分解する"""
        if value and value.count('-') >= 1:
            return value.split('-')
        return [None, None]

    def value_from_datadict(self, data, files, name):
        """永続化用にハイフンで結合する"""
        values = super().value_from_datadict(data, files, name)
        if any(values):
            return '-'.join(values)
        return None


class PhoneNumberWidget(MultiWidget):
    """電話番号用ウィジェット"""
    template_name = 'admin/widgets/multiwidget_hyphen.html'

    def __init__(self, attrs=None):
        widgets = [
            TextInput(attrs={'size': '6', 'maxlength': 5}),
            TextInput(attrs={'size': '6', 'maxlength': 4}),
            TextInput(attrs={'size': '6', 'maxlength': 4}),
        ]
        super().__init__(widgets, attrs)

    def decompress(self, value):
        """画面表示用にハイフンで分解する"""
        if value and value.count('-') >= 2:
            return value.split('-', 2)
        return [None, None, None]

    def value_from_datadict(self, data, files, name):
        """永続化用にハイフンで結合する"""
        values = super().value_from_datadict(data, files, name)
        if any(values):
            return '-'.join(values)
        return None


class PublisherAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # サブウィジェットのmaxlengthを変更するために親ウィジェットのmaxlengthを削除
        self.fields['postal_code'].widget.attrs.pop('maxlength', None)
        self.fields['phone_number'].widget.attrs.pop('maxlength', None)

    class Meta:
        widgets = {
            'postal_code': PostalCodeWidget(),
            'phone_number': PhoneNumberWidget(),
        }


class BookAdminForm(forms.ModelForm):
    def clean_price(self):
        value = self.cleaned_data.get('price', 0)
        if value > 10000:
            raise forms.ValidationError("価格は1万円を超えないでください。")
        return value
