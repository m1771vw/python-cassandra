from cassandra.cluster import Cluster

from select_statements import * 
from insert_statements import *
from create_statements import create_table
if __name__ == "__main__":
    print("Hello World")

    cluster = Cluster(['localhost', '127.0.0.1'])
    session = cluster.connect('animals')
    # create_table(session)
    for x in range(0, 100):
        print("====Inserting Dog====")
        insert_dog(session, generate_name(), generate_breed(), generate_size(),  generate_avg_weight())
    print("====Dogs====")
    select_all_dogs(session)
    # insert(session)