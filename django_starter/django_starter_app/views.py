from django.http import HttpResponse
from django.shortcuts import render, render_to_response

# Create your views here.

def index_view(request):
    context = {"name" : "Matt Kasle"}
    return render_to_response(template_name="twitter.html", context = context)