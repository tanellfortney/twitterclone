from urllib import response
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm

def index(request):
    # If the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid():
            #Yes, Save
            form.save()

            #Redirect to Home
            return HttpResponseRedirect('/')

        else:
            #No, Show Error
            return HttpResponseRedirect(form.errors.as_json())


    # Get all posts, limit = 20
    posts = Post.objects.all()[:20]

    #show
    return render(request, 'posts.html',
                {'tweets': posts})


def delete(request, post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    post = Post.objects.get(id = post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect("not valid")
    form = PostForm
    return render(request, 'edit.html', {'post' : post})

# def upload(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = ImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj = form.instance
#             return render(request, 'upload.html', {'form':form, 'img_obj': img_obj})
#     else:
#         form = ImageForm()
#     return render(request, 'upload.html', {'form': form})

def like(request,post_id):
    heart=Post.objects.get(id = post_id)
    heart.like +=1
    heart.save()
    return HttpResponseRedirect('/')