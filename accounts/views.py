from .forms import *
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def profile(request):
    template = 'account/profile.html'
    if request.method == 'POST':
        profile_form = EditProfile(request.POST,instance = request.user)
        if profile_form.is_valid():
            profile = profile_form.save()
            profile.save()
            user = request.user
            user.updated_at = datetime.now()
            user.save()
            messages.success(
                request, f' ' + profile.name + ' Your Profile Updated Successfully!'
            )
            return redirect('/') 
    else:
        profile_form = EditProfile(instance = request.user)
    
    context = {
        'profile_form' : profile_form
    }

    return render(request,template,context)