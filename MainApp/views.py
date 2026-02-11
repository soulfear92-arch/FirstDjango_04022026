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

items = [
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]

def item_view(request, id):
    product = next((item for item in items if item["id"] == id), None)
    if product:
        return HttpResponse(product["name"])
    else:
        return HttpResponse(f"Товар с id={id} не найден")
    
def items_view(request):
    html_list = "<ol>"
    for item in items:
        html_list += f"<li>{item['name']}</li>"
    html_list += "</ol>"
    return HttpResponse(html_list)