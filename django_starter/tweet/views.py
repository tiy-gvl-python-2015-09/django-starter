from django.http import HttpResponse
from django.shortcuts import render, render_to_response


# Create your views here.

def index_view(request):
    context = {'count': 3, 'username': 'BarnetteME1', 'lemongrap': 'UNACCEPTABLE!!!',
               'panels': [
                   {'title': 'Barnette', 'body': 'I love making jokes',
                    'title': 'Joel', 'body': 'I love making websites',
                    'title': 'Zach', 'body': 'I love making dinner'}
                        ]}
    return render_to_response(template_name='tweets.html', context=context)


def dungeons_and_dragons_view(request):
    context = {'characters': [{'title': 'Barnette', 'body': 'Rogue Elf',
                               'title': 'Benson', 'body': 'Sorcerer Changeling',
                               'title': 'Teddy', 'body': 'Human Barbarian'}
                              ]}
    return render_to_response(template_name='dungeons_and_dragons.html', context=context)
