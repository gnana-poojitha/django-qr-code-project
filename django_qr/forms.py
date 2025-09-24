from django import forms

class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(
        max_length=50,
        label='Restaurant Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder':'Enter Restaurant Name'
        })
    )
    url = forms.URLField(
        max_length=200,
        label='Menu URL',
        widget=forms.URLInput(attrs={
            'class':'form-control',
            'placeholder':'Enter the URL of your online menu'
        })
    )
    fg_color = forms.CharField(
        max_length=7,
        label='Foreground Color',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control', 'value': '#000000'})
    )
    bg_color = forms.CharField(
        max_length=7,
        label='Background Color',
        widget=forms.TextInput(attrs={'type': 'color', 'class': 'form-control', 'value': '#ffffff'})
    )
    logo = forms.ImageField(
        label='Upload Logo (optional)',
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
