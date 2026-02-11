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
   {"id": 1, "name": "Кроссовки abibas","quantity": 30},
   {"id": 2, "name": "Куртка кожаная","quantity": 20},
   {"id": 3, "name": "Coca-cola 1 литр","quantity": 0},
   {"id": 4, "name": "Картофель фри","quantity": 100},
   {"id": 5, "name": "Кепка","quantity": 25},
]

   
def item_view(reguest, id):
    for item in items:
        if item["id"] == id:
            result = f"""
            <h1> Имя: {item["name"]} </h1>
            <p> Количество: {item["quantity"]} </p>
            """
            return HttpResponse(result)
        else:
            return HttpResponse(f"Товар с id={id} не найден")

def items_view(request):
    html_list = "<ol>"
    for item in items:
        html_list += f'<li><a href="/items/{item["id"]}/">{item["name"]}</a></li>'
    html_list += "</ol>"
    return HttpResponse(html_list)

def item_detail_view(request, item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item:
        text = f"""
        <h1>{item['name']}</h1>
        <p> Количество: {item["quantity"]} </p>
        <a href='/items/'>← Назад к списку товаров</a>
        """
        return HttpResponse(text)
    else:
        text = """
        <h1>Товар не найден</h1>
        <p> Количество: {item["quantity"]} </p>
        <a href='/items/'>← Назад к списку товаров</a>
        """
        return HttpResponse(text, status=404)