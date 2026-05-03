from rest_framework import serializers
from tailwind.models import Portfolio, Artwork

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = "__all__"

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = "__all__"