from django.http import HttpResponse
from forum.models import Post
from django.template import loader

def index(request):
    return HttpResponse("Hello, World!")

# Return the recent posts
# Recently posted
def news(request):
    latest_posts = Post.objects.order_by('post_date')
    template = loader.get_template('forum/index.html')
    context = {
        'lastest_post_list' : latest_posts
    }

    #output = ', '.join([q.post_text for q in latest_posts])
    #return HttpResponse(output)

    return HttpResponse(template.render(context, request))

def results(request, post_id):
    response = "This is the post %s"
    return HttpResponse(response % post_id)


# Return the hottest post
# More voted
def hot(request):
    pass

def best(request):
    pass