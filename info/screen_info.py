from screeninfo import get_monitors


def screen_info():
    """
    Function based on get_monitors from screeninfo library.
     It's returns dict with screen resolution info.
    :return: dictionary with screen information
    """
    for m in get_monitors():
        spl = str(m).split('(')
        spl1 = spl[1].split(')')
        dict_ = {}
        spl2 = spl1[0].split(',')
        for el in spl2:
            res = el.split('=')
            dict_[res[0]] = res[1]

    return dict_


def screen():
    """
    Function returns font size based on screen resolution.
    :return: font size
    """
    if '1920' in screen_info().values() and '1080' in screen_info().values():
        font_size = '22'
    else:
        font_size = '50'

    return font_size
