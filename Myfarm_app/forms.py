from django.forms import ModelForm
from .models import FileUpload2, ImageModel

        
        
class FileUploadForm2(ModelForm):
    class Meta:
        model = FileUpload2
        fields = ['title', 'imgfile', 'content']
        
        
#AI
class ImageUploadForm(ModelForm):
    class Meta:
        model = ImageModel
        fields = ['image']
