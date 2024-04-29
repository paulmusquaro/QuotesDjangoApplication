from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from quotes import models  # noqa
from .forms import AuthorForm


# Create your views here.
def detail(request, pk):
    author = models.Author.objects.get(pk=pk)
    return render(request, 'authors/authors.html', {'author': author})


@login_required(login_url='quotes:main')
def insert(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Author was success added')
            return redirect(to='authors:insert')
        else:
            return render(request, 'authors/update.html', {'form': form})
    return render(request, 'authors/update.html', {'form': AuthorForm()})