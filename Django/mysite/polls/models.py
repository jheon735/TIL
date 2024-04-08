from django.db import models

# Create your models here.
class Questions(models.Model):
    question_text = models.CharField(max_length = 200)
    pub_date = models.DateTimeField(auto_now_add=True)
    # is_something = models.BooleanField(default=False) # Boolean 필드는 변수명 앞에 is를 하는게 좋다
    # average_score = models.FloatField(default = 0.0)
    # jason_field = models.JSONField(default = dict)

    def __str__(self):  # 자기 자신을 문자열로 저장할 떄 사용하는 법
        return f'제목: {self.question_text}, 날짜: {self.pub_date}'

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f'{self.choice_text}'