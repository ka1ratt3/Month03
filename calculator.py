import flet as ft


class CalcButton(ft.ElevatedButton):
    def __init__(self, text, button_clicked, expand=1):
        super().__init__()
        self.text = text
        self.expand = expand
        self.on_click = button_clicked
        self.data = text
        self.height = 70
        self.width = 70
        self.text_size = 24
        self.animate_scale = ft.animation.Animation(200, "ease_in_out")


class DigitButton(CalcButton):
    def __init__(self, text, button_clicked, expand=1):
        CalcButton.__init__(self, text, button_clicked, expand)
        self.bgcolor = ft.colors.BLUE_GREY_800
        self.color = ft.colors.WHITE


class ActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.AMBER_600
        self.color = ft.colors.BLACK


class ExtraActionButton(CalcButton):
    def __init__(self, text, button_clicked):
        CalcButton.__init__(self, text, button_clicked)
        self.bgcolor = ft.colors.GREY_600
        self.color = ft.colors.WHITE


class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()
        self.reset()

        self.result = ft.Text(value="0", color=ft.colors.WHITE, size=40, weight=ft.FontWeight.BOLD)
        self.bgcolor = ft.colors.BLACK
        self.border_radius = ft.border_radius.all(20)
        self.padding = 10
        self.content = ft.Column(
            alignment="center",
            spacing=10,
            controls=[
                ft.Row(controls=[self.result], alignment="end"),
                ft.Row(
                    controls=[
                        ExtraActionButton(text="AC", button_clicked=self.button_clicked),
                        ExtraActionButton(text="+/-", button_clicked=self.button_clicked),
                        ExtraActionButton(text="%", button_clicked=self.button_clicked),
                        ActionButton(text="/", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="7", button_clicked=self.button_clicked),
                        DigitButton(text="8", button_clicked=self.button_clicked),
                        DigitButton(text="9", button_clicked=self.button_clicked),
                        ActionButton(text="*", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="4", button_clicked=self.button_clicked),
                        DigitButton(text="5", button_clicked=self.button_clicked),
                        DigitButton(text="6", button_clicked=self.button_clicked),
                        ActionButton(text="-", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="1", button_clicked=self.button_clicked),
                        DigitButton(text="2", button_clicked=self.button_clicked),
                        DigitButton(text="3", button_clicked=self.button_clicked),
                        ActionButton(text="+", button_clicked=self.button_clicked),
                    ]
                ),
                ft.Row(
                    controls=[
                        DigitButton(text="0", expand=2, button_clicked=self.button_clicked),
                        DigitButton(text=".", button_clicked=self.button_clicked),
                        ActionButton(text="=", button_clicked=self.button_clicked),
                    ]
                ),
            ]
        )

    def button_clicked(self, e):
        data = e.control.data
        if self.result.value == "Error" or data == "AC":
            self.result.value = "0"
            self.reset()

        elif data in "0123456789.":
            if self.result.value == "0" or self.new_operand:
                self.result.value = data
                self.new_operand = False
            else:
                self.result.value += data

        elif data in "+-*/":
            self.result.value = self.calculate(self.operand1, float(self.result.value), self.operator)
            self.operator = data
            self.operand1 = float(self.result.value) if self.result.value != "Error" else 0
            self.new_operand = True

        elif data == "=":
            self.result.value = self.calculate(self.operand1, float(self.result.value), self.operator)
            self.reset()

        elif data == "%":
            self.result.value = str(float(self.result.value) / 100)
            self.reset()

        elif data == "+/-":
            self.result.value = str(-float(self.result.value))

        self.update()

    def calculate(self, operand1, operand2, operator):
        try:
            return str({
                "+": operand1 + operand2,
                "-": operand1 - operand2,
                "*": operand1 * operand2,
                "/": "Error" if operand2 == 0 else round(operand1 / operand2, 8)
            }[operator])
        except:
            return "Error"

    def reset(self):
        self.operator = "+"
        self.operand1 = 0
        self.new_operand = True


def main(page: ft.Page):
    page.title = "Advanced Calculator"
    page.window_width = 350
    page.window_height = 500
    page.window_resizable = False
    page.bgcolor = ft.colors.BLACK
    calc = CalculatorApp()
    page.add(calc)


ft.app(target=main)
