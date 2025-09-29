# Django modules
from django.shortcuts import render

def users_list(request):
    users = [
        {"full_name": "Toleutayev Alisher", "age": 20},
        {"full_name": "Tuimebaev Doszhan", "age": 19},
        {"full_name": "Yeldes Alimzhan", "age": 19},
    ]
    return render(request, 'users/users_list.html', {"users": users})
