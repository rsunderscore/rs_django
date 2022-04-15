from django.db import models
from django.conf import settings

# Create your models here.

class Vocab(models.Model):
    eng = models.CharField(max_length=50, help_text='an english translation')
    esp = models.CharField(max_length=50, help_text='a spanish translation')
    pos = models.CharField(max_length=20, help_text = 'the part of speech for the word, e.g. noun, verb')
    sub_date = models.DateField(auto_now_add = True, help_text = 'date submitted')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=False, help_text='user that entered this translation')
    
class PartOfSpeech(models.Model):#verb, noun, adjective, adverb, pronoun, article, preposition
    pos = models.CharField(max_length=50, help_text='the part of speeach, e.g. noun, verb')
    description = models.TextField(max_length=255, help_text='what does it do')
    
#moods: indicative, subjunctive, imperative, progressive, perfect, perfect subjunctive
## imperative may be positive or negative
#others: infinitive, past participle, present participle
#pronouns: yo, tú, él/ella/usted, nosotros, vosotros, ellos/ellas/ustedes
#person: 1st, 2nd (informal), 2nd/3rd (formal), 1st (plural), 2nd(inf plural), 2nd/3rd (formal plural)
#tenses: past/preterite, present, future, imperfect, conditional