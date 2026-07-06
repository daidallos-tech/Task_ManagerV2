import psycopg2

conn = psycopg2.connect("dbname=task_manager_db user=postgres password=YOUR_PASSWORD host=localhost")

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