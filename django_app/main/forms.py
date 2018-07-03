from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]


class MyCustomSignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
        ]

    def save(self):
        # user = super(MyCustomSignupForm, self).save()
        # return user
        print(self.request.user)
        print('Signup Form.')
