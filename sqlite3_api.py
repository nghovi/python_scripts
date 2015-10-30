#!/usr/bin/python

"""This is database management file for task
"""
import sqlite3
import time
import datetime

def dict_factory(cursor, row):
    """Use this function as a row_factory

    This allow fetch a row as a dictionary
    Code from https://docs.python.org/2/library/sqlite3.html#sqlite3.Row
    """
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def query(db_name, query_str, is_commit=True, data=''):
    db_connection = sqlite3.connect(db_name)
    db_connection.row_factory = dict_factory #sqlite3.Row: return list
    cursor = db_connection.cursor()
    print "cursor is"
    print cursor
    cursor.execute(query_str,data)
    rows = cursor.fetchall()
    if is_commit:
        db_connection.commit()
    db_connection.close()
    return rows

def select(db_name, query_str):
    return query(db_name, query_str, is_commit=False)

def create_table(db_name, query_str):
    return query(db_name, query_str, is_commit=True)

def update(db_name, query_str, data=''):
    return query(db_name, query_str, is_commit=True, data=data)

def insert(db_name, query_str, data=''):
    return query(db_name, query_str, is_commit=True, data=data)

def insert_many(db_name, query_str, data):
    db_connection = sqlite3.connect(db_name)
    cursor = db_connection.cursor()
    cursor.executemany(query_str, data)
    db_connection.commit()
    num_row_changed = db_connection.total_changes
    db_connection.close()
    return num_row_changed

if __name__ == '__main__':
    query_str = '''create table task(
        id integer PRIMARY KEY AUTOINCREMENT,
        type int,
        brief text,
        description text,
        status int,
        rate real,
        start_date datetime,
        end_date datetime)'''
    sample_task = [
                    (1,
                    "Improve task management",
                    "Whenever get spare times, or afraid of zero-day, imporve or refactor it",
                    0,
                    0,
                    time.strftime("%d/%m/%Y %H:%M:%S"),
                    "12/03/2090 23:59:59")
                ]
    create_table(db_name='task.db', query_str=query_str)
    num_row_changed = insert_many(db_name='task.db',
            query_str="insert into task(type, brief, description, status, rate, start_date, end_date) values (?, ?, ?, ?, ?, ?, ?)",
            data = sample_task)
    print "Inserted ", num_row_changed
    for row in select('task.db', 'select * from task'):
        for k, v in row.iteritems():
            print k, ': ', v