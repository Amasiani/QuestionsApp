from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
)

User = get_user_model()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('User does not exit')
            if not user.check_password(password):
                raise forms.ValidationError('incorrect password')
            if not user.is_active:
                raise forms.ValidationError('user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="email address")
    email2 = forms.EmailField(label="confirm email")
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]

    def clean(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email != email2:
            raise forms.ValidationError('emails must match')
            email_qs = User.objects.filter(email=email)
            if email_qs.exists():
                raise forms.ValidationError('email already exist')
            return email


class AccountUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'email',
            'username'
        )

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
        raise forms.ValidationError('Email "%s" is already in use.' % email)


    def clean_username(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
        raise forms.ValidationError('Username "%s" is already in use.' % username)
