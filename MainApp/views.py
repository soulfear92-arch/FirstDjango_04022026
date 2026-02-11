from django.http import HttpResponse
from .data import user_info

def home(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Kart G.V.</i>
    """
    return HttpResponse(text)

def about_view(request):
    text_lines = [f"{key}: {value}" for key, value in user_info.items()]
    text = "\n".join(text_lines)
    return HttpResponse(text, content_type="text/plain; charset=utf-8")