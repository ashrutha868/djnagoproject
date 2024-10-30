from django.shortcuts import render
from .forms import FormName
from .models import Feedback

# Create your views here.
def form_name_view(request):
    form= FormName()
    profile_pic_url=None   #initialize profile picture URL

    if request.method == 'POST':
        form = FormName(request.POST, request.FILES)  #Handle file uploads
        if form.is_valid():
            #Extract cleaned data from the form
            name= form.cleaned_data['name']
            email= form.cleaned_data['email']
            feedback= form.cleaned_data['feedback']
            profile_pic= form.cleaned_data.get('profile_pic')

            #Save data to the database
            Feedback.objects.create(name=name,email=email,feedback=feedback)
           # print formatted output in the terminal
            print("\n" + "=" * 50)
            print("User Form Submission".center(50))
            print("=" * 50)
            print(f"Name: {name}")
            print(f"Email: {email}")
            print(f"Feedback: {feedback}")
            print("=" * 50 + "\n")

    return render(request, 'forms_app/form_page.html', {'form': form})







