import psycopg2
from config import config


def insert_into(acct_type, approx_payout_date, body_length, channels, country, currency, delivery_method, description, email_domain, event_created, event_end, event_published, event_start, fb_published, gts, has_analytics, has_header, has_logo, listed, name, name_length, num_order, num_payouts, object_id, org_desc, org_facebook, org_name, org_twitter, payee_name, payout_type, previous_payouts, sale_duration, sale_duration2, show_map, ticket_types, user_age, user_created, user_type, venue_address, venue_country, venue_latitude, venue_longitude, venue_name, venue_state):
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany("INSERT INTO event_info VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                        (acct_type, approx_payout_date, body_length, channels, country, currency, delivery_method, description, email_domain, event_created, event_end, event_published, event_start, fb_published, gts, has_analytics, has_header, has_logo, listed, name, name_length, num_order, num_payouts, object_id, org_desc, org_facebook, org_name, org_twitter, payee_name, payout_type, previous_payouts, sale_duration, sale_duration2, show_map, ticket_types, user_age, user_created, user_type, venue_address, venue_country, venue_latitude, venue_longitude, venue_name, venue_state))
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    insert_into()