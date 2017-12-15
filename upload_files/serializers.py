from rest_framework import serializers

from upload_files.models import TextFile, MediaFile


class TextFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextFile
        fields = '__all__'


class MediaFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = MediaFile
        fields = '__all__'

