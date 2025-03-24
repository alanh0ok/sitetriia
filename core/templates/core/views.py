from django.shortcuts import render

# Views para cada página
def home(request):
    return render(request, 'core/home.html')

def triia_hub(request):
    return render(request, 'core/triia_hub.html')

def branding(request):
    return render(request, 'core/branding.html')

def trafego_pago(request):
    return render(request, 'core/trafego_pago.html')

def contato(request):
    return render(request, 'core/contato.html')
