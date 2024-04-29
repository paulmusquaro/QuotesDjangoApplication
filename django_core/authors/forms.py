from django.forms import ModelForm, CharField, TextInput, Textarea, DateField, DateInput, DateInput
from quotes.models import Author # noqa


class AuthorForm(ModelForm):
    fullname = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "exampleInputText1"}))
    born_date = CharField(max_length=50, widget=TextInput(attrs={"class": "form-control", "id": "exampleInputText2"}))
    born_location = CharField(max_length=100,
                              widget=TextInput(attrs={"class": "form-control", "id": "exampleInputText3"}))
    description = CharField(max_length=500,
                            widget=Textarea(attrs={"class": "form-control", "id": "exampleFormControlTextarea1"}))

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']

