from info.info import colors, elements_by_properties


def bg_color(element):
    """
    Function returns BG color based on element's info
    """
    background_color = None
    if element in elements_by_properties['non_metal_elements']:
        background_color = colors['non_metal']

    elif element in elements_by_properties['alkaline_elements']:
        background_color = colors['alkaline']

    elif element in elements_by_properties['alkaline_earth_elements']:
        background_color = colors['alkaline_earth']

    elif element in elements_by_properties['noble_elements']:
        background_color = colors['noble']

    elif element in elements_by_properties['semimetals_elements']:
        background_color = colors['semimetals']

    elif element in elements_by_properties['halogens_elements']:
        background_color = colors['halogens']

    elif element in elements_by_properties['transition_elements']:
        background_color = colors['transition']

    elif element in elements_by_properties['posttransition_elements']:
        background_color = colors['posttransition']

    elif element in elements_by_properties['lanthanides_elements']:
        background_color = colors['lanthanides']

    elif element in elements_by_properties['actinides_elements']:
        background_color = colors['actinides']

    elif element in elements_by_properties['num1']:
        background_color = colors['lanthanides']

    elif element in elements_by_properties['num2']:
        background_color = colors['actinides']

    return background_color
