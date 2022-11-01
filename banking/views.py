from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Account
from .forms import TransactionForm
import random


# Create your views here.


@login_required
def create_new_account(request):
    a = Account(balance=request.POST['balance'],
                type=request.POST['type'], user=request.user)
    a.number = f"{rn()}-{rn()}-{rn()}-{rn()}"
    a.save()
    return redirect('dashboard')


@login_required
def dashboard(request):
    context = {
        'accounts': request.user.account_set.all()
    }
    if request.user.account_set.first():
        context["account"] = request.user.account_set.first()
        if request.method == "POST":
            context["account"] = request.user.account_set.get(id=request.POST['account'])
    if 'account' in context:
        context['transactions']=context['account'].transaction_set.all()
    # breakpoint()
    return render(request, 'dashboard.html', context)


@login_required
def add_transaction(request):
    form = TransactionForm(request.POST)
    print(request.POST)
    if form.is_valid():
        transaction = form.save()
        account = request.user.account_set.get(id=request.POST['account'])
        transaction.account = account
        print(transaction)
    return redirect('dashboard')


def rn():
    return random.randrange(1000, 9999)
