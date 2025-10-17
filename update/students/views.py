from django.shortcuts import render

def student_list(request):
    
    students = [
        {"name": "amitha", "grade": 85, "passed": True},
        {"name": "greeshma", "grade": 55, "passed": False},
        {"name": "prabin", "grade": 92, "passed": True},
    ]

    
    return render(request, 'student_list.html', {'students': students})
