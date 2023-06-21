'''
from django.shortcuts import render
from .models import University, Country, Course, Level

def index(request):
    context = {
        'countries': Country.objects.all(),
        'courses': Course.objects.all(),
        'levels': Level.objects.all(),
        'prestige_choices': University.PRESTIGE_CHOICES,
    }
    return render(request, 'index.html', context)
from django.shortcuts import render
from .models import University
'''
from django.shortcuts import render
from .models import University, Country, Level, Course

def index(request):
    countries = Country.objects.all()
    courses = Course.objects.all()
    levels = Level.objects.all()

    if request.method == 'POST':
        # filter the universities based on POST data
        country_name = request.POST.get('country')
        course_name = request.POST.get('course')
        level_name = request.POST.get('level')
        prestige_level = request.POST.get('prestige')

        universities = University.objects.all()

        if country_name:
            universities = universities.filter(country__name=country_name)
        if course_name:
            universities = universities.filter(course__name=course_name)
        if level_name:
            universities = universities.filter(level__name=level_name)
        if prestige_level:
            universities = universities.filter(prestige=prestige_level)
    else:
        universities = University.objects.all()

    context = {
        'countries': countries,
        'courses': courses,
        'levels': levels,
        'universities': universities
    }
    return render(request, 'index.html', context)

'''
def filter_university(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        course = request.POST.get('course')
        level = request.POST.get('level')
        prestige = request.POST.get('prestige')

        universities = University.objects.filter(
            country__name=country, 
            courses__name=course, 
            courses__level__name=level, 
            prestige=prestige
        )

        context = {
            'universities': universities,
        }

        return render(request, 'filter_university.html', context)

'''