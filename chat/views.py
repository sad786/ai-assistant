import json
from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import os
import markdown
from django.shortcuts import redirect
from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()


sys_instruct = "You are Iron Man. Your name is Jarvis"
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

@csrf_exempt
def chat(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '')

        # Call Google Gemini API
        def generate_response():
            res = client.models.generate_content_stream(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
            system_instruction=sys_instruct),
            contents=user_message)

        #     url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
        #     headers = {
        #         "Content-Type": "application/json",
        #         "Authorization": f"Bearer {settings.GOOGLE_API_KEY}"
        #     }
        #     payload = {
        #         "contents": [{"parts": [{"text": user_message}]}]
        #     }

        #     with requests.post(url, headers=headers, json=payload, stream=True) as response:
        #         for chunk in response.iter_content(chunk_size=128):
        #             yield chunk.decode('utf-8')

            #full_response = ''
            for chunk in res:
                #full_response += chunk.text
                html_response = markdown.markdown(chunk.text)
                yield html_response
        return StreamingHttpResponse(generate_response(), content_type='text/html')
    return render(request, 'chat.html')


def redirect_to_chat(request):
    return redirect('/chat/')
