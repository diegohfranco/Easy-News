from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from noticias.models import Noticia
# ...

def index(request):
    latest_noticia_list = Noticia.objects.all().order_by('-data_entrada')[:5]
    return render_to_response('noticias/noticia_ultimas.html', {
    'latest_noticia_list': latest_noticia_list,'title': "2",},
							context_instance=RequestContext(request))
    
def detail(request, noticia_id):
    p = get_object_or_404(Noticia, pk=noticia_id)
    return render_to_response('noticias/noticia_visualiza.html', {'noticia': p},
                              context_instance=RequestContext(request))
