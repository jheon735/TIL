from rest_framework import serializers
from polls.models import Questions
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

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
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'pub_date', 'owner']    

class UserSerializer(serializers.ModelSerializer):
    questions = serializers.PrimaryKeyRelatedField(many=True, queryset=Questions.objects.all())     #자기 테이블이 아닌 Question 테이블에서 찾아와야 하기 떄문에 명시해주는 부분

    class Meta:
        model = User
        fields = ['id', 'username', 'questions']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "두 패스워드가 일치하지 않습니다"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password2']