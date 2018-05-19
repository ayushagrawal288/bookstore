from rest_framework import serializers
from bookstore.models import Book, Author, Publisher
from django.core.exceptions import ObjectDoesNotExist


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    publisher = PublisherSerializer(many=False)
    author = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'

    def create(self, validated_data):
        import pdb
        pdb.set_trace()
        publisher_data = validated_data.pop('publisher')
        author_data = validated_data.pop('author')

        publisher_data.pop('id', None)
        try:
            publisher_ins = Publisher.objects.get(name=publisher_data.get('name'))
        except ObjectDoesNotExist:
            publisher_ins = Publisher.objects.create(**publisher_data)

        instance = Book.objects.create(publisher=publisher_ins, **validated_data)
        author_list = list()
        for data in author_data:
            data.pop('id', None)
            try:
                author_ins = Author.objects.get(name=data.get('name'))
            except ObjectDoesNotExist:
                author_ins = Author.objects.create(**data)
            author_list.append(author_ins)

        instance.author.set(author_list)
        instance.save()
        return instance

    def update(self, instance, validated_data):
        publisher_data = validated_data.pop('publisher')
        author_data = validated_data.pop('author')

        if publisher_data:
            publisher_id = publisher_data.pop('id', None)
            if instance.publisher.id == publisher_id:
                publisher_ins = instance.publisher
                for attr, value in publisher_data.items():
                    setattr(publisher_ins, attr, value)
                publisher_ins.save()
            else:
                instance.publisher = Publisher.objects.create(**publisher_data)

        author_qs = instance.author.all()

        for data in author_data:
            try:
                author_ins = author_qs.filter(name=data.get('name'))
                for attr, value in data.items():
                    setattr(author_ins, attr, value)
                author_ins.save()
            except ObjectDoesNotExist:
                author_ins = Author.objects.create(**data)
                instance.author.add(author_ins)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance
