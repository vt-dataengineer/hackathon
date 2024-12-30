import os
import subprocess
from django.shortcuts import render
from django.http import JsonResponse
from .chatgpt import chat_with_gpt
import json


def index(request):
    return render(request, 'index.html')


def chat(request):
    return render(request, 'chat.html')


def generate_response(request):
    if request.method == 'POST':
        try:
            # Parse the JSON body
            data = json.loads(request.body)
            user_input = data.get('message', '')

            if not user_input:
                return JsonResponse({'error': 'Message is required.'}, status=400)

            # Generate Terraform code using ChatGPT
            try:
                response = chat_with_gpt(f"Generate Terraform code for: {user_input}")
                terraform_code = response
            except Exception as e:
                return JsonResponse({'error': f"ChatGPT API Error: {e}"}, status=500)

            # Save the Terraform code to a file
            os.makedirs('generated', exist_ok=True)
            terraform_file_path = os.path.join('generated', 'main.tf')
            with open(terraform_file_path, 'w') as f:
                f.write(terraform_code)

            # Deploy the Terraform code to AWS
            try:
                init_output = subprocess.check_output(['terraform', 'init'], cwd='generated', text=True)
                apply_output = subprocess.check_output(
                    ['terraform', 'apply', '-auto-approve'], cwd='generated', text=True
                )
                deployment_status = "Terraform code applied successfully."
            except subprocess.CalledProcessError as e:
                deployment_status = f"Error during Terraform deployment: {e.output}"

            return JsonResponse({
                'terraform_code': terraform_code,
                'deployment_status': deployment_status
            })

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)
