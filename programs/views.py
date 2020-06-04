from django.shortcuts import render




def programs_index(request):
    context = {'programs_index':programs_index}
    return render(request , 'programs/programs_index.html' , context)
 
