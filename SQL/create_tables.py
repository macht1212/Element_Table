def create_table(curr):
    """
    Function creates new table in DB and drop
    tables before creation (if it necessary)
    :param curr: cursor from connection to DB
    :return: None
    """
    # curr.execute('''
    # DROP TABLE elements;
    # ''')

    curr.execute('''
    CREATE TABLE IF NOT EXISTS elements(
    AtomicNumber VARCHAR,
    Element VARCHAR,
    Symbol VARCHAR,
    AtomicMass VARCHAR,
    Period VARCHAR,
    Discoverer VARCHAR,
    Year VARCHAR,
    NumberOfShells VARCHAR
    );
    ''')
