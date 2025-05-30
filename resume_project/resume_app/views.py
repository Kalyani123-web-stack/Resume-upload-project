from django.shortcuts import render,redirect
from .forms import ResumeForm
from .models import Resume

# Create your views here.
def upload_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_list')  # Redirect after upload
    else:
        form = ResumeForm()
    return render(request, 'resume_app/upload_resume.html', {'form': form})

def resume_list(request):
    resumes = Resume.objects.all()
    return render(request, 'resume_app/resume_list.html', {'resumes': resumes})