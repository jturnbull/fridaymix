from datetime import date, datetime, timedelta
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseServerError
from django.shortcuts import get_object_or_404, render_to_response
from django.template import  RequestContext
import re
from models import *


def home(request, extra_context=None):
    
    context = RequestContext(request)
    
    if extra_context:
        context.update(extra_context)
        
    mixes = Mix.objects.all()

    track_count = Track.objects.all().count()

    total_length = 0
    for mix in mixes:
        if mix.length:
            total_length += mix.length
        
    context.update({
        'mixes': mixes,
        'track_count': track_count,
        'total_length': datetime.timedelta(seconds=int(total_length))
    })
        
    return render_to_response('home.html', context)
    
def mix(request, slug, extra_context=None):
    context = RequestContext(request)
    
    if extra_context:
        context.update(extra_context)
        
    mix = get_object_or_404(Mix, slug=slug)
    tracks = mix.tracks.all().order_by('mixtrack__mixtrack_number')
    
    context.update({
        'mix': mix,
        'tracks': tracks,
    })
        
    return render_to_response('mix.html', context)
    
def tracks(request, extra_context=None):
    context = RequestContext(request)
    
    if extra_context:
        context.update(extra_context)
        
    tracks = Track.objects.all().order_by('name')
    
    context.update({
        'tracks': tracks,
    })
        
    return render_to_response('tracks.html', context)

