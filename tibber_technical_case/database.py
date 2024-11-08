from psycopg2.extras import DictCursor


def save_execution(commands_count, result, duration, conn):
    with conn.cursor(cursor_factory=DictCursor) as cursor:
        cursor.execute("insert into executions(commands, result, duration) values(%s, %s, %s) returning *",
                       (commands_count, result, duration))
        execution = cursor.fetchone()
    conn.commit()

    return execution
