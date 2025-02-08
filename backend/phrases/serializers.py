from rest_framework import serializers
from .models import Phrase, PhraseWordMeaning, Word, Aspect, LinkedWord


class PhraseWordSerializer(serializers.ModelSerializer):
    word = serializers.CharField(required=False)  # Accept word as a string instead of a ForeignKey ID
    linked_word = serializers.CharField(required=False, allow_null=True)
    aspect = serializers.CharField(required=False, allow_null=True)
    translation = serializers.CharField(required=True)  # English meaning as a string

    class Meta:
        model = PhraseWordMeaning
        fields = ['position', 'word', 'linked_word', 'aspect', 'translation']


class PhraseSerializer(serializers.ModelSerializer):
    phrase_words = PhraseWordSerializer(many=True)
    
    class Meta:
        model = Phrase
        fields = ['tagalog', 'english']
        
    def create(self, validated_data):
        tagalog_text = validated_data['tagalog']
        
        split_tagalog_text = tagalog_text.split(" ")
        
        position = 1
        for text in split_tagalog_text:
            word = Word.objects.filter(tagalog=text).first()
            
            
        