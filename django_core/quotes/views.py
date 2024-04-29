from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import QuoteForm
from .models import Author, Quote, Tag
from .utils import get_mongodb
from django.core.paginator import Paginator
from collections import Counter


def main(request, page=1):
    quotes = list(Quote.objects.all())
    paginator = Paginator(list(quotes), 10)
    quotes_on_page = paginator.page(page)
    top_ten = top_tags()
    return render(request, "quotes/index.html", context={"quotes": quotes_on_page, "top_tags": top_ten})


@login_required(login_url='quotes:main')
def insert(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotes:main')
        else:
            return render(request, 'noteapp/note.html', {'form': form})
    return render(request, 'quotes/update.html', {"form": QuoteForm()})


def find(request, tag_name):
    quotes = list(Quote.objects.filter(tags__name=tag_name).all())
    return render(request, "quotes/tags.html", context={"result": tag_name, "quotes": quotes})


def top_tags():
    list_tags = []
    list_objects_tags = []
    for quote in list(Quote.objects.all()):
        for tag in list(quote.tags.all()):
            list_tags.append(tag.name)
    counter = Counter(list_tags)
    top_ten = list(sorted(counter, key=lambda x: counter[x], reverse=True)[:10])
    for tag in top_ten:
        list_objects_tags.append(Tag.objects.filter(name=tag).get())
    return list_objects_tags
