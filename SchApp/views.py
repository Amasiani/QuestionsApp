from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.db.models import Q

from script.models import Question, School, Department

from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html', {})

def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required
def search_view(request):
    qs = Question.objects.all()
    schools = School.objects.all()
    #departments = Department.objects.all()
    queryset = [school_query = request.GET.get('school'),
                department_query = request.GET.get('department'),
                course_code_query = request.GET.get('course_code'),
                session_query = request.GET.get('session'),
                semester_query = request.GET.get('semester')
            ]
    
    
    #query = request.GET.get['q']
    #queries = query.split(" ")
    #for q in queries:
    
    queryset = get_list_or_404(Question, Q(course_code__icontains=course_code_query))
                                        #Q(department__name__icontains=department_query))
                                        #Q(school__name__icontains=school_query))

    
    if is_valid_queryparam(school_query) and school_query != 'choose...':
        qs = queryset.filter(name__icontains=school_query)

    if is_valid_queryparam(course_code_query):
       qs = queryset.filter(course_code__icontains=course_code_query)

    if is_valid_queryparam(department_query):
       qs = queryset.filter(name__icontains=department_query)
    
        #for search in searchs:
        #searchs = get_list_or_404(Question, course_code__startswith='cs')
    #queryset = queryset.append(query)
    context = {
        'queryset': queryset,
        'schools':  schools,
        #'searchs': searchs,
    }   


    return render(request, 'search.html', context)


def result_view(request):
    qs = Question.objects.all()

    context = {
        'qs': qs
    }

    return render(request, 'result.html', context)