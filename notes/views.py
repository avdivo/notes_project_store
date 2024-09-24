from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Theme, Note
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


@login_required
def theme_list(request):
    themes = Theme.objects.filter(user=request.user)  # Фильтруем темы по пользователю
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Theme.objects.create(name=name, user=request.user)
            return redirect('theme_list')
    return render(request, 'notes/theme_list.html', {'themes': themes})


def delete_theme(request, id):
    theme = get_object_or_404(Theme, id=id)
    if request.method == 'POST':
        theme.delete()
        return redirect('theme_list')
    return HttpResponse("Invalid request")


@login_required
def note_list(request, theme_id):
    theme = get_object_or_404(Theme, id=theme_id, user=request.user)  # Проверяем, что тема принадлежит пользователю
    notes = Note.objects.filter(theme=theme)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Note.objects.create(theme=theme, content=content)
            return redirect('note_list', theme_id=theme_id)
    return render(request, 'notes/note_list.html', {'theme': theme, 'notes': notes})


def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('note_list', theme_id=note.theme.id)
    return HttpResponse("Invalid request")


def home(request):
    if request.user.is_authenticated:
        return redirect('theme_list')  # Перенаправляем на список тем, если пользователь авторизован

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Логиним пользователя
            return redirect('theme_list')  # Перенаправляем на список тем
    else:
        form = AuthenticationForm()

    return render(request, 'notes/home.html', {'form': form})