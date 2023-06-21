from django.shortcuts import render
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

    return render(request, 'universities/filter.html', {'universities': universities})
