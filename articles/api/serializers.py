from rest_framework import serializers
from articles.models import Article, Category
from pages.models import Contact, Subscribe
from django.contrib.auth.models import User
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
import six
import json

class NewTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        if isinstance(value, six.string_types):
            if not value:
                value = "[]"
            try:
                if(type(value) == str):
                    if(value.__contains__('"') == True):
                        value = json.loads(value)
                    else:
                        value = value.split(',')

            except ValueError:
                self.fail('invalid_json')

        if not isinstance(value, list):
            self.fail('not_a_list', input_type=type(value).__name__)

        for s in value:
            if not isinstance(s, six.string_types):
                self.fail('not_a_str')

            self.child.run_validation(s)

        return value

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title']


class BlogSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='article-detail',
        lookup_field='slug',
        lookup_url_kwarg='slug'
    )
    author = serializers.ReadOnlyField(source='author.username')
    # category = CategorySerializer
    tags = NewTagListSerializerField()
    class Meta:
        model = Article
        fields = ['id', 'url', 'title', 'body', 'tags',  'author', 'date_added', 'updated_date']
        read_only_fields = ['date_added', 'updated_date']
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['email']
