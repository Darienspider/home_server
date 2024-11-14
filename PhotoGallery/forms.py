from django import forms
from .models import Tags, Person

class uploadForm(forms.Form):
    title = forms.TextInput()
    description = forms.TextInput()
    imageFile = forms.ImageField(required=True)
    tags = forms.ModelChoiceField(queryset=Tags.objects.all(), required=False, empty_label="Select a tag")
    new_tag = forms.CharField(widget=forms.TextInput(), required=False, help_text="Or create a new tag")
    location = forms.TextInput()
    associated_person = forms.ModelMultipleChoiceField(
        queryset= Person.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )
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

