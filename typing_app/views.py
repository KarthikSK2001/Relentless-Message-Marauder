# typing_app/views.py
from django.shortcuts import render, redirect
from .forms import TypingDataForm

import pyautogui
import time

def automate_typing(request):
    if request.method == 'POST':
        form = TypingDataForm(request.POST)
        if form.is_valid():
            form.save()
            sleep_time = form.cleaned_data['sleep_time']
            count = form.cleaned_data['count']
            text = form.cleaned_data['text']
            time.sleep(sleep_time)
            while count > 0:
                # pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('backspace')
                pyautogui.typewrite(text)
                pyautogui.press('enter')
                count -= 1
            return redirect('success')
    else:
        form = TypingDataForm()
    return render(request, 'typing_app/automate_typing.html', {'form': form})

def success(request):
    return render(request, 'typing_app/success.html')
