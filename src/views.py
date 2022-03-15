from django.shortcuts import redirect, render
from django.views.generic import *

# Create your views here.

class Index(TemplateView):

    template_name = "src/index.html"

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_anonymous:
            print("No estas autenticado, eres un usuario anonimo")
            #return redirect("/login")

        else:
            print("Estas autenticado")
            print("Usuario ",request.user)
            print("Usuario Id ", request.user.id)
            contexto = {}
            return render(request,"src/empresa/empresa-crear.html",contexto)


        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['informacion'] = "Hola..."

        
        #print("usuario:",self.request.user)
        #print("rol:",self.request.user.rol)

        
        context['usuario'] = self.request.user
        return context
