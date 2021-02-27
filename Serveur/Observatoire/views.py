
from django.shortcuts import render, redirect
from .forms import PreInscription

def accueil(request):

    if (request.method == "POST") :
        form = PreInscription(request.POST)

        if form.is_valid() :
            values = form.save(commit=False)
            values.save()
            
            return redirect('accueil')

    else :
        form = PreInscription()
        return render(request, "accueil__.html", {'form':form})

