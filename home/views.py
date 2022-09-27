from django.shortcuts import render
from .models import instruction, instructionImages
# Create your views here.
def home(request):

    instructions = instruction.objects.all().order_by('instruction_order').values()

    return render(request,'home.html',{
        'instructions':instructions,
        })