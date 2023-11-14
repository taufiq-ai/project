from django import forms

# Create your forms here
class CourseEndorse(forms.Form):
    id = forms.IntegerField(label="Course ID")
    name = forms.CharField(label="Course Name")
    language = forms.CharField(label="Course Language")
    price = forms.IntegerField(label="Course Price")
    