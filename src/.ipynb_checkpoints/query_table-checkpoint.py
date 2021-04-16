import psycopg2
from config import configs


def query_tables():
    commands = (
        """
        SELECT *
        FROM event_info;
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        for command in commands:
            cur.execute(command)
            
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close
            
if __name__ == '__main__':
    query_tables()