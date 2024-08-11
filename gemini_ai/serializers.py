from rest_framework import serializers
from gemini_ai.models import RecognizedItem,ImageUploaded
from gemini_ai.gemini_ai import generate_json_from_images
import json


class ImageUploadedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageUploaded
        fields = ['id', 'image', 'uploaded_at']


class RecognizedItemsSerializers(serializers.ModelSerializer):
    images = ImageUploadedSerializer(many=True,required=False)
    class Meta:
        model=RecognizedItem
        fields='__all__'
        read_only_fields=['ai_json_response','recyclable_items','non_recyclable_items']

    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')

        gemini_data=generate_json_from_images(images_data)
        cleaned_text = gemini_data.replace('```', '')
        cleaned_text=cleaned_text.replace('json','')
        json_data = json.loads(cleaned_text)
        # print(json_data.get('Recyclable / Reusable objects'))

        recognized_item = RecognizedItem.objects.create(
            ai_json_response=json_data,
            recyclable_items=str(json_data.get("Recyclable / Reusable Objects", '')),
            non_recyclable_items=str(json_data.get("Non-Recyclable Objects", ''))
        )

        for image_data in images_data:
            image_uploaded = ImageUploaded.objects.create(image=image_data)
            recognized_item.images.add(image_uploaded)
        return recognized_item