from django import forms


class tweetForm(forms.Form):
    user_name = forms.CharField(label="Get Tweets of ", max_length=100)
    file_type = forms.ChoiceField(choices=[("CSV", "CSV"), ("XLS", "XLS")])
