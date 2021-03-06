from django.db import models
import re
from django.core.exceptions import ValidationError

def lnglat_validator(value) :
    if re.match(r'^\d+\.?\d*/\d+\.?\d*$', value) :
        pass
    else :
        raise ValidationError('Invalid LngLat Type')


# Create your models here.
class Post(models.Model) :

    STATUS_CHOICE =(
        ('d', 'draft'),
        ('p', 'published'),
        ('w','withdrawn'),
    )

    title = models.CharField(max_length= 100, verbose_name = "제목")
    content = models.TextField()
    tags= models.CharField(max_length=100, blank= True,
                           help_text = 'Optional 입니다.')
    lnglat = models.CharField(max_length = 50 ,
                              help_text = 'Optional 위도/경도 포맷으로 입력',
                              validators = [lnglat_validator],
                              blank = True)
    status = models.CharField(max_length = 1,  choices = STATUS_CHOICE )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
