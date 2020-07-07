from rest_framework import serializers
from articles.models import Article, Category
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)
import six

class NewTagListSerializerField(TagListSerializerField):
    def to_internal_value(self, value):
        if isinstance(value, six.string_types):
            value = value.split(',')

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


class BlogSerializer(TaggitSerializer, serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    category = CategorySerializer(required=True)
    tags = NewTagListSerializerField ()
    class Meta:
        model = Article
        fields = ['id', 'title', 'body', 'tags', 'category', 'author', 'date_added', 'updated_date']
        read_only_fields = ['date_added', 'updated_date']