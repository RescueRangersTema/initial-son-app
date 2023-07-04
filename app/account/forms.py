from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


class UserLoginForm(forms.Form):
    email = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)


class UserCreationForm(forms.ModelForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = (
            'name',
            'email',
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError('Passwords don\'t match')
        return password2

    def save(self, commit=True):

        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])

        if commit:
            user.save()

        return user
