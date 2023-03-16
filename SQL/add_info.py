def add_info(curr, AN, E, S, AM, P, D, Y, NOS):
    params = (AN, E, S, AM, P, D, Y, NOS)
    curr.execute(f'''
    INSERT INTO elements VALUES (?, ?, ?, ?, ?, ?, ?, ?);
    ''', params)