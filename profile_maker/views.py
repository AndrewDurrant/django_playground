

from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)
from .forms import Profile_Form
from .models import User_Profile

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def create_profile(request):
    form = Profile_Form()
    if request.method == 'POST':
        form = Profile_Form(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.display_picture = request.FILES['display_picture']
            file_type = user_pr.display_picture.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'profile_maker/error.html')
            user_pr.save()
            return render(request, 'profile_maker/details.html', {'user_pr': user_pr})
    context = {"form": form,}
    return render(request, 'profile_maker/create.html', context)


def list_view(request):
    context = {}
    context['dataset'] = User_Profile.objects.all()

    return render(request, 'profile_maker/list_view.html', context)

def detail_view(request, id):
    context = {}
    context['data'] = User_Profile.objects.get(id = id)

    return render(request, 'profile_maker/detail_view.html', context)

def update_view(request, id):
    context = {}

    obj = get_object_or_404(User_Profile, id = id)

    form = Profile_Form(request.POST or None, request.FILES or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/upload/'+id)

    context['form'] = form

    return render(request, 'profile_maker/update_view.html', context)
