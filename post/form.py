from django import forms 
from .models import Post, PostAttachments, Comments

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True 

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs) -> None:
        kwargs.setdefault('widget', MultipleFileInput)
        kwargs.setdefault('required', False)
        super().__init__(*args, **kwargs)

    def clean(self, data, initial = None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result
    
class PostForm(forms.ModelForm):
    images = MultipleFileField()
    
    class Meta:
        model = Post 
        fields = ('title_ru', 'title_en', 'content_ru', 'content_en', 'images')

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['images'].widget.attrs['id']="image_select"
        self.fields['images'].widget.attrs['onchange']='show_files(this)'



    
