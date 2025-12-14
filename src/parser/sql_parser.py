def parse_sql_query(query):
    try:
        import sqlparse
    except ImportError:
        raise ImportError("Missing dependency 'sqlparse'. Install it with: pip install sqlparse")

    parsed = sqlparse.parse(query)[0]
    select_clause = None
    from_clause = None
    where_clause = None

    for token in parsed.tokens:
        if token.ttype is sqlparse.tokens.DML and token.value.upper() == 'SELECT':
            select_clause = token
        elif token.ttype is sqlparse.tokens.Keyword and token.value.upper() == 'FROM':
            from_clause = token
        elif token.ttype is sqlparse.tokens.Keyword and token.value.upper() == 'WHERE':
            where_clause = token

    return select_clause, from_clause, where_clause