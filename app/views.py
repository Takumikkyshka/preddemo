from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
# Create your views here.

from .models import Zayavka, Review
from .forms import CreateUserForm, CreateZayavkaForm

@login_required
def index(request):

    if request.method == 'POST' and not request.POST.get('review') == '':
        text = request.POST.get('review')
        zayavka_id = request.POST.get('zayavka_id')

        zayavka_from_db = Zayavka.objects.get(id=zayavka_id)

        Review.objects.create(
            text=text,
            user=request.user,
            zayavka=zayavka_from_db,
        )
        return redirect('/')

    data = Zayavka.objects.filter(user=request.user)

    return render(request, 'index.html', context={
        'data': data
    })

@login_required
def create(request):


    if request.method == 'POST':
        form = CreateZayavkaForm(request.POST)
        if form.is_valid():
            newForm = form.save(commit=False)
            newForm.user = request.user
            newForm.save()
        return redirect('/')

    else:
        form = CreateZayavkaForm()


    return render(request, 'create.html', context={
        'form': form
    })

def register(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    else:
        form = CreateUserForm()

    return render(request, 'register.html', context={
        'form': form
    })