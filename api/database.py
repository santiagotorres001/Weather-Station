'''
Dev: Santiago Torres
Script Description: weather-station Database
Engine: SQLite3
Date: 09/09/2024 
'''

#Import engine database package
import sqlite3

#Create weather-station database connection
con = sqlite3.connect('weather_station.db')

#Create cursor
cur = con.cursor()

#Users model
users_model = '''
    CREATE TABLE IF NOT EXISTS users
    (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        role TEXT NOT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        update_at TIMESTAMP DEFAULT (datetime('now','localtime')),
        deleted_at NULL
    )
'''

#Execute Query
cur.execute(users_model)

#Close connection
con.close()
