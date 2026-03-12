from django.shortcuts import render, get_object_or_404
from .models import video
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.http import HttpResponse


def category_videos(request, slug):
    # جلب التصنيف أو رفع خطأ 404
    category = get_object_or_404(category, slug=slug)
    
    # جلب فيديوهات هذا التصنيف
    videos = video.objects.filter(category=category)
    
    
    # التقسيم (Pagination)
    from django.core.paginator import Paginator
    paginator = Paginator(videos, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'page_obj': page_obj,
    }
    return render(request, 'category.html', context)





def index(request):
    query = request.GET.get('q')
    if query:
        videos = video.objects.filter(title__icontains=query)
    else:
        videos = video.objects.all()

    paginator = Paginator(videos, 20) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
        
    context = {
        'videos': videos,
        'page_obj': page_obj,
        'query': query,
        }
    return render(request, 'index.html', context)


def watch(request, slug):
    # استخدم اسم مختلف للمتغير (مثل: video_obj)
    video_obj = get_object_or_404(video, slug=slug)
    others = video.objects.exclude(id=video_obj.id)[:8]

    context = {
        'video': video_obj,
        'others': others
    }
    return render(request, 'watch.html', context)
