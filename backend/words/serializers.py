from rest_framework import serializers
from .models import Word, English, Translation, Aspect, LinkedWord


class EnglishSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = English
        fields = ['meaning']
        
        
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
        
    def validate(self, data):
        # Validate accents
        accents = data.get("accents", [])
        if not isinstance(accents, list) or not all(isinstance(i, int) for i in accents):
            raise serializers.ValidationError("Accents for aspects must be an array of integers")
        
        return data
        
        
class LinkedWordSerializer(serializers.ModelSerializer):
    class Meta:
        model = LinkedWord
        fields = [
            'linked_word',
            'particle',
            'english_meaning',
            'audio_url'
        ]


class WordSerializer(serializers.ModelSerializer):
    
    translations = TranslationSerializer(many=True)
    aspects = AspectSerializer(many=True)
    linked_words = LinkedWordSerializer(many=True)

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
            'audio_url',
            'translations',
            'aspects',
            'linked_words'
        ]
        
    def validate(self, data):
        # Validate if word is a verb
        if any(translation.part_of_speech == Translation.PartOfSpeech.VERB for translation in data['translations']):
            if "is_irregular_verb" not in data or data["is_irregular_verb"] == None:
                raise serializers.ValidationError("Must provide 'is_irregular_verb' if word is a verb")
            
            aspects = data.get("aspects", [])
            if data["aspects"].length != 3:
                raise serializers.ValidationError("Must provide 3 aspects if word is a verb")
            
            aspect_types = {aspect.aspect for aspect in aspects}
            required_aspects = {Aspect.AspectType.COMPLETED, Aspect.AspectType.UNCOMPLETED, Aspect.AspectType.CONTEMPLATED}
            
            if aspect_types != required_aspects:
                raise serializers.ValidationError(
                    f"Word must have one of each aspect: {required_aspects}. No more, no less, and no duplicates."
                )
                
        # Validate accents
        accents = data.get("accents", [])
        if not isinstance(accents, list) or not all(isinstance(i, int) for i in accents):
            raise serializers.ValidationError("Accents for words must be an array of integers")
                
        return data