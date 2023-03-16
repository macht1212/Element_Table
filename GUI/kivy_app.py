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

from colors import noble, non_metal, transition, posttransition, actinides, alkaline, alkaline_earth, halogens
from colors import semimetals, other, lanthanides

Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 1300)
Config.set('graphics', 'height', 840)


font_color = [0, 0, 0, 1]


class PeriodicTableApp(App):
    def build(self):
        bl = BoxLayout(orientation='vertical')

        al = AnchorLayout(size_hint=[1, .2])

        self.lbl = Label(text='Click on Element', size=[200, 100], pos=[10, 40])

        gl = GridLayout(cols=18, rows=9, padding=[50], spacing=5, size_hint=[1, .8])

        gl.add_widget(Button(text='H', background_color=non_metal, background_normal='', color=font_color, bold=True,
                             on_press=self.on_click))
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Button(text='He', background_color=noble, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Li', background_color=alkaline, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Be', background_color=alkaline_earth, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Button(text='B', background_color=semimetals, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='C', background_color=other, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='N', background_color=other, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='O', background_color=other, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='F', background_color=halogens, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ne', background_color=noble, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))

        gl.add_widget(Button(text='Na', background_color=alkaline, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Mg', background_color=alkaline_earth, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Widget())
        gl.add_widget(Button(text='Al', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Si', background_color=semimetals, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='P', background_color=other, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='S', background_color=other, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Cl', background_color=halogens, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ar', background_color=noble, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))

        gl.add_widget(Button(text='K', background_color=alkaline, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ca', background_color=alkaline_earth, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Sc', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ti', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='V', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Cr', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Mn', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Fe', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Co', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ni', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Cu', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Zn', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ga', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ge', background_color=semimetals, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='As', background_color=semimetals, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Se', background_color=other, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Br', background_color=halogens, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Kr', background_color=noble, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))

        gl.add_widget(Button(text='Rb', background_color=alkaline, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Sr', background_color=alkaline_earth, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Y', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Zr', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Nb', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Mo', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Tc', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ru', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Rh', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Pd', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ag', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Cd', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='In', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Sn', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Sb', background_color=semimetals, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Te', background_color=semimetals, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='I', background_color=halogens, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Xe', background_color=noble, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))

        gl.add_widget(Button(text='Cs', background_color=alkaline, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ba', background_color=alkaline_earth, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Widget())
        gl.add_widget(Button(text='Hf', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ta', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='W', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Re', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Os', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ir', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Pt', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Au', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Hg', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ti', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Pb', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Bi', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Po', background_color=semimetals, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='At', background_color=halogens, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Rn', background_color=noble, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))

        gl.add_widget(Button(text='Fr', background_color=alkaline, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ra', background_color=alkaline_earth, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Widget())
        gl.add_widget(Button(text='Rf', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Db', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Sg', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Bh', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Hs', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Mt', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ds', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Rg', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Cn', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Nh', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Fl', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Mc', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Lv', background_color=posttransition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ts', background_color=halogens, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Og', background_color=noble, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))

        gl.add_widget(Widget())
        gl.add_widget(Button(text='57-71', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True))
        gl.add_widget(Button(text='La', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ce', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Pr', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Nd', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Pm', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Sm', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Eu', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Gd', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Tb', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Dy', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ho', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Er', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Tm', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Yb', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Lu', background_color=lanthanides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Widget())

        gl.add_widget(Widget())
        gl.add_widget(Button(text='89-103', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Ac', background_color=transition, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Th', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Pa', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='U', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Np', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Pu', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Am', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Cm', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Bk', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Cf', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Es', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Fm', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Md', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='No', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
        gl.add_widget(Button(text='Lr', background_color=actinides, background_normal='', color=font_color,
                             bold=True, on_press=self.on_click))
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
