from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class MortgageCalculator(MDApp):
    def build(self):
        return MDLabel(text="Hello, floristry", halign="center")

MortgageCalculator().run()
