import flet as ft
from datetime import datetime


def main(page: ft.Page):
    page.title = 'Моё первое приложение'
    page.theme_mode = ft. ThemeMode.LIGHT
    

    greeting_text = ft.Text('Hello world')

    greeting_history = []
    history_text = ft.Text('История приветсвий:', style='bodyMedium')
    

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            now = datetime.now()
            hour = now.hour   
            
            if 6 <= hour < 12:
                greeting_text.value = f'Доброе утро, {name}!'
            elif 12 <= hour < 18:
                greeting_text.value = f'Добрый день, {name}!'
            elif 18 <= hour < 24:
                greeting_text.value = f'Добрый вечер, {name}!'
            else:
                greeting_text.value = f'Доброй ночи, {name}!'

            greet_button.text = 'Поздороваться снова'
            name_input.value = ''

            timestamp = now.strftime('"%Y-%m-%d %H:%M:%S"')
            greeting_history.append(f'{timestamp}: {name}')
            history_text.value = 'История приветствий:\n' + '\n'.join(greeting_history)
            
            
            
        else:
            greeting_text.value = 'Пожалуйста, введите ваше имя'


        page.update()


    name_input = ft.TextField(label='Say you name:', on_submit=on_button_click, autofocus=True)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий"
        page.update()

    def toogle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT
            
        page.update()

    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip='Сменить тему', on_click=toogle_theme)

    clear_button = ft.TextButton('Очистить историю', on_click=clear_history)
    clear_button_icon= ft.IconButton(icon=ft.icons.DELETE, tooltip='Очистить историю', on_click=clear_history)
    greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)

    page.add(ft.Row([theme_button, clear_button,clear_button_icon], alignment=ft.MainAxisAlignment.CENTER),
             greeting_text, 
             name_input,
             greet_button,history_text,)

ft.app(target=main)