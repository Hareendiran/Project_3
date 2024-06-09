from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse,HttpResponse
import json
from .models import CustomTopic
import openai
from openai import OpenAI
from .forms import CustomContentForm
from dotenv import load_dotenv
load_dotenv()
import os


OPENAI_API_KEY="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"
client=OpenAI(
    api_key=OPENAI_API_KEY
)
# def custom_content_view(request):
#     if request.method == 'POST':
#         content=request.POST['custom-cont']

#         c=CustomTopic(content=content)
#         c.save()

#     custom_content=CustomTopic.objects.all()
#     return render(request,'custom/trial.html',{'custom_content':custom_content})
# def custom_content_view(request):
#     if request.method == 'POST':
#         form = CustomContentForm(request.POST)  # Bind form data to CustomContentForm

#         if form.is_valid():
#             form.save()  # Save form data to the database
#             # Optionally, you can provide feedback to the user after successful submission
#             return HttpResponse("Custom content submitted successfully!")

#     else:
#         form = CustomContentForm()  # Create an empty form instance

#     custom_content = CustomTopic.objects.all()
#     return render(request, 'custom/trial.html', {'form': form, 'custom_content': custom_content})

def custom_content_view(request):
    if request.method == 'POST':
        data=json.loads(request.body)
        content=data.get('chapterContent')
        button_id=data.get('buttonID')

        processed_data = button_id
        if button_id == 'simpler explanation':
            processed_data = ask_openai(button=button_id,message=content)
        elif button_id == "extra information":
            processed_data = ask_openai(button=button_id,message=content)
        elif button_id == "5 question and answers with answers at the end. Make sure the questions are seperated by a line ":
            processed_data = ask_openai(button=button_id,message=content)
        processed_data = processed_data.replace('\n', '<br/>')

        return HttpResponse(processed_data, content_type='text/plain')
    else:
        return render(request,'custom/trial.html')

def ask_openai(button,message):
    response=client.chat.completions.create(
        messages=[
            {"role":"system", "content": f"You are a teacher who's job is to help students based on personalised learning. You will be given the text to teach and the query they have"},
            {"role":"user","content":message},
            {"role":"system","content":f"Explain the content with {button}"}
        ],
        model="gpt-3.5-turbo",
    )
    answer=response.choices[0].message.content.strip()
    return answer
