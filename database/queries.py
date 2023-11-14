CREATE_TASK_TABLE = """
CREATE TABLE IF NOT EXISTS task_tables(
    task_id SERIAL PRIMARY KEY,
    task_name VARCHAR(50),
    end_date DATE,
    status INTEGER
);
"""

INSERT_TASK="INSERT INTO task_tables( task_name, end_date, status ) VALUES(%s, %s, %s)"
SELECT_ALL_TASK="SELECT * FROM task_tables"
