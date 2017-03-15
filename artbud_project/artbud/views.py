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
	
	visitor_cookie_handler(request)
	context_dict['visits'] = request.session['visits']

	response = render(request, 'artbud/index.html', context_dict)
	return response


def category(request):
	context_dict = {}
	response = render(request,'artbud/category.html',context_dict)
	return response

@login_required
def add_category(request):
	form = CategoryForm()
	if request.method == 'POST':
		form = CategoryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
		return index(request)
	else:
		print(form.errors)

	return render(request, 'artbud/add_category.html', {'form': form})	
	
def show_category(request, category_name_slug):
	context_dict = {}
	
	try:
		category = Category.objects.get(slug=category_name_slug)
		pages = Page.objects.filter(category=category).order_by('-views')
		context_dict['pages'] = pages
		context_dict['category'] = category
	except Category.DoesNotExist:
		context_dict['category'] = None
		context_dict['pages'] = None
		
	return render(request, 'artbud/category.html', context_dict)
	
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
	
def get_server_side_cookie(request, cookie, default_val=None):
	val = request.session.get(cookie)
	
	if not val:
		val = default_val
		
	return val


def visitor_cookie_handler(request):
	visits = int(get_server_side_cookie(request, 'visits', '1'))
	last_visit_cookie = get_server_side_cookie(request,'last_visit',
	str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')
	
	if (datetime.now() - last_visit_time).days > 0:
		visits = visits + 1
		request.session['last_visit'] = str(datetime.now())
		
	else:
		visits = 1
		request.session['last_visit'] = last_visit_cookie
		request.session['visits'] = visits
		
def track_url(request):
	page_id = None
	url = '/artbud/'
	if request.method == 'GET':
		if 'page_id' in request.GET:
			page_id = request.GET['page_id']
			
			try:
				page = Page.objects.get(id=page_id)
				page.views = page.views + 1
				page.save()
				url = page.url
			except:
				pass
				
	return redirect(url)
	
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
		{'website': userprofile.website, 'picture': userprofile.picture, 'bio': userprofile.bio, 'artwork': userprofile.artwork})
	
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









	
	
	