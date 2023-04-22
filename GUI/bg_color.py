from info.info import non_metal_elements
from info.info import alkaline_elements, alkaline_earth_elements, \
    noble_elements
from info.info import semimetals_elements, halogens_elements
from info.info import transition_elements, posttransition_elements
from info.info import lanthanides_elements, actinides_elements, \
    num2, num1

from info.info import colors


def bg_color(element):
    """
    Function returns BG color based on element's info
    """
    background_color = None
    if element in non_metal_elements:
        background_color = colors['non_metal']

    elif element in alkaline_elements:
        background_color = colors['alkaline']

    elif element in alkaline_earth_elements:
        background_color = colors['alkaline_earth']

    elif element in noble_elements:
        background_color = colors['noble']

    elif element in semimetals_elements:
        background_color = colors['semimetals']

    elif element in halogens_elements:
        background_color = colors['halogens']

    elif element in transition_elements:
        background_color = colors['transition']

    elif element in posttransition_elements:
        background_color = colors['posttransition']

    elif element in lanthanides_elements:
        background_color = colors['lanthanides']

    elif element in actinides_elements:
        background_color = colors['actinides']

    elif element in num1:
        background_color = colors['lanthanides']

    elif element in num2:
        background_color = colors['actinides']

    return background_color
