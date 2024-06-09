from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json
from .models import PhysicsTopic,PhysicsContent
import openai
from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv()
# OPENAI_API_KEY="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"
OPENAI_API_KEY="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"
# OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

client=OpenAI(
   api_key=OPENAI_API_KEY
)
def physics_chapter_view(request):
    physics_chapters=PhysicsTopic.objects.all()
    return render(request,'physics/physics.html',{'physics_chapters':physics_chapters})

def physics_chapter_detail(request,pk):
    if request.method == 'POST':
        data = json.loads(request.body)
        content = data.get('chapterContent')
        button_id = data.get('buttonID')
        # content = request.POST.get('chapterContent')
        # button_id = request.POST.get('buttonID')
        # print("Received POST request:")
        # print("Chapter Content:", content)
        # print("Button ID:", button_id)

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
        item=get_object_or_404(PhysicsContent,pk=pk)
        return render(request, 'physics/physics_detail.html', {'item':item})

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