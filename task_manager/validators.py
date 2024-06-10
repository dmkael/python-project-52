from django.contrib.auth.password_validation import MinimumLengthValidator


class MyMinimumLengthValidator(MinimumLengthValidator):

    def __init__(self, min_length=3):
        super().__init__(min_length)
