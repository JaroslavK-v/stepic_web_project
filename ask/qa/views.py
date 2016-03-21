from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse, Http404

def test(request, *args, **kwargs):
    return HttpResponse('OK')


def draw_new(request):
    questions = Question.objects.all()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/ask/new_questions/?page='
    page = paginator.page(page)
    return render(request, 'ask/new_questions.html', {
        'questions' : page.object_list,
        'paginator' : paginator,
        'page' : page 
        })


def draw_popular(request):
    questions = Question.objects.order_by(rating)
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/ask/popular/?page='
    page = paginator.page(page)
    return render(request, 'ask/popular.html', {
        'questions' : page.object_list,
        'paginator' : paginator,
        'page' : page 
        })

def draw_question(request, id):
    try:
        question = Question.objects.get(id = id)
    except Question.DoesNotExist:
        raise Http404
    return render(request, 'ask/question.html', {
        'question' : question,
        'title' : question.title,
        'text' : question.text,
         
        })

'''def draw_answer(request):
    try:
        answer = Answer.objects.all
    except Answer.DoesNotExist:
        raise Http404
    return render(request, 'ask/answer.html', {
        'question' : question,
        'text' : answer.text,
         
        })
    '''
