def select_info(curr, Symbol):
    """
    Function selects info from DB
    :param curr: cursor from connection
    :param Symbol: Element symbol
    :return: Tuple with element's info
    """
    param = (Symbol,)
    curr.execute(f'''
    SELECT AtomicNumber, Element, Symbol, AtomicMass, Period, Discoverer, Year, NumberOfShells FROM elements
    WHERE Symbol=?;
    ''', param)
    return curr.fetchone()
