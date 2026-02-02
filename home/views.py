from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post
from projects.models import Project
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm

# Create your views here.
def home(request):
    context = {}
    context["projects"] = Project.objects.all()
    context["posts"] = Post.objects.all()
    return render(request, 'home/home.html', context)

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Inquiry from Eduardo Gallifa"
            body = {
                'topic' : form.cleaned_data['topic'],
                'name' : form.cleaned_data['name'],
                'email' : form.cleaned_data['email'],
                'message' : form.cleaned_data['message'],
            }
            message = "\n".join(body.values())

            try:
                send_mail(subject, message, 'eduardogallifao@gmail.com', ['eduardogallifao@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header.')
            return redirect ("home")
    form = ContactForm()
    return render(request, 'home/contact.html', {'form':form})
