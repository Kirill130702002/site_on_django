from django.shortcuts import render


def index(request):
    dictionary = {
        'title': 'Руководитель IT-проектами',
    }
    return render(request, 'main/index.html', dictionary)


def demand(request):
    dictionary = {
        'title': 'Востребованность',
    }
    return render(request, 'main/demand.html', dictionary)


def geography(request):
    dictionary = {
        'title': 'География',
    }
    return render(request, 'main/geography.html', dictionary)


def skills(request):
    dictionary = {
        'title': 'Навыки',
    }
    return render(request, 'main/skills.html', dictionary)


def recent_vacancies(request):
    dictionary = {
        'title': 'Последние вакансии',
    }
    return render(request, 'main/recent_vacancies.html', dictionary)