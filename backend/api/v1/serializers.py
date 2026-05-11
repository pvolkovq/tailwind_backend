from rest_framework import serializers
from tailwind.models import Portfolio, Artwork

class PortfolioSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.user.username
    
    class Meta:
        model = Portfolio
        fields = (
            'username',
            'is_commissioning_open',
            'description',
        )

class ArtworkSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    def get_likes(self, obj):
        return obj.likes.count()
    
    class Meta:
        model = Artwork
        fields = "__all__"

class PublicPortfolioArtworkSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    artworks = serializers.ManyRelatedField(child_relation=ArtworkSerializer(), read_only=True)
    
    def get_username(self, obj):
        return obj.user.username
    
    class Meta:
        model = Portfolio
        fields = (
            'username',
            'is_commissioning_open',
            'description',
            'artworks',
        )