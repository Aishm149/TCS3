from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
#from .models import Profile
#from .forms import ProfileForm
from .models import Education
#from .forms import EducationForm
from .forms import SecondaryEducationForm
# from .forms import SeniorSecondaryEducationForm
# from .forms import PersonalDetails
# from .forms import Links
# from .forms import InternshipDetails

from django.utils import timezone


def edu_new(request):
    if request.method == "POST":
        form = SecondaryEducationForm(request.POST)
        if form.is_valid():
            Education = form.save(commit=False)
            Education.userID = request.user
            Education.created_date = timezone.now()
            Education.save()
    else:
        form= SecondaryEducationForm()
    return render(request, 'education/edu_edit.html', {'form': form, })
    # if request.method == "POST":
    #     formset = SeniorSecondaryEducationForm(request.POST)
    #     if formset.is_valid():
    #         Education = formset.save(commit=False)
    #         Education.userID = request.user
    #         Education.created_date = timezone.now()
    #         Education.save()
    # else:
    #     formset = SeniorSecondaryEducationForm()
    #




# def personal_details(request):
#     if request.method == "POST":
#         form = PersonalDetails(request.POST)
#         if form.is_valid():
#             Education = form.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         form= PersonalDetails()
#
#     if request.method == "POST":
#         formset = Links(request.POST)
#         if formset.is_valid():
#             Education = formset.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         formset = Links()
#
#     return render(request, 'education/personal_edit.html', {'form': form,
#                                                             'formset': formset})
#
#
# def internship_details(request):
#     if request.method == "POST":
#         form = InternshipDetails(request.POST)
#         if form.is_valid():
#             Education = form.save(commit=False)
#             Education.userID = request.user
#             Education.created_date = timezone.now()
#             Education.save()
#     else:
#         form= InternshipDetails()
#
#     return render(request, 'education/internship.html', {'form': form})