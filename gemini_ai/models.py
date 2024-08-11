from django.db import models


class ImageUploaded(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"


class RecognizedItem(models.Model):
    images = models.ManyToManyField(ImageUploaded, related_name='recognized_items')
    ai_json_response = models.JSONField()  # Store additional data about the item
    recyclable_items=models.TextField(help_text='Comma seprated Items',null=True,blank=True)
    non_recyclable_items=models.TextField(help_text='Comma seprated Items',null=True,blank=True)

    def __str__(self):
        return self.recyclable_items