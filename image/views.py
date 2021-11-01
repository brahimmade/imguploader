from django.contrib.messages.api import success
from django.forms import models
from django.shortcuts import redirect, render
from django.views.generic import View
from .forms import SignUpForm, LoginForm, UploadPhotoForm, ProfileEditForm, ChangePasswordForm, ResetPasswordForm
from django.contrib.auth import authenticate, login, logout
from .models import Photo, Person
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

# Create your views here.


class HomeView(View):
    def get(self, request):
        photos = Photo.objects.all()
        return render(request, 'image/home.html', {'photos': photos})


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'image/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/login/')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'image/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']

            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
            return redirect('/')
        return render(request, 'image/login.html', {'form': form})


def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/login/')
    else:
        return redirect('/login/')


@method_decorator(login_required, name="dispatch")
class UploadPhotoView(View):
    def get(self, request):
        form = UploadPhotoForm()
        return render(request, 'image/upload.html', {'form': form})

    def post(self, request):
        form = UploadPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            caption = form.cleaned_data['caption']
            photo = form.cleaned_data['photo']
            desc = form.cleaned_data['desc']
            Photo(user=user, caption=caption, photo=photo, desc=desc).save()
            messages.success(request, 'Image Uploaded!')
            return redirect('/')


@method_decorator(login_required, name="dispatch")
class ViewPhoto(View):
    def get(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        return render(request, 'image/viewphoto.html', {'photo': photo})


@method_decorator(login_required, name="dispatch")
class EditPhotoView(View):
    def get(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        form = UploadPhotoForm(instance=photo)
        return render(request, 'image/editphoto.html', {'form': form, 'photo': photo})

    def post(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        form = UploadPhotoForm(
            data=request.POST, files=request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image Updated!')
        return redirect('/view/' + str(pk))


@login_required
def deletePhoto(request, pk):
    item = Photo.objects.get(pk=pk)
    item.delete()
    messages.success(request, 'Image Deleted!')
    return redirect('/')


@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    def get(self, request):
        return render(request, 'image/profile.html', {'active': 'btn-primary'})


@method_decorator(login_required, name="dispatch")
class ProfileUpdateView(View):
    def get(self, request):
        form = ProfileEditForm()
        return render(request, 'image/profileupdate.html', {'active': 'btn-primary', 'form': form})

    def post(self, request):
        form = ProfileEditForm(request.POST)
        if form.is_valid():
            user = request.user
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            gender = form.cleaned_data['gender']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']

            Person(user=user, first_name=first_name, last_name=last_name,
                   gender=gender, mobile=mobile, address=address).save()
            messages.success(request, 'Profile Updated!')

        return redirect('/profile/')


@method_decorator(login_required, name="dispatch")
class ChangePasswordView(View):
    def get(self, request):
        form = ChangePasswordForm(user=request.user)
        return render(request, 'image/passwordchange.html', {'form': form, 'active': 'btn-primary'})

    def post(self, request):
        form = ChangePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/logout/')


class ResetPasswordView(PasswordResetView):
    template_name = 'image/resetpass.html'
    form_class = ResetPasswordForm


class ResetPassDone(PasswordResetDoneView):
    template_name = 'image/resetpassdone.html'


class ResetPassConf(PasswordResetConfirmView):
    template_name = 'image/resetpassconf.html'
