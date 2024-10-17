from django.shortcuts import render, redirect, get_object_or_404
from .models import Link
from .forms import LinkForm

def create_link(request):
    form = LinkForm(request.POST or None)
    if form.is_valid():
        link = form.save()
        return redirect('link_list')
    return render(request, 'links/create_link.html', {'form': form})

def link_list(request):
    links = Link.objects.all()
    return render(request, 'links/link_list.html', {'links': links})

def redirect_link(request, code):
    link = get_object_or_404(Link, short_code=code)
    return redirect(link.original_url)
