# Django modules
from django.shortcuts import redirect, render

cnt_value = 0

def cnt_view(request):
    global cnt_value
    return render(request, "cnt/index.html", {"counter": cnt_value})

def increment(request):
    global cnt_value
    cnt_value += 1
    return redirect("cnt_view")

def reset(request):
    global cnt_value
    cnt_value = 0
    return redirect("cnt_view")