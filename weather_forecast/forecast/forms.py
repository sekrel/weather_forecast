from django import forms


class AddPostForm(forms.Form):
    city = forms.CharField(label='Город', max_length=255, widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
