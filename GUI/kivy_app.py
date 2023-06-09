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

from info.info import font_color

from info.info import elements
from info.screen_info import screen

from GUI.bg_color import bg_color

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 840)

font = 'Arial'
bold = True


class PeriodicTableApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical')

        al = AnchorLayout(size_hint=[1, .2])

        gl2 = GridLayout(cols=6, rows=3, padding=[50], spacing=5)

        self.lbl1 = Label(text='Element:', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl2 = Label(text=' ', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl3 = Label(text='Atomic Mass:', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl4 = Label(text=' ', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl5 = Label(text='Discoverer:', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl6 = Label(text=' ', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl7 = Label(text='Symbol:', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl8 = Label(text=' ', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl9 = Label(text='Period:', font_family=font,
                          bold=bold, font_size=screen())

        self.lbl10 = Label(text=' ', font_family=font,
                           bold=bold, font_size=screen())

        self.lbl11 = Label(text='Year:', font_family=font,
                           bold=bold, font_size=screen())

        self.lbl12 = Label(text=' ', font_family=font,
                           bold=bold, font_size=screen())

        self.lbl13 = Label(text='Atomic Number:', font_family=font,
                           bold=bold, font_size=screen())

        self.lbl14 = Label(text=' ', font_family=font,
                           bold=bold, font_size=screen())

        self.lbl15 = Label(text='Number Of Shells:', font_family=font,
                           bold=bold, font_size=screen())

        self.lbl16 = Label(text=' ', font_family=font,
                           bold=bold, font_size=screen())

        gl2.add_widget(self.lbl1)
        gl2.add_widget(self.lbl2)
        gl2.add_widget(self.lbl3)
        gl2.add_widget(self.lbl4)
        gl2.add_widget(self.lbl5)
        gl2.add_widget(self.lbl6)
        gl2.add_widget(self.lbl7)
        gl2.add_widget(self.lbl8)
        gl2.add_widget(self.lbl9)
        gl2.add_widget(self.lbl10)
        gl2.add_widget(self.lbl11)
        gl2.add_widget(self.lbl12)
        gl2.add_widget(self.lbl13)
        gl2.add_widget(self.lbl14)
        gl2.add_widget(self.lbl15)
        gl2.add_widget(self.lbl16)

        gl = GridLayout(cols=18,
                        rows=9,
                        padding=[50],
                        spacing=5,
                        size_hint=[1, .8])

        for element in elements:
            if element:

                gl.add_widget(Button(text=element,
                                     background_color=bg_color(element),
                                     background_normal='',
                                     color=font_color,
                                     bold=True,
                                     on_press=self.on_click))

            else:
                gl.add_widget(Widget())

        bl.add_widget(al)
        bl.add_widget(gl)
        al.add_widget(gl2)

        return bl

    def on_click(self, instance):
        """
        Function returns information about element.
        :param instance:
        :return: label update after click
        """
        with sqlite3.connect('PeriodicTable.db') as db:
            curr = db.cursor()

            self.symbol = select_info(curr, Symbol=instance.text)
            self.update_label()

    def update_label(self):
        """
        Function returns information about element from SQLite
        :return: information from DB to labels
        """
        self.lbl2.text = self.symbol[1]  # Element
        self.lbl4.text = self.symbol[3]  # AM
        self.lbl6.text = self.symbol[5]  # D
        self.lbl8.text = self.symbol[2]  # S
        self.lbl10.text = self.symbol[4]  # P
        self.lbl12.text = self.symbol[6]  # Y
        self.lbl14.text = self.symbol[0]  # AN
        self.lbl16.text = self.symbol[7]  # NOS
