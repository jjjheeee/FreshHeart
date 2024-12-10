# # views.py
from rest_framework.views import APIView
from rest_framework.response import Response
import os
from huggingface_hub import InferenceClient


class AlphaInstructView(APIView):

    def post(self, request):
        hugging_token = os.getenv('HUGGINGFACE_TOKEN')
        llm_model_id = os.getenv('LLM_MODEL_ID')
        
        client = InferenceClient(api_key=hugging_token)
        user_input = request.data.get('input')
        messages = [
            {
                "role": "user",
                "content": user_input
            }
        ]

        completion = client.chat.completions.create(
            model=llm_model_id, 
            messages=messages, 
            max_tokens=500
        )

        return Response({"response": completion.choices[0].message.content})
        

