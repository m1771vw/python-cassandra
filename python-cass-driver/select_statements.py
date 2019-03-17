def select_all_monkeys(session):
    query = """ 
    SELECT * 
    FROM monkeys
    """
    rows = session.execute(query)
    for (type, family, common_name, avg_size_in_grams, coversation_status) in rows: 
        print type, family, common_name, avg_size_in_grams, coversation_status

def select_all_dogs(session):
    query = """
    SELECT *
    FROM dogs 
    """ 
    rows = session.execute(query)
    for(name, breed, size, avg_weight) in rows:
        print name, breed, size, avg_weight 