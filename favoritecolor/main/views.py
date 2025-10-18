from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')
        context = {
            'name': name,
            'color': color,
            'form_data': request.POST
        }
        return render(request, 'result.html', context)
    return render(request, 'home.html')
