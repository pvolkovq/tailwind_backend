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
    class Meta:
        model = Artwork
        fields = "__all__"