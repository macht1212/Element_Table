from info.info import colors, elements_by_properties


def bg_color(element):
    """
    Function returns BG color based on element's info
    """
    background_color = {
        element: colors['non_metal'],
        **{e: colors['alkaline'] for e in elements_by_properties['alkaline_elements']},
        **{e: colors['alkaline_earth'] for e in elements_by_properties['alkaline_earth_elements']},
        **{e: colors['noble'] for e in elements_by_properties['noble_elements']},
        **{e: colors['semimetals'] for e in elements_by_properties['semimetals_elements']},
        **{e: colors['halogens'] for e in elements_by_properties['halogens_elements']},
        **{e: colors['transition'] for e in elements_by_properties['transition_elements']},
        **{e: colors['posttransition'] for e in elements_by_properties['posttransition_elements']},
        **{e: colors['lanthanides'] for e in elements_by_properties['lanthanides_elements']},
        **{e: colors['actinides'] for e in elements_by_properties['actinides_elements']},
        **{e: colors['lanthanides'] for e in elements_by_properties['num1']},
        **{e: colors['actinides'] for e in elements_by_properties['num2']}
    }.get(element, None)

    return background_color
