from django.http import HttpResponse
from django.shortcuts import render
from .models import Settings  # jika kamu pakai Settings model
from .forms import SettingsForm
from django.shortcuts import redirect

def edit_settings(request):
    settings_list = Settings.objects.all()

    if request.method == "POST":
        for setting in settings_list:
            new_value = request.POST.get(setting.name)
            if new_value is not None:
                setting.value = new_value
                setting.save()
        return redirect("edit_settings")

    context = {
        "settings": settings_list,
    }
    return render(request, "edit_settings.html", context)


def index(request):
    return HttpResponse("Ini adalah halaman raw/index.")

def profile(request):
    return HttpResponse("Ini adalah halaman profile.")

def contact(request):
    return HttpResponse("Ini adalah halaman contact.")

def address(request):
    return HttpResponse("Ini adalah halaman address.")

def phone(request):
    return HttpResponse("Ini adalah halaman phone.")

from .models import Question, Choice, Settings  # Pastikan sudah import Settings

def html_index(request):
    return render(request, 'polls/index.html')


def settings_view(request):
    settings_data = Settings.objects.all()
    output = "<br>".join([f"{s.name}: {s.value}" for s in settings_data])
    return HttpResponse(f"<h1>Settings:</h1><p>{output}</p>")
