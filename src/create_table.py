import psycopg2
from config import configs

def create_tables():
    commands = (
        """
        CREATE TABLE event_info (
            acct_type VARCHAR (255)
            approx_payout_date INT (64)
            body_length INT (64)
            channels INT (64)
            country VARCHAR (255)
            currency VARCHAR (255)
            delivery_method INT (64)
            description VARCHAR
            email_domain VARCHAR
            event_created INT (64)
            event_end INT (64)
            event_published INT64 
            event_start INT64
            fb_published INT64
            gts INT64
            has_analytics INT64
            has_header INT
            has_logo INT
            listed VARCHAR
            name VARCHAR
            name_length INT64
            num_order INT64
            num_payouts INT64
            object_id INT64
            org_desc VARCHAR
            org_facebook INT64
            org_name VARCHAR
            org_twitter INT64
            payee_name VARCHAR
            payout_type VARCHAR
            previous_payouts VARCHAR
            sale_duration INT64
            sale_duration2 INT64
            show_map INT64
            ticket_types VARCHAR
            user_age INT64
            user_created INT64
            user_type INT64
            venue_address VARCHAR
            venue_country VARCHAR
            venue_latitude INT64
            venue_longitude INT64
            venue_name VARCHAR
            venue_state VARCHAR
        
        )
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
    create_tables()