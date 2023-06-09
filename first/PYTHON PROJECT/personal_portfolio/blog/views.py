from django.shortcuts import render

def blogs(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/blogs.html',{'blogs': blogs})

