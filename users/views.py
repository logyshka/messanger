from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView

from users.forms import RegisterForm, LoginForm


class NoAuthRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("home"))
        return super().dispatch(request, *args, **kwargs)


class UserRegisterView(NoAuthRequiredMixin, CreateView):
    form_class = RegisterForm
    template_name = "users/register.html"
    success_url = reverse_lazy("login")


class UserLoginView(NoAuthRequiredMixin, LoginView):
    form_class = LoginForm
    template_name = "users/login.html"
    next_page = reverse_lazy("home")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")

