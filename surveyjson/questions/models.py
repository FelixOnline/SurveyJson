from django.db import models


class Question(models.Model):

    HEADER='h'
    RADIO='r'
    DROPDOWN='d'
    CHECKBOX='c'
    FLOORPLAN='f'
    TYPE_CHOICES= (
        (HEADER, 'header'),
        (RADIO, 'radio'),
        (DROPDOWN, 'dropdown'),
        (CHECKBOX, 'checkbox'),
        (FLOORPLAN, 'floorplan'),
    )    
        
    label=models.TextField()
    kind=models.CharField(max_length=1, choices=TYPE_CHOICES, default=RADIO, verbose_name="type")
    default=models.CharField(max_length=30)
    name=models.CharField(max_length=20)
    inline=models.BooleanField(default=True)
    reverse=models.BooleanField(default=False)

    def __str__(self):
        return self.label + " - " + self.get_kind_display()

class Option(models.Model):

    value=models.CharField(max_length=40)
    label=models.CharField(max_length=40)
    question=models.ForeignKey(Question, related_name='Options')

class Dependency(models.Model):

    _id=models.CharField(max_length=40, verbose_name="id")
    value=models.CharField(max_length=40)
    question=models.ForeignKey(Question, related_name='Dependencies')
