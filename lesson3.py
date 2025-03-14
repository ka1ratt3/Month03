import flet as ft
from datetime import datetime

def main(page: ft.Page):
    page.title = "Моё первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    # greeting_text = ft.Text("Привет, мир!")

    greeting_text = ft.Text(
        "Привет, мир!", 
        size=20,
        width=ft.FontWeight.BOLD,
        opacity=1, 
        animate_opacity=ft.Animation(600, 'ease_in_out'),
        # 600 = 0.6сек
        animate_scale=ft.Animation(500, 'bounce_out'),
        text_align=ft.TextAlign.CENTER
        )



    greeting_history = []

    # history_text = ft.Text("История приветствий:", style='bodyMedium')
    
    history_text = ft.Text("История приветствий:", 
                           style='bodyMedium',
                           opacity=1,
                           animate_opacity=ft.Animation(700, 'ease_in_out'))
    

    def on_button_click(e):
        name = name_input.value.strip()

        if name:
            greeting_text.value = f"Привет, {name}!"
            greeting_text.scale = 1.2
            greeting_text.opacity = 1
            greet_button.text = 'Поздороваться снова'
            greet_button.bgcolor = ft.colors.GREEN_400
            name_input.value = ''

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            greeting_history.append(f"{timestamp}: {name}")
            history_text.value = "История приветствий:\n" + "\n".join(greeting_history)
            history_text.opacity = 1
        else:
            greeting_text.value = "Пожалуйста, введите ваше имя!"

        page.update()

    name_input = ft.TextField(label="Введите ваше имя:", autofocus=True, on_submit=on_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История приветствий:"
        page.update()
    
    def toggle_theme(e):
        if page.theme_mode == ft.ThemeMode.LIGHT:
            page.theme_mode = ft.ThemeMode.DARK
        else:
            page.theme_mode = ft.ThemeMode.LIGHT

        page.update()


    theme_button = ft.IconButton(icon=ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)


    clear_button = ft.TextButton("Очистить историю", on_click=clear_history)

    clear_button_icon = ft.IconButton(icon=ft.icons.DELETE, tooltip="Очиститка", on_click=clear_history)


    # greet_button = ft.ElevatedButton("Поздороваться", on_click=on_button_click)
    greet_button = ft.ElevatedButton(
        "Поздороваться", 
        on_click=on_button_click,
        bgcolor=ft.colors.RED_600,
        animate_opacity=ft.Animation(30, 'ease_in_out')
        )


    # page.add(ft.Row([theme_button, clear_button,
    #          clear_button_icon], alignment=ft.MainAxisAlignment.CENTER), 
    #          greeting_text, 
    #          name_input, 
    #          greet_button,
    #          history_text
    # )

    page.add(
        ft.Column(
            [
                ft.Row([theme_button], alignment=ft.MainAxisAlignment.CENTER),
                greeting_text,
                name_input,
                ft.Row([greet_button, clear_button_icon], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,  
            horizontal_alignment=ft.CrossAxisAlignment.CENTER 
        ),
        history_text

    )


ft.app(target=main)
