from django.shortcuts import render, redirect 
from .models import Post, PostAttachments, Comments 
from .form import PostForm 
from django.contrib.auth.decorators import login_required

# Create your views here.
def post_list(request):
    posts = Post.objects.order_by('-time_stamp')
    for post in posts:
        att = PostAttachments. objects.filter(post_id = post.pk)
        post.att = att
        comments_pin = Comments.objects.filter(post_id = post.pk, pinned = True)
        comments_reg = Comments.objects.filter(post_id = post.pk, pinned = False)
        post.comments_pin = comments_pin 
        post.comments_reg = comments_reg

    if request.method == 'POST':
        action = request.POST.get('action')
        post_id = request.POST.get('post_id')
        if action == 'comment':
            Comments.objects.update_or_create(
            content = request.POST['content'],
            post_id = post_id,
            author = request.user,
        )
        
        elif action == 'likes':
            post = Post.objects.get(pk = post_id)
            if request.user in post.likes.all():
                post.likes.remove(request.user)
            else:
                post.likes.add(request.user)
        return redirect(to='post_list')
    
    return render(request, 'post/post_list.html', {'posts': posts})

def post_details(request, pid):
    post = Post.objects.get(pk = pid)
    images = PostAttachments.objects.filter(post_id = pid)
    comments = Comments.objects.filter(post_id = pid)
    return render(request, 'post/post_details.html', {'post': post, 'images': images, 'comments' : comments})

@login_required
def new_post(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        att = request.FILES.getlist('images')
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for img in att:
                PostAttachments.objects.create(post_id = post.pk, file=img)
        return redirect(to='post_details', pid=post.pk)
    return render(request, 'post/new_post.html', {'form': form})

'''
request.method = ('POST', 'Get', 'PUT', 'PATCH', 'DELETE')
'''
@login_required
def post_edit(request, pid):
    post = Post.objects.get(pk = pid)
    post_att = PostAttachments.objects.filter(post_id = pid)
    if request.method != 'POST':
        form = PostForm(instance = post)
    else:
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit=False)
            att = request.FILES.getlist('images')
            for img in att:
                PostAttachments.objects.create(
                    post_id = pid, file = img
                )
            chosen = request.POST.getlist('attachments')
            for img_id in chosen:
                PostAttachments.objects.get(pk = img_id).delete()
            post.edited = True 
            post.save()
        return redirect(to='post_details', pid=post.pk)
    return render(request, 'post/edit_post.html', {'form': form, 'post_att': post_att})

@login_required
def delete_post(request, pid):
    post = Post.objects.get(pk = pid)
    post.delete()
    return redirect(to='post_list')

