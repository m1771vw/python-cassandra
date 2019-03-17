def create_table(session):
    session.execute(
        """
        CREATE TABLE dogs (
            name text,
            breed text,
            size text,
            avg_weight int,
        PRIMARY KEY (name, breed)
        );
        """
    )