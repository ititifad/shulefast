from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserFeedbackForm
from .models import *
from django.db.models import Q

# Create your views here.
def home(request):
    query = request.GET.get('query', '')
    regions = Region.objects.filter(Q(name__icontains=query))
    ads = SchoolAds.objects.filter(is_active=True)
    schools = School.objects.all().order_by('-id')

    context  = {
        'regions':regions,
        'ads':ads,
        'schools':schools
    }
    return render(request, 'home.html', context)


def region_cat(request, region_id):
    region = Region.objects.get(id=region_id)
    data = Category.objects.filter(region=region)

    context = {
        'region':region,
        'data':data
    }
    return render(request, 'region_cat.html', context)

def subcat_cat(request, category_id):
    category = Category.objects.get(id=category_id)
    data = SubCategory.objects.filter(category=category)

    context = {
        'category':category,
        'data':data
    }
    return render(request, 'subcat_cat.html', context)


def school_sub(request, subcategory_id):
    query = request.GET.get('query', '')
    subcategory = SubCategory.objects.get(id=subcategory_id)
    data = School.objects.filter(Q(subcategory=subcategory, name__icontains=query))

    context = {
        'subcategory':subcategory,
        'data':data
    }
    return render(request, 'schools_subcat.html', context)


def school(request, slug):
    school = get_object_or_404(School, slug=slug)

    files = SchoolJoining.objects.filter(school_id=school.id)

    context  = {
        'school':school,
        'files':files
    }
    return render(request, 'school_details.html', context)


def school_ad(request, id):
    ad = get_object_or_404(SchoolAds, id=id)

    context  = {
        'ad':ad,
        
    }
    return render(request, 'school_ads.html', context)


def feedback(request):
    if request.method == 'POST':
        form = UserFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you_page')  # Redirect to a thank you page or wherever you want

    else:
        form = UserFeedbackForm()

    return render(request, 'feedback.html', {'form': form})


def thank_you_page(request):
    return render(request, 'thanks.html')