from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from noticias.models import Noticia
# ...

def index(request):
    latest_noticia_list = Noticia.objects.all().order_by('-data_entrada')[:5]
    return render_to_response('noticias/noticia_ultimas.html', {
    'latest_noticia_list': latest_noticia_list,
    'title': "2",
    })
    
def detail(request, noticia_id):
    p = get_object_or_404(Noticia, pk=noticia_id)
    return render_to_response('noticias/noticia_visualiza.html', {'noticia': p},
                              context_instance=RequestContext(request))

#def results(request, poll_id):
    #return HttpResponse("You're looking at the results of poll %s." % poll_id)
    
def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/poll_results.html', {'poll': p})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('polls/poll_detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        }, context_instance=RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
        return HttpResponseRedirect(reverse('poll_results', args=(p.id,)))
