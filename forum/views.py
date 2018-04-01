from forum.models import Post

from django.shortcuts import render, get_object_or_404


def index(request):
    return HttpResponse("Hello, World!")

# Return the recent posts
# Recently posted
def news(request):
    latest_posts = Post.objects.order_by('post_date')
    context = {
        'lastest_post_list' : latest_posts
    }

    #output = ', '.join([q.post_text for q in latest_posts])
    #return HttpResponse(output)

    #return HttpResponse(template.render(context, request))
    return render(request, 'forum/index.html', context)

def results(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'forum/results.html', {'post' : post})


# Return the hottest post
# More voted
def hot(request):
    pass

def best(request):
    pass