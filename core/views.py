from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from forms import UserForm, PDPlanForm, ActionItemFormSet
from models import PDPlan, ActionItem


class PDPlanCreateView(CreateView):
    template_name = 'pdplan_add.html'
    model = PDPlan
    form_class = PDPlanForm
    success_url = '/list/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        actionitem_form = ActionItemFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
                                  actionitem_form=actionitem_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        actionitem_form = ActionItemFormSet(self.request.POST)
        if form.is_valid() and actionitem_form.is_valid():
            return self.form_valid(form, actionitem_form)
        else:
            return self.form_invalid(form, actionitem_form)

    def form_valid(self, form, actionitem_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        actionitem_form.instance = self.object
        actionitem_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, actionitem_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  actionitem_form=actionitem_form))


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
    all_plans = PDPlan.objects.all()

    context = RequestContext(request, {'plans': all_plans})
    return render_to_response('index.html', context_instance=context)

def profile(request):
    form = UserForm()
    context = RequestContext(request, {'user_form': form})
    return render_to_response('profile.html', context_instance=context)


def logout_view(request):
    logout(request)

    return HttpResponseRedirect('registration/login.html')


class PDPlanList(ListView):
    model = PDPlan

    def get(self, request):
        plans = PDPlan.objects.filter(user = request.user)
        return render(request, 'index.html', {'plans': plans})

class PDPlanDetailView(DetailView):
    model = PDPlan
    template_name = 'plan_view.html'
    context_object_name = 'plan'


    def get_context_data(self, **kwargs):
        context = super(PDPlanDetailView, self).get_context_data(**kwargs)
        return context

from django.forms.formsets import formset_factory

class PDPlanClone(UpdateView):
    #PDPlan.objects.create(user=request.user, name=toClone.name).save()
    print UpdateView.__dict__
    template_name = 'pdplan_add.html'
    model = PDPlan
    form_class = PDPlanForm
    success_url = '/list/'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        pdpToClone = PDPlan.objects.get(id=self.kwargs['plan_id'])
        actionsToClone = ActionItem.objects.filter(plan=pdpToClone)
        self.object = None
        form = PDPlanForm(instance=pdpToClone)

        actionitem_form = ActionItemFormSet()

        return self.render_to_response(
            self.get_context_data(form=form,
                                  actionitem_form=actionitem_form,
                                  clone_action=actionsToClone ))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        actionitem_form = ActionItemFormSet(self.request.POST)
        if form.is_valid() and actionitem_form.is_valid():
            return self.form_valid(form, actionitem_form)
        else:
            return self.form_invalid(form, actionitem_form)

    def form_valid(self, form, actionitem_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        actionitem_form.instance = self.object
        actionitem_form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, actionitem_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
                                  actionitem_form=actionitem_form))
