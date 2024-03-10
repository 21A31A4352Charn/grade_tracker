from django import forms


class SubscribeForm(forms.Form):
    email = forms.EmailField()

    def __str__ (self):
        return self.email