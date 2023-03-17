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

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 840)


font_color = [0, 0, 0, 1]

non_metal = [143 / 255, 250 / 255, 139 / 255, 1]
alkaline = [252 / 255, 77 / 255, 83 / 255, 1]
alkaline_earth = [255 / 255, 215 / 255, 157 / 255, 1]
noble = [181 / 255, 255 / 255, 255 / 255, 1]
semimetals = [193 / 255, 194 / 255, 136 / 255, 1]
halogens = [255 / 255, 255 / 255, 136 / 255, 1]
transition = [253 / 255, 176 / 255, 178 / 255, 1]
posttransition = [193 / 255, 193 / 255, 193 / 255, 1]
lanthanides = [253 / 255, 172 / 255, 255 / 255, 1]
actinides = [253 / 255, 130 / 255, 193 / 255, 1]
other = [143 / 255, 250 / 255, 139 / 255, 1]

elements = ['H', None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 'He',
            'Li', 'Be', None, None, None, None, None, None, None, None, None, None, 'B', 'C', 'N', 'O', 'F', 'Ne',
            'Na', 'Mg', None, None, None, None, None, None, None, None, None, None, 'Al', 'Si', 'P', 'S', 'Cl', 'Ar',
            'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr',
            'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb', 'Te', 'I', 'Xe',
            'Cs', 'Ba', None, 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn',
            'Fr', 'Ra', None, 'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn', 'Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og',
            None, '57-71', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
            None,
            None, '89-103', 'Ac', 'Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr',
            None]

non_metal_elements = ['H', 'C', 'N', 'O', 'P', 'S', 'Se']
alkaline_elements = ['Li', 'Na', 'K', 'Rb', 'Cs', 'Fr']
alkaline_earth_elements = ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra']
noble_elements = ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Og']
semimetals_elements = ['B', 'Si', 'Ge', 'As', 'Sb', 'Te', 'Po']
halogens_elements = ['F', 'Cl', 'Br', 'I', 'At', 'Ts']
transition_elements = ['La', 'Ac', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn',
                       'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd',
                       'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg',
                       'Rf', 'Db', 'Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn']
posttransition_elements = ['Al', 'Ga', 'In', 'Sn', 'Tl', 'Pb', 'Bi', 'Nh', 'Fl', 'Mc', 'Lv']
lanthanides_elements = ['Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu']
actinides_elements = ['Th', 'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No', 'Lr']
num1 = ['57-71']
num2 = ['89-103']


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
            self.update_lable()

    def update_lable(self):
        self.lbl.text = f"""
Atomic Number: {self.symbol[0]}
Element: {self.symbol[1]},
Symbol: {self.symbol[2]},
Atomic Mass: {self.symbol[3]},
Period: {self.symbol[4]},
Discoverer: {self.symbol[5]},
Year: {self.symbol[6]},
Number Of Shells: {self.symbol[7]}"""
