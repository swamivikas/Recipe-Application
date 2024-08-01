from django.shortcuts import render ,redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def receipes(request):
    if request.method == 'POST':
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_descriptipn = data.get('receipe_descriptipn')
        
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_descriptipn = receipe_descriptipn,
            receipe_image  = receipe_image,
        )
        
        return redirect("/receipes/")
    
    queryset = Receipe.objects.all()
    context = {'receipes' : queryset} 
        
    return render(request, "receipes.html", context)



def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    context = {'receipe' : queryset}
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_descriptipn = data.get('receipe_descriptipn')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_descriptipn = receipe_descriptipn
        
        if receipe_image:
            queryset.receipe_image = receipe_image
            
        queryset.save()
        return redirect("/receipes/")
        
        
    return render(request, "update_recepies.html", context)
    
    
    
     
def delete_receipe(request, id):
    print(id)
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect("/receipes/")

