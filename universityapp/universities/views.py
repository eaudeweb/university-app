from django.template.response import TemplateResponse
from .models import University

def filter_universities(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        if city != "":
            universities = University.objects.filter(city=city)
        else:
            universities = University.objects.all()
    elif request.method == 'GET':
        search = request.GET.get('search')
        universities = University.objects.filter(name=search)
        print(search)
    else:
        universities = University.objects.all()

    t = TemplateResponse(request, 'universities/filter.html', {'universities': universities})

    return t.render()
