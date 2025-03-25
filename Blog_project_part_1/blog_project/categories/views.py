

# Create your views here.
from django.shortcuts import render,redirect
from .import forms

# Create your views here.
def add_category(request):
    if request.method=='POST': #user post request
     category_form=forms.CategoryForm(request.POST) #user er post request data eiknahe capture kore
     if category_form.is_valid(): #post kora data gula amr valid kina chek korbo
        category_form.save() #jode  data valid hoy tahole database a save hobe
        return redirect('add_category') #sob thik thakel add_catagory ei url a pathai dibo
     
    else:
       category_form=forms.CategoryForm()
        
    return render(request,'add_category.html',{'form':category_form})
