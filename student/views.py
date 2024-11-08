from django.shortcuts import render, redirect
from student.forms import StudentRegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, update_session_auth_hash
from .forms import PersonalInfoEditForm, UserProfileEditForm
from .models import UserProfile

# Create your views here.


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to the login page
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'students/register.html', {'form': form})


@login_required
def student_dashboard(request):
    return render(request, 'students/dashboard.html')

@login_required
def edit_profile(request):
    user = request.user
    profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        personal_info_form = PersonalInfoEditForm(request.POST, instance=user)
        profile_form = UserProfileEditForm(request.POST, instance=profile)

        if personal_info_form.is_valid() and profile_form.is_valid():
            personal_info_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully.')  # Success message
            return redirect('edit_profile')  # Redirect to the same page to show the message

        else:
            messages.error(request, 'Please correct the errors below.')  # Error message

    else:
        personal_info_form = PersonalInfoEditForm(instance=user)
        profile_form = UserProfileEditForm(instance=profile)

    return render(request, 'students/edit_profile.html', {
        'personal_info_form': personal_info_form,
        'profile_form': profile_form,
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        confirm_new_password = request.POST.get('confirm_new_password')

        # Check if the current password is correct
        if request.user.check_password(current_password):
            if new_password == confirm_new_password:
                request.user.set_password(new_password)
                request.user.save()
                update_session_auth_hash(request, request.user)  # Important!
                return redirect('change_password')  # Redirect to a profile view or success page
            else:
                # error_message = "New passwords do not match."
                messages.success(request, 'New passwords do not match.')  # Success message
        else:
            # error_message = "Current password is incorrect."
            messages.success(request, 'Current password is incorrect.')  # Success message
    else:
        messages.success(request, 'Your profile has been updated successfully.')  # Success message

    return render(request, 'students/change_password.html', {
        # 'error_message': error_message,
    })

@login_required
def course_list(request):
    return render(request, 'students/course_list.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')  # Redirect to user login after logout