from django.shortcuts import (render, get_object_or_404, HttpResponseRedirect)

# relative import of forms
from .models import GeeksModel
from .forms import GeeksForm

def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = GeeksForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "geeks/create_view.html", context)

def list_view(request):
    
    context = {}

    context['dataset'] = GeeksModel.objects.all()

    return render(request, "geeks/list_view.html", context)

# after updating it will redirect to detail_view
def detail_view(request, id):
    context = {}
    context['data'] = GeeksModel.objects.get(id = id)

    return render(request, "geeks/detail_view.html", context)

# update view for details
def update_view(request, id):
    context = {}
    
    # fetch the object related to passed id
    obj = get_object_or_404(GeeksModel, id = id)

    # pass the object as instance in form
    form = GeeksForm(request.POST or None, instance = obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("geeks/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "geeks/update_view.html", context)