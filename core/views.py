from django.shortcuts import render, get_object_or_404, redirect
from .forms import UserFeedbackForm, SchoolFilterForm
from django.http import JsonResponse
from django.views import View
from .models import *
from django.db.models import Q
# from .filters import SchoolFilter

# Create your views here.
def home(request):
    query = request.GET.get('query', '')
    schools = School.objects.filter(Q(name__icontains=query))
    ads = SchoolAds.objects.filter(is_active=True)
    regions = Region.objects.all().order_by('id')

    context  = {
        'regions':regions,
        'query':query,
        'ads':ads,
        'schools':schools,

    }
    return render(request, 'home.html', context)


class AutocompleteSchoolsView(View):
    def get(self, request, *args, **kwargs):
        term = request.GET.get('term', '')
        schools = School.objects.filter(name__icontains=term).values_list('name', flat=True)
        data = list(schools)
        return JsonResponse(data, safe=False)


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



def about_page(request):
    return render(request, 'about.html')


def school_list(request):
    query = request.GET.get('query', '')
    form = SchoolFilterForm(request.GET)
    schools = School.objects.filter(Q(name__icontains=query))
    regions = Region.objects.all()
    

    if form.is_valid():
        name = form.cleaned_data.get('name')
        region = form.cleaned_data.get('region')
        subcategory = form.cleaned_data.get('subcategory')
        location = form.cleaned_data.get('location')

        if name:
            schools = schools.filter(name__icontains=name)
        if region:
            schools = schools.filter(region=region)
        
        if location:
            schools = schools.filter(location__icontains=location)

    context = {
        'schools': schools,
        'form': form,
        'regions':regions,
        
    }

    return render(request, 'school_list.html', context)

# class SchoolListView(ListView):
#     model = School
#     template_name = 'school_list.html'
#     context_object_name = 'schools'
#     paginate_by = 10

#     def get_queryset(self):
#         queryset = School.objects.all()
#         self.filterset = SchoolFilter(self.request.GET, queryset=queryset)
#         return self.filterset.qs

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['filter'] = self.filterset
#         return context