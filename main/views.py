
import random
from datetime import datetime

from django.shortcuts import render


def home(request):
    days = [
        "Понедельник",
        "Вторник",
        "Среда",
        "Четверг",
        "Пятница",
        "Суббота",
        "Воскресенье"
    ]

    quotes = [
        "Даже самое длинное путешествие начинается с первого шага.",
        "Знание — сила.",
        "Ошибки — это часть обучения.",
        "Никогда не переставай учиться.",
        "Каждый день — новая возможность."
    ]

    current_day = days[datetime.today().weekday()]
    random_quote = random.choice(quotes)

    return render(request, "main/home.html", {
        "day": current_day,
        "quote": random_quote
    })
