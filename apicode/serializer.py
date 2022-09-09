from dataclasses import field
from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    charges = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    title_name = serializers.SerializerMethodField()

    class Meta:
        model = Article
        #fields = ['id', 'title','author']
        fields = ['id','title', 'author','email','date','shipping','journal','myimage','charges','image_url','title_name']

    def get_charges(self,obj):
        if obj.shipping == "online":
            return "Rs. 500"
        else:
            return "Rs. 600"

    def get_image_url(self,obj):
        return obj.myimage.url

    def get_title_name(self,obj):
        return obj.title

    def validate(self, data):
        if (data.get('author')):
            for n in data.get('author'):
                if n.isdigit():
                    raise serializers.ValidationError({'error':'Author name cannot be numeric'})
        
        return data

    
    