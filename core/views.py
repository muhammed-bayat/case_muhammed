from django.shortcuts import render
from .models import Post
from django.utils.translation import gettext as _

from django.utils.translation import ugettext as _
from django.utils import translation
from django.utils.translation import get_language,activate,gettext


def token_view(request):
    posts = Post.objects.all().order_by('-id')
   
    return render(request, 'control_token.html', {'posts':posts})

#değer kontrolü için ise
print(_("hello"))

def create_form_view(request):
    if request.POST.get('action') == 'create-form':
        title = request.POST.get('title')
        description = request.POST.get('description')
        link = request.POST.get('link')
        mail = request.POST.get('mail')
        image = request.FILES.get('image') # request.FILES used for to get files

        Post.objects.create(
            title=title,
            description=description,
            link=link,
            mail=mail,
            image=image
        )
    trans= translate(language='tr')
    return render(request, 'create-form.html',{'trans':trans})


def translate(language):
    current_language = get_language()
    try:
        activate(language)
        text = gettext('hello')
    finally:
        activate(current_language)
        
    return text