def init_config(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS all_calls
        (id INTEGER PRIMARY KEY,
         verb varchar(10),
         uri varchar(100),
         status_code INTEGER,
         headers varchar(100),
         data JSONB)""")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reduce_map
        (id INTEGER PRIMARY KEY,
         verb VARCHAR(10),
         uri VARCHAR(100),
         status_code INTEGER,
         headers VARCHAR(100),
         count INTEGER)""")

