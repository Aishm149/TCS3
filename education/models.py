from django.db import models
from django.utils import timezone


# class Profile(models.Model):
#     userID = models.ForeignKey('auth.User')
#     userName = models.CharField(max_length=20, unique=True)
#     firstName = models.CharField(max_length=200)
#     lastName = models.CharField(max_length=200)
#     email = models.EmailField()
#     contact = models.CharField()
#     #contact= models.USPhoneNumberField();
#     #created_date = models.DateTimeField(default=timezone.now)= ('firstName', 'lastName', 'contact')

class Education(models.Model):
    # userID = models.ForeignKey(User)
   

    CATEGORIES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    # PERSONAL DETAILS
    name = models.CharField(max_length=100, default='')
    homeadd = models.CharField(max_length=200, default='N/A')
    dob = models.DateField(default='2000-0-0')
    contact = models.IntegerField(default=0)
    gender = models.CharField(max_length=3, choices=CATEGORIES)

    # yoc1 is for Xth
    yoc1 = models.IntegerField()
    board1= models.CharField(max_length=200)
    percentage1 = models.IntegerField(default='0')
    # email = models.EmailField()

    # yoc2 is for XIIth
    yoc2 = models.IntegerField()
    board2 = models.CharField(max_length=200)
    percentage2 = models.IntegerField(default='0')

    #GRADUATION DETAILS
    yoc3 = models.IntegerField(blank=True)  # yoc3 is for graduation
    percentage3 = models.IntegerField(default='0', blank=True)
    college = models.CharField(max_length=100, default='N/A', blank=True)
    course = models.CharField(max_length=20, default='N/A', blank=True)

    #INTERNSHIP DETAILS
    company_i = models.CharField(max_length=200, default='N/A', blank=True)
    duration = models.IntegerField(default= 0, blank=True)
    profile_i=models.CharField(max_length=20, default='N/A', blank=True)

    # INTERNSHIP DETAILS 2
    company_i2 = models.CharField(max_length=200, default='N/A', blank=True)
    duration2 = models.IntegerField(default=0, blank=True)
    profile_i2 = models.CharField(max_length=20, default='N/A', blank=True)

    #MAIN SEARCH MODULE
    work = models.CharField(max_length=100, default='N/A', blank=True)

    #PROJECT
    title_p=models.CharField(max_length=30,default='N/A', blank= True)
    description_p= models.CharField(max_length=100, default='N/A', blank=True)

    #SKILLS
    skills= models.CharField(max_length=100)

    #LINKS
    git_hub = models.URLField(default='',  blank=True)
    linked_in = models.URLField(default='' , blank=True)







    # contact= models.USPhoneNumberField();
    # created_date = models.DateTimeField(default=timezone.now)= ('firstName', 'lastName', 'contact')
