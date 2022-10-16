from django.shortcuts import render
from datetime import datetime

def vue_de_test(request):
    return render(request,"index.html", context = {"prenom":"Guillaume","date":datetime.today()})