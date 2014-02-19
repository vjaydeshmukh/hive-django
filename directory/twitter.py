import re
from django.db import models
from django.core.exceptions import ValidationError

MAX_TWITTER_NAME_LEN = 15

def validate_twitter_name(value):
    base_err = '"%s" is not a valid Twitter username.' % value
    if len(value) > MAX_TWITTER_NAME_LEN:
        raise ValidationError(base_err + ' A username cannot be longer than '
                              '%d characters.' % MAX_TWITTER_NAME_LEN)
    if not re.match('^[A-Za-z_]+$', value):
        raise ValidationError(
            base_err +
            ' A username can only contain alphanumeric characters (letters '
            'A-Z, numbers 0-9) with the exception of underscores.'
        )

class TwitterNameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(TwitterNameField, self).__init__(
            max_length=MAX_TWITTER_NAME_LEN,
            validators=[validate_twitter_name],
            *args,
            **kwargs
        )
