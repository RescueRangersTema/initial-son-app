import urllib
from django.urls import reverse
from django.http import HttpResponseRedirect


def custom_redirect(url_name, *args, **kwargs):
    # https://stackoverflow.com/questions/3765887/add-request-get-variable-using-django-shortcuts-redirect
    url = reverse(url_name, args = args)
    params = urllib.parse.urlencode(kwargs)
    return HttpResponseRedirect(url + "?%s" % params)
