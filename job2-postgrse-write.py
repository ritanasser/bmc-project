import psycopg

with psycopg.connect("postgres://postgres:postgres@postgres-service:5432/bmc-project") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        cur.execute(f"INSERT INTO users (name) VALUES ('{100 ** 2}')")
        cur.execute(f"SELECT * FROM users")
        conn.commit()
