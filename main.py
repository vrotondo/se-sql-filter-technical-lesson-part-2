import sqlite3
import pandas as pd

conn = sqlite3.connect('pets_database.db')
cursor = conn.cursor()
cats_data = pd.read_sql("SELECT * FROM cats;", conn)
print(cats_data)

# Step 1
'''
pd.read_sql("""
SELECT *
    FROM cats
WHERE age >= 5;
""", conn)
'''

# Step 2
'''
pd.read_sql("""
SELECT *
  FROM cats
 WHERE age BETWEEN 1 AND 3;
""", conn)
'''

# Step 3
'''
pd.read_sql("""
SELECT *
  FROM cats
WHERE owner_id IS NULL;
""", conn)
'''

# Step 4
'''
pd.read_sql("""
SELECT *
  FROM cats
 WHERE substr(name, 1, 1) = "M";
""", conn)

pd.read_sql("""
SELECT *
  FROM cats
 WHERE name LIKE '_a__';
""", conn)

pd.read_sql("""
SELECT *
  FROM cats
 WHERE length(name) = 4 AND substr(name, 2, 1) = "a";
""", conn)
'''

# Step 5
'''
pd.read_sql("""
SELECT COUNT(owner_id)
  FROM cats
 WHERE owner_id = 1;
""", conn)
'''

conn.close()