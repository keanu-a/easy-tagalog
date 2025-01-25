from django.db import models
import uuid
        

class Word(models.Model):
    
    pid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    tagalog = models.CharField(max_length=60, blank=False)
    
    root = models.CharField(max_length=60, blank=False)
    accents = models.JSONField() # Must be an array of integers
    
    alternate_spelling = models.CharField(max_length=60, blank=True, null=True, unique=True)
    is_irregular_verb = models.BooleanField(default=False)
    note = models.CharField(max_length=60, blank=True)

    audio_url = models.CharField(max_length=60)
    
    class Meta:
        unique_together = ('tagalog', 'accents',)
    
    def __str__(self) -> str:
        return self.tagalog
    
    def is_verb(self) -> bool:
        return self.translations.filter(part_of_speech=Translation.PartOfSpeech.VERB).exists()
    
    
# Many-to-many to Translation
class English(models.Model):
    
    meaning = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return self.meaning
    
    
# Many-to-one to Word
# Many-to-many to English
class Translation(models.Model):
    
    class PartOfSpeech(models.TextChoices):
        NOUN = 'N', 'noun'
        VERB = 'V', 'verb'
        ADJECTIVE = 'ADJ', 'adjective'
        ADVERB = 'ADV', 'adverb'
        PRONOUN = 'PRON', 'pronoun'
        PREPOSITION = 'PREP', 'preoposition'
        CONJUNCTION = 'CONJ', 'conjunction'
        INTERJECTION = 'INTERJ', 'interjection'
        INTERROGATIVE = 'INTERR', 'interrogative'
        ARTICLE = 'ART', 'article'
        PARTICLE = 'PART', 'particle'
        PREFIX = 'PRE', 'prefix'
        
    part_of_speech = models.CharField(max_length=60, choices=PartOfSpeech.choices, blank=False)
    
    english_meanings = models.ManyToManyField(English, related_name='english_meanings')
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='translations')
    
    def __str__(self) -> str:
        english_meanings = ", ".join([str(meaning) for meaning in self.english_meanings.all()])
        return f"{self.word.tagalog} [{self.part_of_speech}]: {english_meanings}"
    

# Many-to-one Word
class Aspect(models.Model):
    
    class AspectType(models.TextChoices):
        COMPLETED = 'COMP', 'completed'
        UNCOMPLETED = 'UNCOMP', 'uncompleted'
        CONTEMPLATED = 'CONT', 'contemplated'
        
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='aspects')
        
    tagalog = models.CharField(max_length=60, unique=True)
    aspect = models.CharField(max_length=10, choices=AspectType)
    accents = models.JSONField() # Must be an array of integers
    audio_url = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return f"{self.word.tagalog} ({self.aspect}): {self.tagalog}"
    

# Many-to-one Word
class LinkedWord(models.Model):
    
    word = models.ForeignKey(Word, on_delete=models.CASCADE, related_name='linked_words')
    
    linked_word = models.CharField(max_length=60, unique=True)
    particle = models.CharField(max_length=10)
    english_meaning = models.CharField(max_length=60)
    audio_url = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return f"{self.linked_word}: {self.word.tagalog} + {self.particle}]"