from django import forms

# TODO: na przyszłość: możnaby dodać select z wytrenowanymi modelami, i wyświetlać wynik dla danego tekstu i danego modelu
class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={'placeholder':\
                                     "Type in your doctor's note here!"}),label=False)