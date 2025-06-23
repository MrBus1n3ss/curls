def init_config(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS all_calls(
         verb TEXT,
         uri TEXT,
         status_code INTEGER,
         headers JSONB,
         data JSONB,
         create_at TEXT)""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reduce_map(
         verb VARCHAR(10),
         uri VARCHAR(100),
         status_code INTEGER,
         headers VARCHAR(100),
         count INTEGER)""")
