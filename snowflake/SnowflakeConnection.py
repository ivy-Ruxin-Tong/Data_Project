from snowflake import connector

def sfconnect():
    cnx = connector.connect(
    account = ,
    user = ,
    password = ,
    warehouse = 'COMPUTE_WH',
    database = 'DEMO_DB',
    schema = 'Public'  
    )
    return cnx

