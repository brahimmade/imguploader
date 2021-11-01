from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import ResetPasswordForm, SetPassForm

urlpatterns = [
    path('', views.HomeView.as_view()),
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.logoutView, name="logout"),
    path('upload/', views.UploadPhotoView.as_view(), name="upload"),
    path('view/<int:pk>', views.ViewPhoto.as_view(), name="view"),
    path('editphoto/<int:pk>', views.EditPhotoView.as_view(), name="editphoto"),
    path('deletephoto/<int:pk>', views.deletePhoto, name="deletephoto"),
    path('profile/', views.ProfileView.as_view(), name="profile"),
    path('profileupdate/', views.ProfileUpdateView.as_view(), name="profileupdate"),
    path('changepass/', views.ChangePasswordView.as_view(), name="changepass"),

    ###########Reset Password###########
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name="image/resetpass.html", form_class=ResetPasswordForm),
         name="password-reset"),
    path('password_reset_done/', auth_view.PasswordResetDoneView.as_view(template_name="image/resetpassdone.html"),
         name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name="image/resetpassconf.html", form_class=SetPassForm),
         name="password_reset_confirm"),
    path('password_reset_complete/', auth_view.PasswordResetCompleteView.as_view(template_name="image/resetpasscomplete.html"),
         name="password_reset_complete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
