from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import NewsItem, OfficerListing


# Create your views here.
def index(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('index.html', context_dict, context)


def officers(request):
    context = RequestContext(request)

    officer_listings = OfficerListing.objects.all()

    context_dict = {'officer_listings': officer_listings}

    return render_to_response('officers.html', context_dict, context)


def alumni(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('alumni.html', context_dict, context)


def our_mission(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('our_mission.html', context_dict, context)


def programs(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('programs.html', context_dict, context)


def scholarships(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('scholarships.html', context_dict, context)


def events(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('events.html', context_dict, context)


def news(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('news.html', context_dict, context)