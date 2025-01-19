from django.shortcuts import render
from django.views.decorators.http import require_POST, require_GET
from django.http import JsonResponse
import hashlib
from datetime import datetime, timedelta
from .models import URL, AccessLog
from django.shortcuts import redirect
from django.utils import timezone
from django.db.models import Prefetch
from .serializers import AccessLogSerializer



@require_GET
def get_original_url(request, short_url):
    try:
        url_obj = URL.objects.get(shortened_url=short_url)
    except Exception as e:
        return JsonResponse({"status": "error", 'message': "there is no url with short_url provided"}, status=400)
    if url_obj.expiration_timestamp >= timezone.now():
        return JsonResponse({"status": "error", 'message': "the is expired"}, status=400)
    else :
        access_obj = AccessLog(
            url=url_obj,
            timestamp=datetime.now(),
            ip_address=request.META.get('REMOTE_ADDR')
        )
        access_obj.save()
        return redirect(url_obj.original_url)


@require_GET
def get_url_analytics(request, short_url):
    try:
        url_obj = URL.objects.prefetch_related(Prefetch('access_logs', queryset=AccessLog.objects.all(), to_attr='access_log_list')).get(shortened_url=short_url)
    except Exception as e:
        return JsonResponse({"status": "error", 'message': "there is no url with short_url provided"}, status=400)
    serializer = AccessLogSerializer(url_obj.access_log_list, many=True)
    return JsonResponse({'status':"success", "data": serializer.data}, status=200)

    return
    print(short_url)
    pass


@require_POST
def shorten(request):
    url = request.POST.get('Original URL')
    expiration_time = request.POST.get('Expiration', 12)
    errors = {}
    if not expiration_time.isdigit():
        errors['Expiration'] = "Invalid Expiration"
    if not url:
        errors['URL'] = "URL is required"
    if errors:
        return JsonResponse({"status": "error", "errors": errors}, status=400)
    encoded_url = url.encode('utf-8')
    hashed_url = hashlib.md5(encoded_url).hexdigest()
    expiration_time = datetime.now() + timedelta()
    url_obj = URL(original_url=url, shortened_url=hashed_url, expiration_timestamp=expiration_time)
    url_obj.save()
    return JsonResponse({"status": "success", "message": {"Shorten url": hashed_url}}, status=201)




