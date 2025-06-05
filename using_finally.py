import sqlite3

conn = None
try:
    conn = sqlite3.connect('toast.db')
    cursor = conn.cursor()
except Exception as err:
    raise err
    # print(type(err), err)
    # exit()
else:
    data = cursor.execute('select 1').fetchall()
finally:
    if conn:
        conn.close()