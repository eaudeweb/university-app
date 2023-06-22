from django.template.response import TemplateResponse
from .models import University

def filter_name(search, university_name):
    if search == None or search == "":
        return True

    search = search.lower()
    for i in range(len(university_name)):
        if university_name[i] == search[0]:
            return university_name[i:i+len(search)] == search

def filter_city(city, university_city):
    if city == None or city == university_city or city == "":
        return True

def filter_country(country, university_country):
    if country == None or country == university_country or country == "":
        return True

def filter_domain(domain, university_domain):
    if domain == None or domain == university_domain or domain == "":
        return True

def filter_universities(request):
    universities = []
    search = None
    city = None
    country = None
    domain = None

    if request.method == 'POST':
        city = request.POST.get('city')
        country = request.POST.get('country')
        domain = request.POST.get('domain')
        search = request.GET.get('search')
        
    elif request.method == 'GET':
        search = request.GET.get('search')
    else:
        universities = University.objects.all()


    for university in University.objects.all():
        if filter_name(search, university.name.lower()) and filter_city(city, university.city) and filter_country(country, university.country) and filter_domain(domain, university.domain):
            universities.append(university)

    t = TemplateResponse(request, 'universities/filter.html', {'universities': universities})

    return t.render()

def university_page(request):
    if request.method == 'GET':
        university_name = request.GET.get('University')

    for university in University.objects.all():
        if university.name == university_name:
            university_shown = university

    t = TemplateResponse(request, 'universities/university.html', {'university': university_shown})

    return t.render()
