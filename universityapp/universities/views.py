from django.template.response import TemplateResponse
from .models import University

def filter_universities(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        if location != "":
            universities = University.objects.filter(location=location)
        else:
            universities = University.objects.all()
    else:
        universities = University.objects.all()

    t = TemplateResponse(request, 'universities/filter.html', {'universities': universities})

    return t.render()
