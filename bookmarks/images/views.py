from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Image

@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImageCreateForm(request.POST, request.FILES)
        if form.is_valid():
            # form data is valid
            cd = form.cleaned_data
            new_item = form.save(commit=False)

            # assign current user to the item
            new_item.user = request.user
            new_item.save()
            messages.success(request, 'Image added successfully')

            # redirect to new created item detail view
            return redirect(new_item.get_absolute_url())
    else:
        form = ImageCreateForm(data=request.GET)
    return render(request, 'images/image/create.html',
                  {'section': 'images', 'form': form})


def image_list(request):
    if request.user.is_authenticated:
        images = Image.objects.filter(user_id=request.user.id)
    else:
        images = Image.objects.filter(private=True)
    paginator = Paginator(images, 8)
    page = request.GET.get('page')
    try:
        images = paginator.page(1)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    return render(request, 'images/image/list.html',
                  {'section': 'images', 'images': images})


def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    return render(request, 'images/image/image.html',
                  {'section': 'images', 'image': image})

