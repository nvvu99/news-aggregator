from django import forms
from .models import User
from news.models import Category
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import authenticate
from django.db.models import Q


class ResetPasswordForm(forms.Form):
    email = forms.EmailField(
        label = _('Email')
    )


class SigninForm(forms.Form):
    username = forms.CharField(
        label = _('Username'),
    )
    password = forms.CharField(
        label = _("Mật khẩu"),
        strip = False,
        widget = forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
    )

    error_messages = {
        'invalid_login': _("Username hoặc mật khẩu không đúng."),
    }

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        return super().__init__(*args, **kwargs)

    def get_initial_for_field(self, field, field_name):
            return ''

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username is not None and password is not None:
            self.user_cache = authenticate(username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code = 'invalid_login',
                    )

        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class SignupForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('Mật khẩu không khớp.'),
    }

    re_password = forms.CharField(
        label = 'Nhập lại mật khẩu', 
        widget = forms.PasswordInput,
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)
        labels = {
            'email': 'Email',
            'password': 'Mật khẩu',
            'first_name': 'Tên',
            'last_name': 'Họ',
        }

    def get_initial_for_field(self, field, field_name):
        return ''

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password and re_password and password != re_password:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code = 'password_mismatch'
            )

        return re_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class ChangePasswordForm(forms.Form):
    error_messages = {
        'password_incorrect': _("Mật khẩu cũ bạn vừa nhập không đúng."),
        'password_mismatch': _('Mật khẩu không khớp.'),
    }

    old_password = forms.CharField(
        label = _("Mật khẩu cũ"),
        strip = False,
        widget = forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )
    new_password1 = forms.CharField(
        label = _("Mật khẩu mới"),
        widget = forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip = False,
    )
    new_password2 = forms.CharField(
        label = _("Nhập lại mật khẩu mới"),
        strip = False,
        widget = forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def get_initial_for_field(self, field, field_name):
        return ''

    def clean_new_password2(self):
        new_password1 = self.cleaned_data.get('new_password1')
        new_password2 = self.cleaned_data.get('new_password2')

        if new_password1 != new_password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code = 'password_mismatch',
            )
        return new_password2

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code = 'password_incorrect',
            )
        return old_password

    def clean(self):
        new_password = self.cleaned_data.get('new_password1')
        self.user.set_password(new_password)
        self.user.save()
        return self.cleaned_data


class OrganizeTopicForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.following = user.following.all()
        self.fields['following'].queryset = self.following

    class Meta:
        model = User
        fields = ('following', )
        widgets = {
            'following': forms.CheckboxSelectMultiple(),
        }


class AddTopicForm(OrganizeTopicForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        following_query = Q()

        for category in self.following:
            following_query |= Q(pk=category.pk)

        self.fields['following'].queryset = Category.objects.exclude(following_query)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data['following'] = cleaned_data.get('following').union(self.following)
        return cleaned_data


class UpdateUserInfoForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        return super().__init__(*args, **kwargs)

    
    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'avatar')
        labels = {
            'last_name': 'Họ',
            'first_name': 'Tên',
            'avatar': 'Avatar',
        }