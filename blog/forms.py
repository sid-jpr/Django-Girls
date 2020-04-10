from django import forms

from .models import Post

# PostForm is the name of the form
class PostForm(forms.ModelForm):

    class Meta:
        # we tell Django which model should be used to create this form
        model = Post
        # specify field(s) should end up in our form
        fields = ('title', 'text',) 
