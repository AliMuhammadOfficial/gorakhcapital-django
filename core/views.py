from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    if request.method == "POST":
        full_name = request.POST.get('name', '')
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        return render(request, 'index.html', {'data': {'full_name': full_name, 'email': email, 'subject': subject, 'message': message}})
    else:
        return render(request, 'index.html')