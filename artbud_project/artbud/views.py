from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from artbud.models import Page, UserProfile, Upload
from artbud.forms import UserProfileForm, UploadForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registration.backends.simple.views import RegistrationView


def index(request):
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'pages': page_list}

    response = render(request, 'artbud/index.html', context_dict)
    return response


def artwork(request):
    context_dict = {}
    response = render(request, 'artbud/artwork.html', context_dict)
    return response


def category(request):
    context_dict = {}
    response = render(request, 'artbud/category.html', context_dict)
    return response


def logout(request):
    context_dict = {}
    response = render(request, 'registration/logout.html', context_dict)
    return response


@login_required
def add_artwork(request):
    context_dict = {}
    response = render(request, 'artbud/add_artwork.html', context_dict)
    return response


@login_required
def register_profile(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()

            return redirect('index')
        else:
            print(form.errors)

    context_dict = {'form': form}

    return render(request, 'artbud/profile_registration.html', context_dict)


class artbudRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')


@login_required
def profile(request, username):
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return redirect('index')

    uploads = Upload.objects.filter(user=user)
    userprofile = UserProfile.objects.get_or_create(user=user)[0]
    form = UserProfileForm(
        {'website': userprofile.website, 'picture': userprofile.picture, 'bio': userprofile.bio})

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=userprofile)
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile', user.username)
        else:
            print(form.errors)

    return render(request, 'artbud/profile.html',
                  {'userprofile': userprofile, 'selecteduser': user, 'form': form, 'uploads': uploads})


def list_profiles(request):
    userprofile_list = UserProfile.objects.all()

    return render(request, 'artbud/list_profiles.html',
                  {'userprofile_list': userprofile_list})


@login_required
def user_upload_photography(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.user = request.user
            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()
            return render(request, 'artbud/upload_complete.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        uploads = Upload.objects.filter(category="Photography")

    return render(request, 'artbud/artwork.html', {'uploads': uploads, 'upload_form': upload_form})


@login_required
def user_upload_sculpture(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.user = request.user
            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()
            return render(request, 'artbud/upload_complete.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        uploads = Upload.objects.filter(category="Sculpture")

    return render(request, 'artbud/artwork.html', {'uploads': uploads, 'upload_form': upload_form})


@login_required
def user_upload_drawing(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.user = request.user
            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()
            return render(request, 'artbud/upload_complete.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        uploads = Upload.objects.filter(category="Drawing")

    return render(request, 'artbud/artwork.html', {'uploads': uploads, 'upload_form': upload_form})


@login_required
def user_upload_painting(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.user = request.user
            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()
            return render(request, 'artbud/upload_complete.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        uploads = Upload.objects.filter(category="Painting")

    return render(request, 'artbud/artwork.html', {'uploads': uploads, 'upload_form': upload_form})


@login_required
def user_upload_other(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.user = request.user
            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()
            return render(request, 'artbud/upload_complete.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        uploads = Upload.objects.filter(category="Other")

    return render(request, 'artbud/artwork.html', {'uploads': uploads, 'upload_form': upload_form})


@login_required
def user_upload(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save(commit=False)
            upload.user = request.user
            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()
            return render(request, 'artbud/upload_complete.html', {'upload_form': upload_form})
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
        uploads = Upload.objects.all()

    return render(request, 'artbud/upload.html', {'uploads': uploads, 'upload_form': upload_form})


def art_display(request, username, uploaded_picture):
	uploads = Upload.objects.filter(name=uploaded_picture)

	return render(request, 'artbud/art_display.html', {'uploads': uploads})


def art_delete(request, username, uploaded_picture):

	uploads = Upload.objects.filter(name=uploaded_picture, user=request.user)
	uploads.delete()

	return render(request, 'artbud/art_delete.html', {'uploads': uploads})
