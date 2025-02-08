from django.db import models
import uuid
from words.models import Aspect, Word, LinkedWord, Translation


class Phrase(models.Model):
    
    pid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    tagalog = models.CharField(max_length=100, blank=False)
    english = models.CharField(max_length=100, blank=False)
    
    words = models.ManyToManyField('Word', through='PhraseWordMeaning')
    
    def __str__(self) -> str:
        return self.tagalog
    

# Many-to-one Phrase
class PhraseWordMeaning(models.Model):
    phrase = models.ForeignKey(Phrase, on_delete=models.CASCADE, related_name='word_meanings')
    
    word = models.ForeignKey(Word, on_delete=models.CASCADE, null=True, blank=True)  # Main word reference
    
    is_name = models.BooleanField(default=False)
    position = models.PositiveIntegerField()  # Position in the phrase

    class Meta:
        unique_together = ('phrase', 'position')

    def __str__(self) -> str:
        return f"{self.phrase.tagalog} - {self.word or self.linked_word} ({self.translation})"

        
