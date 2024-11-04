from django.http import HttpResponseForbidden



class BlockIPMiddleware:

    BLOCKED_IPS = ['192.168.0.1']  # List of blocked IPs



    def __init__(self, get_response):

        self.get_response = get_response



    def __call__(self, request):

        if request.META.get('REMOTE_ADDR') in self.BLOCKED_IPS:

            return HttpResponseForbidden("Your IP address is blocked.")

        return self.get_response(request)