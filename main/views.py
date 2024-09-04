from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152172',
        'name': 'Siti Shofi Nadhifa',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)