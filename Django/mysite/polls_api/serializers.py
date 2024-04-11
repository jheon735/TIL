from rest_framework import serializers
from polls.models import Questions

"""
class QuestionSerializer(serializers.Serializer):
    # 모델 필드에 대한 정의
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(max_length=200)
    pub_date = serializers.DateTimeField(read_only=True)

    # method 구현
    def create(self, validated_data):
        return Questions.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.question_text = validated_data.get('question_text', instance.question_text) + '[시리얼라이저에서 업데이트]'
        instance.save()
        return instance
"""

class QuestionSerializer(serializers.ModelSerializer):  #위에서 복잡하게 구현하던걸 쉽게 하도록 하는 메서드
    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'pub_date']    