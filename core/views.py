from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic import ListView
from forms import UserForm
from models import PDPlan


def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render_to_response('registration/login.html', {}, context)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()

    # Render the template depending on the context.
    context = RequestContext(request, {'user_form': user_form, 'registered': registered})
    return render_to_response('registration/register.html', context_instance=context)


@login_required
def base(request):
    context = RequestContext(request)
    return render_to_response('index.html', context_instance=context)


def profile(request):
    context = RequestContext(request)
    return render_to_response('profile.html', context_instance=context)

def logout_view(request):
    logout(request)

    return HttpResponseRedirect('registration/login.html')

class PDPlanList(ListView):
    model = PDPlan

    def get(self, request):
        plans = PDPlan.objects.all()
        return render(request, 'index.html', {'plans': plans})
