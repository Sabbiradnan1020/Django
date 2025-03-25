

# Create your views here.
from django.shortcuts import render,redirect
from .import forms
from.import models

# Create your views here.
def add_post(request):
    if request.method=='POST': #user post request
     post_form=forms.PostForm(request.POST) #user er post request data eiknahe capture kore
     if post_form.is_valid(): #post kora data gula amr valid kina chek korbo
        post_form.save() #jode  data valid hoy tahole database a save hobe
        return redirect('add_post') #sob thik thakel add_catagory ei url a pathai dibo
     
    else:
      post_form =forms.PostForm()
        
    return render(request,'add_post.html',{'form':post_form})


def edit_post(request,id):
    post=models.Post.objects.get(pk=id)
    post_form=forms.PostForm(instance=post)

    # print(post.tital)
    if request.method=='POST': #user post request
     post_form=forms.PostForm(request.POST,instance=post) #user er post request data eiknahe capture kore
     if post_form.is_valid(): #post kora data gula amr valid kina chek korbo
        post_form.save() #jode  data valid hoy tahole database a save hobe
        return redirect('homepage') #sob thik thakel add_catagory ei url a pathai dibo
    
    return render(request,'add_post.html',{'form':post_form})


def delete_post(request,id):
   post=models.Post.objects.get(pk=id)
   post.delete()
   return redirect('homepage')
   
   







