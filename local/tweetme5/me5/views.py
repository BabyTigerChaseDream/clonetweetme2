from django.http import HttpResponse,Http404,JsonResponse
from django.shortcuts import render
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request,"pages/home.html",context={},status=200)
    #return HttpResponse("<h1>Hello World</h1>")

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