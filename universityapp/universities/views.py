from django.template.response import TemplateResponse
from .models import University

def filter_name(search, university_name):
    if search is None or search == "":
        return True

    search = search.lower()
    for i in range(len(university_name)):
        if university_name[i] == search[0]:
            return university_name[i:i + len(search)] == search

def filter_city(city, university_city):
    if city is None or city == university_city or city == "":
        return True

def filter_country(country, university_country):
    if country is None or country == university_country or country == "":
        return True

def filter_domain(domain, university_domain):
    if domain is None or domain == university_domain or domain == "":
        return True

def domain_filter_options(domains, university):
    contains = False
    if domains is not None:
        for i in domains:
            if university.domain == i:
                contains = True
                break
        if not contains:
            domains.append(university.domain)
    else:
        domains = []
        domains.append(university.domain)
    return domains

def country_filter_options(countries, university):
    contains = False
    if countries is not None:
        for i in countries:
            if university.country == i:
                contains = True
                break
        if not contains:
            countries.append(university.country)
    else:
        countries = []
        countries.append(university.country)
    return countries

def city_filter_option(countries, universities_array, cities):
    for i in range(len(countries)):
        row = []
        for university in universities_array:
            contains = False
            for j in row:
                if university.city == j:
                    contains = True
                    break
            if university.country == countries[i] and not contains:
                row.append(university.city)
        cities.append(row)
    return cities

def get_current_country_index(country, countries):
    for i in range(len(countries)):
        if country == countries[i]:
            return i
    return None

def filter_universities(request):
    universities = []
    cities = []
    countries = []
    domains = []
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

    for university in University.objects.all():
        if filter_name(search, university.name.lower()) and filter_city(city, university.city) and filter_country(country, university.country) and filter_domain(domain, university.domain):
            universities.append(university)

        countries = country_filter_options(countries, university)
        domains = domain_filter_options(domains, university)

    universities_array = University.objects.all()
    cities = city_filter_option(countries, universities_array, cities)
    current_country_index = get_current_country_index(country, countries)
    current_cities = cities[current_country_index] if current_country_index is not None else []

    t = TemplateResponse(request, 'universities/filter.html', {'universities': universities, 'countries': countries, 'cities': current_cities, 'domains': domains})
    return t.render()

def university_page(request):
    if request.method == 'GET':
        university_name = request.GET.get('University')

        for university in University.objects.all():
            if university.name == university_name:
                university_shown = university
                break
        else:
            university_shown = None

        t = TemplateResponse(request, 'universities/university.html', {'university': university_shown})
        return t.render()