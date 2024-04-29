from django.forms import ModelForm, TextInput, CharField, ModelChoiceField, ModelMultipleChoiceField, \
    CheckboxSelectMultiple, SelectMultiple
from .models import Quote, Author, Tag


class QuoteForm(ModelForm):
    quote = CharField(max_length=250, required=True, widget=TextInput(attrs={"class": "form-control", "id": "exampleInputText1"}))
    author = ModelChoiceField(queryset=Author.objects.all(), empty_label="choose author...")
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=SelectMultiple)

    class Meta:
        model = Quote
        fields = ['quote', "author", "tags"]
