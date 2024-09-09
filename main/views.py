from django.shortcuts import render
from .models import ContentHtml
from .forms import RegisterForm
from telegrambot.send_tg_message import send_message_telegram
import logging


logger = logging.getLogger('main')


# Create your views here.
def main(request):
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = ContentHtml.objects.all()
        form = RegisterForm()
        object_dict = {
            'content': content,
            'form': form,
            'message': 'Ваша заявка отправлена, спасибо'
        }
        send_message_telegram(name, email, phone)
        return render(request, './main.html', object_dict)
    else:
        content = ContentHtml.objects.all()
        form = RegisterForm()
        object_dict = {
            'content': content,
            'form': form,
        }
        return render(request, './main.html', object_dict)
