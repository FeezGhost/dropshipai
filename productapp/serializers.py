from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    product             = serializers.CharField(max_length=500, allow_blank=True,  trim_whitespace=True)
    store_name          = serializers.CharField(max_length=500, allow_blank=True, trim_whitespace=True)
    platform            = serializers.CharField(allow_blank=True, trim_whitespace=True)
    username            = serializers.CharField(max_length=500, allow_blank=True,  trim_whitespace=True)
    bio                 = serializers.CharField(max_length=500, allow_blank=True, trim_whitespace=True)
    marketing_campaign  = serializers.CharField(allow_blank=True, trim_whitespace=True)
    web_design          = serializers.CharField(max_length=500, allow_blank=True,  trim_whitespace=True)
    ad_idea             = serializers.CharField(max_length=500, allow_blank=True, trim_whitespace=True)
    scaling             = serializers.CharField(allow_blank=True, trim_whitespace=True)