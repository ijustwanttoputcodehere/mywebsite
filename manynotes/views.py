from django.contrib.admin.templatetags.admin_list import pagination
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import NoteForm
from .models import Notes

# Create your views here.
class Home(TemplateView):
    template_name = 'home.html'

@login_required(login_url='login')
def home(request):
    return render(request=request, template_name="manynotes/home.html")


@login_required(login_url='login')
def base(request):
    return render(request=request, template_name="manynotes/base.html")


@login_required(login_url='login')
def categories(request):
    return render(request=request, template_name="manynotes/categories.html")


@login_required(login_url='login')
def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, "manynotes/upload.html")


@login_required(login_url='login')
def notes_list(request):
    notes = Notes.objects.all()
    return render(request, 'manynotes/notes_list.html', {'notes': notes})


@login_required(login_url='login')
def upload_notes(request):
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'manynotes/upload_notes.html', {'form': form})


@login_required(login_url='login')
def delete_notes(request, pk):
    if request.method == 'POST':
        note = Notes.objects.get(pk=pk)
        note.delete()
    return redirect('notes_list')


@login_required(login_url='login')
def search(request):
    template = 'manynotes/notes_list.html'

    query = request.GET.get('q')
    if query:
        notes = Notes.objects.filter(Q(title__icontains=query) | Q(author__icontains=query))

        return render(request, template, {'notes': notes})
    else:
        return redirect('notes_list')


@login_required(login_url='login')
def category_1(request):
    template = 'manynotes/notes_list.html'

    notes = Notes.objects.filter(Q(category__icontains='Kid'))
    return render(request, template, {'notes': notes})


@login_required(login_url='login')
def category_2(request):
    template = 'manynotes/notes_list.html'

    notes = Notes.objects.filter(Q(category__icontains='Mix'))
    return render(request, template, {'notes': notes})


@login_required(login_url='login')
def category_3(request):
    template = 'manynotes/notes_list.html'

    notes = Notes.objects.filter(Q(category__icontains='Women'))
    return render(request, template, {'notes': notes})


@login_required(login_url='login')
def category_4(request):
    template = 'manynotes/notes_list.html'

    notes = Notes.objects.filter(Q(category__icontains='W'))
    return render(request, template, {'notes': notes})


@login_required(login_url='login')
def category_5(request):
    template = 'manynotes/notes_list.html'

    notes = Notes.objects.filter(Q(category__icontains='Men'))
    return render(request, template, {'notes': notes})


def logout_request(request):
    logout(request)
    return render(request, "manynotes/home.html")


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    form = AuthenticationForm()
    return render(request, "manynotes/login.html", {"form": form})
