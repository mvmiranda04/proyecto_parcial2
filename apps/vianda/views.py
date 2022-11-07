from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.
from vianda.forms import SolicitudViandaForm


def solicitud_vianda_create(request):
    nueva_solicitud_vianda = None
    if request.method == 'POST':
        solicitud_vianda_form = SolicitudViandaForm(request.POST, request.FILES)
        if solicitud_vianda_form.is_valid():
            # Se guardan los datos que provienen del formulario en la B.D.
            nueva_solicitud_vianda = solicitud_vianda_form.save(commit=True)
            messages.success(request,
                             'Se ha agregado correctamente Una Solicitud de Vianda {}'.format(nueva_solicitud_vianda))
            return redirect(reverse('vianda:vianda_detalle', args={nueva_solicitud_vianda.id}))
    else:
        solicitud_vianda_form = SolicitudViandaForm()

    return render(request, 'vianda/vianda_form.html',
                  {'form': solicitud_vianda_form})
