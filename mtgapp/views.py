from django.shortcuts import render

def post_list(request):
    return render(request, 'mtgapp/post_list.html', {})
