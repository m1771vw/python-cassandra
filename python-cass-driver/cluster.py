from cassandra.cluster import Cluster

cluster = Cluster()
# session = cluster.connect()
session = cluster.connect('animals')
# session.set_keyspace('animal')
# session.execute('USE animal')
rows = session.execute('SELECT * FROM monkeys')
for r in rows:
    print r.type, r.family, r.common_name 

"""
# Different ways of printing
rows = session.execute('SELECT name, age, email FROM users')
for row in rows:
    print row.name, row.age, row.email

rows = session.execute('SELECT name, age, email FROM users')
for (name, age, email) in rows:
    print name, age, email


rows = session.execute('SELECT name, age, email FROM users')
for row in rows:
    print row[0], row[1], row[2]


"""
'''
# Passing Parameters 
session.execute(
    """
    INSERT INTO users (name, credits, user_id)
    VALUES (%s, %s, %s)
    """,
    ("John O'Reilly", 42, uuid.uuid1())
)
session.execute(
    """
    INSERT INTO users (name, credits, user_id, username)
    VALUES (%(name)s, %(credits)s, %(user_id)s, %(name)s)
    """,
    {'name': "John O'Reilly", 'credits': 42, 'user_id': uuid.uuid1()}
)
'''
'''
# Async Function
query = "SELECT * FROM users WHERE user_id=%s"
future = session.execute_async(query, [user_id])

# ... do some other work

try:
    rows = future.result()
    user = rows[0]
    print user.name, user.age
except ReadTimeout:
    log.exception("Query timed out:")
-----------------------------------------
# build a list of futures
futures = []
query = "SELECT * FROM users WHERE user_id=%s"
for user_id in ids_to_fetch:
    futures.append(session.execute_async(query, [user_id])

# wait for them to complete and use the results
for future in futures:
    rows = future.result()
    print rows[0].name
'''

'''
#Consistency Level
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement

query = SimpleStatement(
    "INSERT INTO users (name, age) VALUES (%s, %s)",
    consistency_level=ConsistencyLevel.QUORUM)
session.execute(query, ('John', 42))
'''

'''
# Prepared Statement
user_lookup_stmt = session.prepare("SELECT * FROM users WHERE user_id=?")

users = []
for user_id in user_ids_to_query:
    user = session.execute(user_lookup_stmt, [user_id])
    users.append(user)
'''