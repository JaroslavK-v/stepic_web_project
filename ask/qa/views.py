from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question, Answer


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def draw_new(request):
    questions = Question.objects.order_by('-added_at')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/new/?page='
    page = paginator.page(page)
    return render(request, 'qa/new_questions.html', {
        'questions' : page.object_list,
        'paginator' : paginator,
        'page' : page 
        })


def draw_popular(request):
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'qa/popular.html', {
        'questions' : page.object_list,
        'paginator' : paginator,
        'page' : page 
        })

def draw_question(request, q_id):                                                             
    try:                                                                                      
        question = Question.objects.get(id = q_id)                                            
    except Question.DoesNotExist:                                                             
        raise Http404                                                                         
    #question = {'title' : "121", 'text' : "222", 'id': 44}                                   
    answer = Answer.objects.filter(question__exact = q_id)                                    
    #answer = {'text' : 'blablabla', 'question' : 3}                                          
    return render(request, 'qa/question.html', {                                              
        'question' : question,                                                                
        'title' : question.title,                                                             
        'text' : question.text,                                                               
        'answer' : answer,                                                                    
                                                                                              
        })         
