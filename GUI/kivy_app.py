import sqlite3

from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label

from SQL.select_info import select_info

from info.info import font_color, non_metal, alkaline, alkaline_earth, noble, semimetals, halogens, transition
from info.info import posttransition, lanthanides, actinides

from info.info import elements, non_metal_elements, alkaline_elements, alkaline_earth_elements, noble_elements
from info.info import semimetals_elements, halogens_elements, transition_elements, posttransition_elements
from info.info import lanthanides_elements, actinides_elements, num2, num1

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 840)


class PeriodicTableApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical')

        al = AnchorLayout(size_hint=[1, .2])

        self.lbl = Label(text='Click on Element', size=[200, 100], pos=[10, 40])

        gl = GridLayout(cols=18, rows=9, padding=[50], spacing=5, size_hint=[1, .8])

        for element in elements:
            if element:
                if element in non_metal_elements:
                    gl.add_widget(Button(text=element, background_color=non_metal, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in alkaline_elements:
                    gl.add_widget(Button(text=element, background_color=alkaline, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in alkaline_earth_elements:
                    gl.add_widget(Button(text=element, background_color=alkaline_earth, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in noble_elements:
                    gl.add_widget(Button(text=element, background_color=noble, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in semimetals_elements:
                    gl.add_widget(Button(text=element, background_color=semimetals, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in halogens_elements:
                    gl.add_widget(Button(text=element, background_color=halogens, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in transition_elements:
                    gl.add_widget(Button(text=element, background_color=transition, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in posttransition_elements:
                    gl.add_widget(Button(text=element, background_color=posttransition, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in lanthanides_elements:
                    gl.add_widget(Button(text=element, background_color=lanthanides, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in actinides_elements:
                    gl.add_widget(Button(text=element, background_color=actinides, background_normal='',
                                         color=font_color, bold=True, on_press=self.on_click))
                elif element in num1:
                    gl.add_widget(Button(text=element, background_color=lanthanides, background_normal='',
                                         color=font_color, bold=True))
                elif element in num2:
                    gl.add_widget(Button(text=element, background_color=actinides, background_normal='',
                                         color=font_color, bold=True))
            else:
                gl.add_widget(Widget())

        bl.add_widget(al)
        bl.add_widget(gl)
        al.add_widget(self.lbl)

        return bl

    def on_click(self, instance):
        with sqlite3.connect('PeriodicTable.db') as db:
            curr = db.cursor()

            self.symbol = select_info(curr, Symbol=instance.text)
            self.update_label()

    def update_label(self):
        self.lbl.text = f"""
Atomic Number: {self.symbol[0]}
Element: {self.symbol[1]},
Symbol: {self.symbol[2]},
Atomic Mass: {self.symbol[3]},
Period: {self.symbol[4]},
Discoverer: {self.symbol[5]},
Year: {self.symbol[6]},
Number Of Shells: {self.symbol[7]}"""
