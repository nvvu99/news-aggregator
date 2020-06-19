from django import forms
from .models import User
from news.models import Category
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import authenticate, forms as auth_forms
from django.db.models import Q


class LoginForm(forms.Form):
    username = forms.CharField(
        label=_('Username'),
    )
    password = forms.CharField(
        label=_("Mật khẩu"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password'}),
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
            self.user_cache = authenticate(
                username=username, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                )

        return self.cleaned_data

    def get_user(self):
        return self.user_cache


class RegisterForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _('Mật khẩu không khớp.'),
    }

    re_password = forms.CharField(
        label='Nhập lại mật khẩu',
        widget=forms.PasswordInput,
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
                code='password_mismatch'
            )

        return re_password

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class SetPasswordForm(auth_forms.SetPasswordForm):
    error_messages = {
        'password_mismatch': _('Mật khẩu không khớp.'),
    }
    new_password1 = forms.CharField(
        label=_("Mật khẩu"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
        strip=False,
    )
    new_password2 = forms.CharField(
        label=_("Nhập lại mật khẩu"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )


class PasswordChangeForm(SetPasswordForm):
    error_messages = {
        **SetPasswordForm.error_messages,
        'password_incorrect': _("Mật khẩu cũ bạn vừa nhập không đúng."),
    }

    old_password = forms.CharField(
        label=_("Mật khẩu cũ"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True}),
    )

    field_order = ['old_password', 'new_password1', 'new_password2']

    def get_initial_for_field(self, field, field_name):
        return ''

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return old_password

    def clean(self):
        new_password = self.cleaned_data.get('new_password1')
        self.user.set_password(new_password)
        self.user.save()
        return self.cleaned_data


class TopicOrganizeForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.following_categories = user.following_categories.all()
        self.fields['following_categories'].queryset = self.following_categories

    class Meta:
        model = User
        fields = ('following_categories', )
        widgets = {
            'following_categories': forms.CheckboxSelectMultiple(),
        }


class TopicAddForm(TopicOrganizeForm):
    adding_categories = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, user, *args, **kwargs):
        super().__init__(user, *args, **kwargs)
        following_query = Q()

        for category in self.following_categories:
            following_query |= Q(pk=category.pk)

        self.fields['adding_categories'].queryset = Category.objects.exclude(following_query)

    def clean(self):
        cleaned_data = self.cleaned_data
        cleaned_data['following_categories'] = self.following_categories.union(cleaned_data.get('adding_categories'))
        return cleaned_data

    class Meta(TopicOrganizeForm.Meta):
        fields = ('following_categories', 'adding_categories', )
        widgets = {
            'adding_categories': forms.CheckboxSelectMultiple()
        }


class UserUpdateForm(forms.ModelForm):
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
