from rest_framework import serializers

from upload_files.models import TextFile


class TextFileSerializers(serializers.ModelSerializer):
    class Meta:
        model = TextFile
        fields = '__all__'