from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
# dev_26
@login_required(login_url="accounts:login_user")
def payment_process(request):
    pass
