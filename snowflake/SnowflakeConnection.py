from snowflake import connector

def sfconnect():
    cnx = connector.connect(
    account = 'jp81237.us-central1.gcp',
    user = 'ivytong',
    password = 'Seattlenewlife!12',
    warehouse = 'COMPUTE_WH',
    database = 'DEMO_DB',
    schema = 'Public'  
    )
    return cnx

