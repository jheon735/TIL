from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from polls.models import Questions
from polls_api.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status, mixins, generics
from rest_framework.views import APIView

# Create your views here.
"""
# Method 기반 구현
@api_view(['GET', 'POST']) # 변수를 주지 않을 땐 아래의 함수가 get요청을 처리할 것이라는 의미를 주는 데코레이터
def question_list(request):
    if request.method == 'GET':
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many = True) #many option으로 여러개의 question 처리 가능
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   #is_valid 이후에 진행하야 함
            return Response(serializer.data, status=status.HTTP_201_CREATED) #200도 정상이지만 생성했을 땐 201을 주도록 status 메서드를 활용한다
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, id):
    question = get_object_or_404(Questions, pk=id)
    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Class 기반 구현 APIView의 메서드를 사용하지 않은 버전
class QuestionList(APIView):
    def get(self, request):
        questions = Questions.objects.all()
        serializer = QuestionSerializer(questions, many = True) #many option으로 여러개의 question 처리 가능
        return Response(serializer.data)
    
    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()   #is_valid 이후에 진행하야 함
            return Response(serializer.data, status=status.HTTP_201_CREATED) #200도 정상이지만 생성했을 땐 201을 주도록 status 메서드를 활용한다
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetail(APIView):
    def get(self, request, id):
        question = get_object_or_404(Questions, pk=id)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, id):
        question = get_object_or_404(Questions, pk=id)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        question = get_object_or_404(Questions, pk=id)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#mixins의 메서드를 활용
class QuestionList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class QuestionDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""

#generics의 메서드를 활용
class QuestionList(generics.ListCreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer