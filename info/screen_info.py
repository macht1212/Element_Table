from screeninfo import get_monitors


def screen_info():
    for m in get_monitors():
        spl = str(m).split('(')
        spl1 = spl[1].split(')')
        dict_ = {}
        spl2 = spl1[0].split(',')
        for el in spl2:
            res = el.split('=')
            dict_[res[0]] = res[1]

    return dict_

