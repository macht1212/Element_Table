def create_table(curr):
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
