from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.contrib.auth import get_user_model

from users.forms import LoginForm, UserRegistrationForm

User = get_user_model()


class UserLoginView(SuccessMessageMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'
    success_message = 'You are successfully logged in'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = 'core:home-page'


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'
    success_message = 'Registration is completed. Please Login in here'


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'users/profile.html'
    login_url = 'users:login'

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        requests = self.request
        context['user'] = User.objects.filter(id=requests.user.id).first()
        return context
