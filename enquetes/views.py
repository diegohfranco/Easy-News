from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from enquetes.models import Escolha, Enquete
# ...

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-data_entrada')[:5]
    return render_to_response('enquetes/enquete_list.html', {
    'latest_poll_list': latest_poll_list,
    'title': "2",
    })
    
def detail(request, enquete_id):
    p = get_object_or_404(Poll, pk=enquete_id)
    return render_to_response('enquetes/enquete_detail.html', {'enquete': p},
                              context_instance=RequestContext(request))

#def results(request, poll_id):
    #return HttpResponse("You're looking at the results of poll %s." % poll_id)
    
def results(request, enquete_id):
    p = get_object_or_404(Poll, pk=enquete_id)
    return render_to_response('enquetes/enquete_results.html', {'poll': p})

def vote(request, enquete_id):
    p = get_object_or_404(Enquete, pk=enquete_id)
    try:
        selected_escolha = p.escolha_set.get(pk=request.POST['escolha'])
    except (KeyError, Escolha.DoesNotExist):
        # Redisplay the poll voting form.
        return render_to_response('enquetes/enquete_detail.html', {
            'enquete': p,
            'error_message': "Voce nao escolheu nenhuma opcao",
        }, context_instance=RequestContext(request))
    else:
        selected_escolha.votos += 1
        selected_escolha.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        #return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))
        return HttpResponseRedirect(reverse('enquete_results', args=(p.id,)))
