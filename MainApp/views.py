from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Kart G.V.</i>
    """
    return HttpResponse(text)

from .data import user_info

def user_info(request):
    # Формируем текст, например, через join
    text_lines = [f"{key}: {value}" for key, value in user_info.items()]
    text = "\n".join(text_lines)
    return HttpResponse(text)