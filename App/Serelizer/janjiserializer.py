from rest_framework import serializers
from App.models import DetailPembuatJanji


class JanjiSerializer (serializers.ModelSerializer):
    class Meta:
        model = DetailPembuatJanji
        fields = '__all__'
