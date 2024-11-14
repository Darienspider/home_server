from django import forms
from .models import Tags
from django.forms.widgets import Widget

class JournalEntry(forms.Form):
    title = forms.TextInput()
    content  = forms.Textarea()
    tags = forms.ModelMultipleChoiceField(
        queryset=Tags.objects.all(),
        widget=forms.CheckboxSelectMultiple(),
    )
    new_tag = forms.CharField(widget=forms.TextInput(), required=False, help_text="Or create a new tag")
    location = forms.TextInput()
    category = forms.TextInput()
    def save(self):
            # Retrieve form data
            data = self.cleaned_data
            
            # Check if a new tag is provided
            if data['new_tag']:
                # Create and save the new tag
                new_tag = Tags.objects.create(name=data['new_tag'])
                # Set the new tag to the 'tags' field for later use
                data['tags'] = new_tag
