from django import forms


class tweetForm(forms.Form):
    user_name = forms.CharField(label="Get Tweets of ", max_length=100, widget=forms.TextInput(
        attrs={"placeholder": "@username", "id": "textbox"}))
    file_type = forms.ChoiceField(label="File Type ", choices=[
                                  ("CSV", "CSV"), ("XLS", "XLS")])
