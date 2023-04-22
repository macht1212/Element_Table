def add_info(curr, AN, E, S, AM, P, D, Y, NOS):
    """
    Function added information to DB
    :param curr: cursor (DB connection)
    :param AN: Atomic Number
    :param E: Element
    :param S: Symbol
    :param AM: Atomic Mass
    :param P: Period
    :param D: Discoverer
    :param Y: Discovery year
    :param NOS: Number of shields
    :return: None
    """
    params = (AN, E, S, AM, P, D, Y, NOS)
    curr.execute('''
    INSERT INTO elements VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    ''', params)
