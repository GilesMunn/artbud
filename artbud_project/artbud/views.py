from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from artbud.models import Category, Page, UserProfile
from artbud.forms import CategoryForm, PageForm, UserForm, UserProfileForm
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from registration.backends.simple.views import RegistrationView

def index(request):
	page_list = Page.objects.order_by('-views')[:5]
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list, 'pages': page_list}

	response = render(request, 'artbud/index.html', context_dict)
	return response
	
def painting(request):
	context_dict = {}
	response = render(request,'artbud/painting.html',context_dict)
	return response

def drawing(request):
	context_dict = {}
	response = render(request,'artbud/drawing.html',context_dict)
	return response

def photography(request):
	context_dict = {}
	response = render(request,'artbud/photography.html',context_dict)
	return response

def sculpture(request):
	context_dict = {}
	response = render(request,'artbud/sculpture.html',context_dict)
	return response

def other(request):
	context_dict = {}
	response = render(request,'artbud/other.html',context_dict)
	return response

def category(request):
	context_dict = {}
	response = render(request,'artbud/category.html',context_dict)
	return response
	
def artwork(request):
	context_dict = {}
	response = render(request,'artbud/artwork.html',context_dict)
	return response
		
def add_page(request, category_name_slug):
	try:
		category = Category.objects.get(slug=category_name_slug)
	except Category.DoesNotExist:
		category = None

	form = PageForm()
	if request.method == 'POST':
		form = PageForm(request.POST)
		if form.is_valid():
			if category:
				page = form.save(commit=False)
				page.category = category
				page.views = 0
				page.save()
				return show_category(request, category_name_slug)
		else:
			print(form.errors)
			
	context_dict = {'form':form, 'category': category}
	return render(request, 'artbud/add_page.html', context_dict)
	
	
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

    context_dict = {'form':form}
    
    return render(request, 'artbud/profile_registration.html', context_dict)

class artbudRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')
	
	
def profile(request, username):
	try:
		user = User.objects.get(username=username)
	except User.DoesNotExist:
		return redirect('index')
		
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
		{'userprofile': userprofile, 'selecteduser': user, 'form': form})


def list_profiles(request):
	userprofile_list = UserProfile.objects.all()
	
	return render(request, 'artbud/list_profiles.html',
		{'userprofile_list' : userprofile_list})


@login_required
def like_category(request):
	cat_id = None
	if request.method == 'GET':
		cat_id = request.GET['category_id']
		likes = 0
	if cat_id:
		cat = Category.objects.get(id=int(cat_id))
		if cat:
			likes = cat.likes + 1
			cat.likes = likes
			cat.save()
		return HttpResponse(likes)


@login_required
def user_upload(request):
    if request.method == 'POST':
        upload_form = UploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload = upload_form.save()
            upload.name = name
            if 'picture' in request.FILES:
                upload.picture = request.FILES['picture']
            upload.save()
        else:
            print(upload_form.errors)
    else:
        upload_form = UploadForm()
    uploads = Upload.objects.all()

    return render(request, 'artbud/artwork.html',
                  {'upload_form': upload_form})
				  
		