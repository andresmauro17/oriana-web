
"""
    Dashboard view
"""

# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def dashboard(request):
    """ this view renderize a tempalte to load the Dashboard component"""
    return render(request, 'dashboard/dashboard.html')