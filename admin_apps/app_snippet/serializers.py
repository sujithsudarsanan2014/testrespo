from rest_framework import serializers
from .models import Snippet, Tag
from django.contrib.auth.models import User


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']


class SnippetSerializer(serializers.ModelSerializer):
    tag = TagSerializer()

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'note', 'created_at', 'updated_at', 'user', 'tag']

    def create(self, validated_data):
        tag_data = validated_data.pop('tag')
        tag, created = Tag.objects.get_or_create(title=tag_data['title'])
        snippet = Snippet.objects.create(tag=tag, **validated_data)
        return snippet
