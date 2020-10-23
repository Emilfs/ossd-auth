import jwt
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        location = request.GET.get('next2') or settings.LOGIN_REDIRECT_URL
        return redirect(location)
    return render(request, 'index.html', context={
        'title': 'Index',
    })


def login(request):
    context = {'title': "Login"}
    if request.user.is_authenticated:
        location = request.GET.get('next2') or settings.LOGIN_REDIRECT_URL
        return redirect(location)
    return render(request, 'login.html', context=context)


@login_required(redirect_field_name='next2')
def logout(request):
    context = {'title': "Logout"}
    return render(request, 'logout.html', context=context)


@login_required(redirect_field_name='next2')
def oauth2_logout(request):
    auth.logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)


@api_view(('GET',))
@login_required(redirect_field_name='next2')
def profile(request):
    attributes = {}

    if request.user.social_auth.exists():
        attributes["oauth2"] = request.user.social_auth.get().extra_data

    if "attributes" in request.session:
        attributes["cas"] = request.session["attributes"]

    if not attributes:
        return Response(status=status.HTTP_204_NO_CONTENT)

    attributes['app_id'] = settings.APP_ID

    payload = jwt.encode(attributes, settings.APP_SECRET,
                         algorithm='HS256').decode('utf-8')

    # return Response(payload)
    return render(request, "message-to-frontend.html", {'payload': payload})
