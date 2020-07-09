
from django.core.exceptions import ValidationError

from django.utils.translation import gettext_lazy as _

def subjects_taught_validator(value):
    if len(value.split(','))>5:
        raise ValidationError(
            _('subjects taught can not be more than five. '),
            params={'value': value},
        )
