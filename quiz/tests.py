from django.test import TestCase
from .models import Quiz, Question, Answer

class QuizModelTest(TestCase):
    def test_create_quiz(self):
        quiz = Quiz.objects.create(title='Capital Quiz', description='Test quiz about capitals')
        self.assertEqual(quiz.title, 'Capital Quiz')

    def test_create_question(self):
        quiz = Quiz.objects.create(title='Capital Quiz', description='Test quiz about capitals')
        question = Question.objects.create(quiz=quiz, text='What is the capital of France?', correct_answer='Paris')
        self.assertEqual(question.text, 'What is the capital of France?')
