# import re
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _


class UsernameValidator(UnicodeUsernameValidator):
    regex = r'^[\w.]+\Z'
    message = _(
        'Username chỉ bao gồm chữ cái, số, '
        'và ký tự chấm(.).'
    )