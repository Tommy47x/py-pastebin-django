from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PasteText
from .forms import PasteTextForm

def index(request):
    if request.method == 'POST':
        form = PasteTextForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PasteTextForm()

    pastes = PasteText.objects.all()
    return render(request, 'index.html', {'form': form, 'pastes': pastes})

def new(request):
    return HttpResponse("Your text has been successfully saved. You can go back now.")
# Create your views here.
