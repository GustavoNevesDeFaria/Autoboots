from django.shortcuts import render
from django.http import JsonResponse
from .Llama_boot import gerarResposta

# Create your views here.

def chatbot(request):
    """
    Render the chatbot page.
    """
   # return render(request, 'chatbot/chatbot.html')
    if request.method == "POST":
        user_msg = request.POST.get("message", "")
        if not user_msg:
            return JsonResponse({"error": "Mensagem vazia."}, status=400)
        answer = gerarResposta(user_msg)
        return JsonResponse({"response": answer})
    return JsonResponse({"error": "Método não suportado."}, status=405)