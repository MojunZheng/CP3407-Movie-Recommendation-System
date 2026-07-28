from django import forms

from movie.models import User, Movie_rating


# Registration Form
class RegisterForm(forms.ModelForm):
    password_repeat = forms.CharField(max_length=256)

    def get_errors(self):
        errors = self.errors.get_json_data()
        errors_lst = []
        for messages in errors.values():
            for message_dict in messages:
                for key, message in message_dict.items():
                    if key == 'message':
                        errors_lst.append(message)
        return errors_lst

    # Final Validation After Standard Validation
    # Validate Password
    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        pwd = cleaned_data.get('password')
        password_repeat = cleaned_data.get('password_repeat')
        if pwd != password_repeat:
            raise forms.ValidationError(message='Passwords do not match!')
        return cleaned_data

    class Meta:
        model = User
        fields = ['name', 'password', 'email']


# Login Form
class LoginForm(forms.ModelForm):
    name = forms.CharField(max_length=128)
    remember = forms.IntegerField(required=False)

    class Meta:
        model = User
        fields = ['password']

    def get_errors(self):
        errors = self.errors.get_json_data()
        errors_lst = []
        for messages in errors.values():
            for message_dict in messages:
                for key, message in message_dict.items():
                    if key == 'message':
                        errors_lst.append(message)
        return errors_lst


# After Form Validation Passes, Check Whether the Score Is 0
class CommentForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        score = cleaned_data.get('score')
        if score == 0:
            raise forms.ValidationError(message='Rating cannot be empty!')
        else:
            return cleaned_data

    class Meta:
        # Movie Rating: Record Only the Rating and Review
        model = Movie_rating
        fields = ['score', 'comment']
