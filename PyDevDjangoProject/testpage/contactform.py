'''
Created on 25 июл. 2019 г.

@author: av.novikov3
'''
from django import forms
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

class ContactForm(forms.Form):
    firstname = forms.CharField(max_length = 100, label = 'Имя')        
    middlename = forms.CharField(max_length = 100, label = 'Отчество')
    lastname = forms.CharField(max_length = 100, label = 'Фамилия')
    email = forms.EmailField(label = 'Email', required = False)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # assert False
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'testpage/contact.html', {'form': form, 'submitted': submitted})
    