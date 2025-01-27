from django.shortcuts import render, redirect
from .models import Quiz, Question, Answer
from django.contrib.auth.decorators import login_required

# Home page
def home(request):
    return render(request, 'quiz/home.html')  
#کاری که باید بکنم اینه دیتا بهش بدمو واسه استارت و اسکور پیج بسازم و همینطور تغییرات توی فرانت و نوشته هاش


# Start quiz page
@login_required
def start_quiz(request):
    quiz = Quiz.objects.first()  # You can fetch a quiz based on the user's choice
    questions = quiz.questions.all()
    question = questions.first()  # Show the first question
    if request.method == 'POST':
        answer = request.POST.get('answer')
        # Check if the answer is correct
        correct_answer = question.correct_answer
        if answer.lower() == correct_answer.lower():
            request.session['score'] = request.session.get('score', 0) + 1
        return redirect('quiz:next_question', question.id)
    return render(request, 'quiz_page.html', {'quiz': quiz, 'question': question})

# Show score
@login_required
def show_score(request):
    score = request.session.get('score', 0)
    return render(request, 'score.html', {'score': score})

# Finish quiz
@login_required
def finish_quiz(request):
    score = request.session.get('score', 0)
    return render(request, 'score.html', {'score': score})
