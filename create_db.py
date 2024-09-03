from cs50 import SQL

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

# Create the birthdays table
db.execute("""
CREATE TABLE IF NOT EXISTS birthdays (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    month INTEGER NOT NULL,
    day INTEGER NOT NULL
);
""")

print("Database and table created successfully.")
