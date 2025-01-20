from rest_framework import serializers
from words.models import Word, English, Translation, Aspect, LinkedWord


class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Word
        fields = [
            'pid',
            'tagalog',
            'root',
            'accents',
            'alternate_spelling',
            'is_irregular_verb',
            'note',
            'audio_url'
        ]
        
        
class EnglishSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = English
        fields = ['english']
        
        
class TranslationSerializer(serializers.ModelSerializer):
    english_meanings = EnglishSerializer(many=True)
    
    class Meta:
        model = Translation
        fields = [
            'part_of_speech',
            'english_meanings'
        ]
        
        
class AspectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspect
        fields = [
            'tagalog',
            'aspect',
            'accents',
            'audio_url'
        ]
        
        
class LinkedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedWord
        fields = [
            'linked_word',
            'particle',
            'english_meaning',
            'audio_url'
        ]