from django.shortcuts import render

def lecture(request):
    return render(request, 'community/lecture.html')