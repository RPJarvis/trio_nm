
from django.template import RequestContext
from .models import NewsItem, AchieverProfile, CalendarEvent, OfficerListing, ScholarshipListing
from django.shortcuts import render_to_response, get_object_or_404, render


# Create your views here.
def index(request):
    context = RequestContext(request)

    latest_news_item = NewsItem.objects.latest('publish_date')
    calendar = CalendarEvent.objects.all()

    context_dict = {'latest_news_item': latest_news_item, 'calendar': calendar}

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

    scholarships = ScholarshipListing.objects.all()

    context_dict = {'scholarships': scholarships}

    return render_to_response('scholarships.html', context_dict, context)


def achiever(request):
    context = RequestContext(request)

    achievers = AchieverProfile.objects.all().order_by('-optional_posting_date')

    context_dict = {'achievers': achievers}

    return render(request, 'achiever.html', context_dict)


def events(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('events.html', context_dict, context)


def news(request):
    context = RequestContext(request)

    context_dict = {}

    return render_to_response('news.html', context_dict, context)


def fair_share(request):
    context = RequestContext(request)

    context_dict = {}

    return render(request, 'fair_share.html', context_dict)


def committee(request):
    context = RequestContext(request)

    context_dict = {}

    return render(request, 'committee.html', context_dict)


def bylaws(request):
    context = RequestContext(request)

    context_dict = {}

    return render(request, 'bylaws.html', context_dict)


def membership(request):
    context = RequestContext(request)

    context_dict = {}

    return render(request, 'membership.html', context_dict)

def event_post(request, slug):
    post = get_object_or_404(CalendarEvent, slug=slug)
    context_dict = {'post': post}

    return render(request, 'event_post.html', context_dict)

