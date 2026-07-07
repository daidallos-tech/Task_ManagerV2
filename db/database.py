import psycopg2

def init_db(db_params: str):

    conn = psycopg2.connect(db_params)

    with conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id SERIAL PRIMARY KEY,
                    title VARCHAR(50) NOT NULL,
                    description TEXT,
                    status VARCHAR(20) DEFAULT 'In'
                );
            """)

    conn.close()