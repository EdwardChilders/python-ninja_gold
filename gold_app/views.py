from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    # gold = 0
    if 'gold' not in request.session:
        request.session['gold'] = 0
    return render(request, 'index.html')
    

def money(request):
    if 'my_list' not in request.session:
        request.session['my_list'] = []
    # print(request.POST)
    if 'farm' in request.POST:
        num1 = random.randint(10, 20) 
        request.session['gold'] += num1
        # print(request.session['gold'])
        request.session['my_list'].append(f"you gained {num1} gold")
    if 'cave' in request.POST:
        num2 = random.randint(5, 10) 
        request.session['gold'] += num2
        # print(request.session['gold'])
        request.session['my_list'].append(f"you gained {num2} gold")
    if 'house' in request.POST:
        num3 = random.randint(2, 5) 
        request.session['gold'] += num3
        # print(request.session['gold'])
        request.session['my_list'].append(f"you gained {num3} gold")
    if 'casino' in request.POST:
        num4 = random.randint(-50, 50) 
        request.session['gold'] += num4
        # print(request.session['gold'])
        if num4 >= 0:
          request.session['my_list'].append(f"you gained {num4} gold")
        elif num4 < 0:
          request.session['my_list'].append(f"you lost {num4} gold")
    request.session.save()
    return redirect('/')

def refresh(request):
    request.session['my_list'] = []
    request.session['gold'] = 0
    return redirect('/')