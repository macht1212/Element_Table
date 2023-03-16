def select_info(curr, Symbol):
    param = (Symbol,)
    curr.execute(f'''
    SELECT AtomicNumber, Element, Symbol, AtomicMass, Period, Discoverer, Year, NumberOfShells FROM elements
    WHERE Symbol=?;
    ''', param)
    return curr.fetchone()
