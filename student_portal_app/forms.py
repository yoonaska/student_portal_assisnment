from django import forms


class studentDetailsForm (forms.Form):
      firstName = forms.CharField(max_length=200)
      lastName = forms.CharField(max_length=200)
      phonenumber = forms.CharField(max_length=200)
      email = forms.EmailField(max_length = 254)
      addressOne = forms.CharField(max_length=500, label='Address 1')
      addressTwo = forms.CharField(max_length=500, label='Address 2')
      password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))