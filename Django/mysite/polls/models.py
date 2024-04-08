from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add=True)
    # is_something = models.BooleanField(default=False) # Boolean 필드는 변수명 앞에 is를 하는게 좋다
    # average_score = models.FloatField(default = 0.0)
    # jason_field = models.JSONField(default = dict)

    def __str__(self):  # 자기 자신을 문자열로 저장할 떄 사용하는 법
        if self.was_published_recently():
            new_badge = "NEW!!"
        else:
            new_badge = ""
        return f'{new_badge}제목: {self.question_text}, 날짜: {self.pub_date}'
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.choice_text}'