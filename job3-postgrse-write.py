import psycopg

with psycopg.connect("postgres://postgres:postgres@postgres-service:5432/bmc-project") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        cur.execute(f"INSERT INTO mails (email) VALUES ('welcome')")
        conn.commit()
