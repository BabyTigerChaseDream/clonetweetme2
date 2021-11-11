from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render
from .models import Tweet
import random
# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html",context={},status=200)
    #return HttpResponse("<h1>Hello World</h1>")

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Andriod
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content, "likes":random.randint(0,10)} for x in qs]
    data = {
        "response": tweets_list,
        "isUser":False
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    '''
    REST API VIEW
    Consume by Javascript or Swift/Java/iOS/Android
    '''
    data = {
        'id':tweet_id,
        #'content':obj.content,
        #'image_path':obj.image

    }
    # by detauls status is 500 
    status = 200

    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'Not Found'
        status = 404
        #raise Http404

    # json.dumps content_type='application/json'
    return JsonResponse(data,status=status)
    #return HttpResponse(f"<h1>Hello {tweet_id} - {obj.content}</h1>")