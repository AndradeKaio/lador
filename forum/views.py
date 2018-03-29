from django.http import HttpResponse

from forum.models import Post


def index(request):
    return HttpResponse("Hello, World!")


def news(request):
    latest_posts = Post.objects.order_by('post_date')
    output = ', '.join([q.post_text for q in latest_posts])
    return HttpResponse(output)