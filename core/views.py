from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm

from .models import publicCategory, publicPhoto

def public(request):
    user = request.user
    publiccategory = request.GET.get('publiccategory')
    if publiccategory == None:
        publicphotos = publicPhoto.objects.filter(publiccategory__user=user)
    else:
        publicphotos = publicPhoto.objects.filter(
            publiccategory__name=publiccategory, publiccategory__user=user)

    publiccategories = publicCategory.objects.filter(user=user)
    context = {'publiccategories': publiccategories, 'publicphotos': publicphotos}
    return render(request, 'core/public.html', context)

def publicaddPhoto(request):
    user = request.user

    publiccategories = user.publiccategory_set.all()

    if request.method == 'POST':
        data = request.POST
        publicimages = request.FILES.getlist('publicimages')

        if data['publiccategory'] != 'none':
            publiccategory = publicCategory.objects.get(id=data['publiccategory'])
        elif data['publiccategory_new'] != '':
            publiccategory, created = publicCategory.objects.get_or_create(
                user=user,
                name=data['publiccategory_new'])
        else:
            publiccategory = None

        for publicimage in publicimages:
            publicphoto = publicPhoto.objects.create(
                publiccategory=publiccategory,
                publicdescription=data['publicdescription'],
                publicimage=publicimage,
            )

        return redirect('public')

    context = {'publiccategories': publiccategories}
    return render(request, 'core/publicadd.html', context)


def frontpage(request):
    return render(request, 'core/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'core/signup.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('frontpage')

def faqs(request):
    return render(request, 'core/faqs.html')
