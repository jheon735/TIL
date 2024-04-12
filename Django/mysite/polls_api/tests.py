from django.test import TestCase
from polls_api.serializers import QuestionSerializer, VoteSerializer
from django.contrib.auth.models import User
from polls.models import Questions, Choice, Vote
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.utils import timezone

class QuestionListTest(APITestCase):
    def setUp(self):
        self.question_data = {'question_text':'some question'}
        self.url = reverse('question-list')

    def test_create_question(self):
        user = User.objects.create(username='testuser', password='testpass')
        self.client.force_authenticate(user=user)
        response = self.client.post(self.url, self.question_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Questions.objects.count(), 1)
        question = Questions.objects.first()
        self.assertEqual(question.question_text, self.question_data['question_text'])
        self.assertLess((timezone.now()-question.pub_date).total_seconds(), 1)

    def test_create_question_without_authentication(self):
        response = self.client.post(self.url, self.question_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_list_questions(self):
        question = Questions.objects.create(question_text='Question1')
        choice = Choice.objects.create(question=question, choice_text="choice1")
        Questions.objects.create(question_text="Question2")
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['choices'][0]['choice_text'], choice.choice_text)

class VoteSerializerTest(TestCase):
    def setUp(self):    # 각 테스트 수행 전 매번 시행됨
        self.user = User.objects.create(username='testuser')
        self.question = Questions.objects.create(
            question_text='abc',
            owner=self.user,
        )
        self.choice = Choice.objects.create(
            question = self.question,
            choice_text = '1',
        )

    def test_vote_serializer(self):
        data = {
            'question' : self.question.id,
            'choice' : self.choice.id,
            'voter' : self.user.id,
        }
        serializer = VoteSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        vote = serializer.save()

        self.assertEqual(vote.question, self.question)
        self.assertEqual(vote.choice, self.choice)
        self.assertEqual(vote.voter, self.user)

    def test_vote_serializer_with_duplicate_vote(self):
        choice1 = Choice.objects.create(
            question = self.question,
            choice_text = '2',
        )
        Vote.objects.create(question=self.question, choice=self.choice, voter=self.user)
        data = {
            'question' : self.question.id,
            'choice' : choice1.id,
            'voter' : self.user.id,
        }
        serializer = VoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_vote_serializer_with_unmatched_question_and_choice(self):
        question2 = Questions.objects.create(
            question_text='abc',
            owner=self.user,
        )
        choice2 = Choice.objects.create(
            question = question2,
            choice_text = '1',
        )
        data = {
            'question' : self.question.id,
            'choice' : choice2.id,
            'voter' : self.user.id,
        }
        serializer = VoteSerializer(data=data)
        self.assertFalse(serializer.is_valid())


# Create your tests here.
class QuestionSerializerTestCase(TestCase): #TestCase를 상속받아 아래 함수 이름이 test_이런식으로 시작되어야 실행됨
    def test_with_valid_data(self):
        # self.assertEqual(1, 2)  # 두 입력자료가 같은지 확인하는 함수
        serializer = QuestionSerializer(data={'question_text':'abc'})
        self.assertEqual(serializer.is_valid(), True)
        new_question = serializer.save()
        self.assertIsNotNone(new_question.id)

    def test_with_invalid_data(self):
        serializer = QuestionSerializer(data={'question_text':''})
        self.assertEqual(serializer.is_valid(), False)

