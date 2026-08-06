import sqlite3

conn = sqlite3.connect("players.db")
cursor = conn.cursor()

# Fresh start
cursor.execute("DROP TABLE IF EXISTS players")

cursor.execute("""
CREATE TABLE players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    team TEXT NOT NULL,
    format TEXT NOT NULL,
    hundreds INTEGER,
    fifties INTEGER,
    runs INTEGER,
    wickets INTEGER
)
""")

players = [
    # ==================== INDIA ====================
    ("Virat Kohli", "India", "odi", 50, 72, 13848, 5),
    ("Rohit Sharma", "India", "odi", 31, 55, 10866, 9),
    ("KL Rahul", "India", "odi", 8, 24, 3000, 0),
    ("Hardik Pandya", "India", "odi", 0, 8, 1800, 85),
    ("Jasprit Bumrah", "India", "odi", 0, 0, 200, 160),
    ("Shubman Gill", "India", "odi", 7, 14, 2500, 0),
    ("Mohammed Siraj", "India", "odi", 0, 0, 80, 100),
    ("Ravindra Jadeja", "India", "odi", 0, 12, 2500, 200),
    ("Kuldeep Yadav", "India", "odi", 0, 0, 150, 150),

    ("Virat Kohli", "India", "t20", 1, 38, 4188, 4),
    ("Suryakumar Yadav", "India", "t20", 4, 20, 2650, 0),
    ("Rohit Sharma", "India", "t20", 5, 29, 3974, 1),
    ("Hardik Pandya", "India", "t20", 0, 5, 1200, 80),
    ("Jasprit Bumrah", "India", "t20", 0, 0, 60, 89),
    ("Rishabh Pant", "India", "t20", 0, 3, 1000, 0),
    ("Axar Patel", "India", "t20", 0, 1, 500, 50),

    ("Virat Kohli", "India", "test", 30, 32, 9230, 0),
    ("Rohit Sharma", "India", "test", 12, 18, 4000, 2),
    ("Ravindra Jadeja", "India", "test", 4, 20, 3500, 300),
    ("Jasprit Bumrah", "India", "test", 0, 0, 700, 210),
    ("Shubman Gill", "India", "test", 5, 10, 2000, 0),
    ("R Ashwin", "India", "test", 6, 14, 3500, 520),
    ("Mohammed Shami", "India", "test", 0, 2, 800, 240),
    ("KL Rahul", "India", "test", 8, 15, 3000, 0),

    # ==================== AUSTRALIA ====================
    ("Steve Smith", "Australia", "odi", 12, 35, 5800, 8),
    ("David Warner", "Australia", "odi", 20, 25, 6932, 0),
    ("Glenn Maxwell", "Australia", "odi", 3, 12, 3500, 60),
    ("Mitchell Starc", "Australia", "odi", 0, 0, 250, 230),
    ("Pat Cummins", "Australia", "odi", 0, 0, 537, 143),
    ("Josh Hazlewood", "Australia", "odi", 0, 0, 100, 120),
    ("Travis Head", "Australia", "odi", 6, 15, 3200, 15),
    ("Marnus Labuschagne", "Australia", "odi", 5, 10, 2500, 2),

    ("David Warner", "Australia", "t20", 1, 24, 3277, 0),
    ("Glenn Maxwell", "Australia", "t20", 4, 10, 2150, 40),
    ("Marcus Stoinis", "Australia", "t20", 0, 8, 1200, 35),
    ("Mitchell Starc", "Australia", "t20", 0, 0, 50, 80),
    ("Pat Cummins", "Australia", "t20", 0, 0, 80, 60),
    ("Travis Head", "Australia", "t20", 3, 8, 1500, 5),
    ("Josh Hazlewood", "Australia", "t20", 0, 0, 30, 50),

    ("Steve Smith", "Australia", "test", 33, 41, 10000, 20),
    ("David Warner", "Australia", "test", 26, 37, 8786, 0),
    ("Marnus Labuschagne", "Australia", "test", 15, 18, 4500, 0),
    ("Pat Cummins", "Australia", "test", 1, 15, 1897, 294),
    ("Nathan Lyon", "Australia", "test", 0, 2, 1500, 530),
    ("Mitchell Starc", "Australia", "test", 2, 8, 2200, 380),
    ("Travis Head", "Australia", "test", 7, 12, 3500, 10),
    ("Josh Hazlewood", "Australia", "test", 0, 3, 800, 280),

    # ==================== ENGLAND ====================
    ("Joe Root", "England", "odi", 20, 48, 7826, 30),
    ("Jos Buttler", "England", "odi", 12, 25, 5000, 0),
    ("Ben Stokes", "England", "odi", 5, 22, 3500, 80),
    ("Jonny Bairstow", "England", "odi", 15, 18, 4500, 0),
    ("Jofra Archer", "England", "odi", 0, 0, 200, 100),
    ("Moeen Ali", "England", "odi", 3, 10, 2000, 100),
    ("Chris Woakes", "England", "odi", 0, 5, 1500, 180),
    ("Liam Livingstone", "England", "odi", 2, 8, 1200, 30),

    ("Jos Buttler", "England", "t20", 1, 15, 2900, 0),
    ("Ben Stokes", "England", "t20", 0, 5, 800, 25),
    ("Phil Salt", "England", "t20", 2, 8, 1200, 0),
    ("Jofra Archer", "England", "t20", 0, 0, 50, 40),
    ("Adil Rashid", "England", "t20", 0, 0, 100, 110),
    ("Moeen Ali", "England", "t20", 0, 3, 800, 45),
    ("Harry Brook", "England", "t20", 1, 6, 1000, 0),

    ("Joe Root", "England", "test", 36, 66, 13542, 32),
    ("Ben Stokes", "England", "test", 13, 30, 6500, 200),
    ("Jonny Bairstow", "England", "test", 12, 22, 6000, 0),
    ("James Anderson", "England", "test", 0, 1, 1200, 700),
    ("Ollie Pope", "England", "test", 6, 12, 3000, 0),
    ("Zak Crawley", "England", "test", 5, 10, 2800, 0),
    ("Stuart Broad", "England", "test", 1, 3, 3500, 600),
    ("Chris Woakes", "England", "test", 2, 10, 2500, 150),

    # ==================== PAKISTAN ====================
    ("Babar Azam", "Pakistan", "odi", 19, 30, 5729, 0),
    ("Mohammad Rizwan", "Pakistan", "odi", 3, 18, 2500, 0),
    ("Fakhar Zaman", "Pakistan", "odi", 10, 15, 3500, 0),
    ("Shaheen Afridi", "Pakistan", "odi", 0, 0, 300, 110),
    ("Shadab Khan", "Pakistan", "odi", 0, 3, 800, 80),
    ("Haris Rauf", "Pakistan", "odi", 0, 0, 150, 80),
    ("Imam-ul-Haq", "Pakistan", "odi", 9, 18, 3000, 0),
    ("Naseem Shah", "Pakistan", "odi", 0, 0, 80, 60),

    ("Babar Azam", "Pakistan", "t20", 3, 36, 4145, 0),
    ("Mohammad Rizwan", "Pakistan", "t20", 1, 28, 4000, 0),
    ("Shaheen Afridi", "Pakistan", "t20", 0, 0, 50, 70),
    ("Shadab Khan", "Pakistan", "t20", 0, 1, 500, 45),
    ("Iftikhar Ahmed", "Pakistan", "t20", 0, 5, 1000, 15),
    ("Haris Rauf", "Pakistan", "t20", 0, 0, 40, 50),

    ("Babar Azam", "Pakistan", "test", 9, 28, 4000, 0),
    ("Mohammad Rizwan", "Pakistan", "test", 2, 12, 2000, 0),
    ("Shaheen Afridi", "Pakistan", "test", 0, 0, 400, 110),
    ("Sarfaraz Ahmed", "Pakistan", "test", 4, 15, 2800, 0),
    ("Yasir Shah", "Pakistan", "test", 0, 1, 1500, 250),
    ("Azhar Ali", "Pakistan", "test", 19, 35, 7142, 0),

    # ==================== SOUTH AFRICA ====================
    ("Quinton de Kock", "South Africa", "odi", 7, 21, 6770, 0),
    ("Temba Bavuma", "South Africa", "odi", 3, 12, 2000, 0),
    ("David Miller", "South Africa", "odi", 2, 15, 3500, 0),
    ("Kagiso Rabada", "South Africa", "odi", 0, 0, 300, 150),
    ("Heinrich Klaasen", "South Africa", "odi", 4, 10, 1800, 0),
    ("Anrich Nortje", "South Africa", "odi", 0, 0, 100, 80),
    ("Rassie van der Dussen", "South Africa", "odi", 6, 16, 2500, 0),
    ("Marco Jansen", "South Africa", "odi", 0, 2, 500, 60),

    ("Quinton de Kock", "South Africa", "t20", 1, 14, 2200, 0),
    ("David Miller", "South Africa", "t20", 0, 8, 1800, 0),
    ("Heinrich Klaasen", "South Africa", "t20", 2, 6, 1200, 0),
    ("Kagiso Rabada", "South Africa", "t20", 0, 0, 40, 55),
    ("Aiden Markram", "South Africa", "t20", 1, 10, 1500, 5),
    ("Tristan Stubbs", "South Africa", "t20", 0, 4, 800, 0),

    ("Dean Elgar", "South Africa", "test", 14, 22, 5500, 0),
    ("Aiden Markram", "South Africa", "test", 8, 15, 3500, 0),
    ("Kagiso Rabada", "South Africa", "test", 0, 3, 1000, 310),
    ("Keshav Maharaj", "South Africa", "test", 0, 3, 1200, 180),
    ("Temba Bavuma", "South Africa", "test", 5, 10, 2500, 0),
    ("Marco Jansen", "South Africa", "test", 1, 5, 800, 60),

    # ==================== NEW ZEALAND ====================
    ("Kane Williamson", "New Zealand", "odi", 15, 45, 7000, 40),
    ("Tom Latham", "New Zealand", "odi", 8, 20, 4000, 0),
    ("Trent Boult", "New Zealand", "odi", 0, 0, 200, 200),
    ("Devon Conway", "New Zealand", "odi", 5, 12, 2000, 0),
    ("Mitchell Santner", "New Zealand", "odi", 0, 5, 1500, 90),
    ("Matt Henry", "New Zealand", "odi", 0, 0, 200, 140),
    ("Daryl Mitchell", "New Zealand", "odi", 3, 10, 1800, 20),
    ("Glenn Phillips", "New Zealand", "odi", 2, 8, 1500, 5),

    ("Kane Williamson", "New Zealand", "t20", 0, 18, 2500, 0),
    ("Glenn Phillips", "New Zealand", "t20", 2, 10, 1800, 0),
    ("Finn Allen", "New Zealand", "t20", 3, 8, 1500, 0),
    ("Ish Sodhi", "New Zealand", "t20", 0, 0, 100, 70),
    ("Trent Boult", "New Zealand", "t20", 0, 0, 30, 45),
    ("Tim Southee", "New Zealand", "t20", 0, 1, 300, 60),
    ("Mitchell Santner", "New Zealand", "t20", 0, 2, 500, 40),

    ("Kane Williamson", "New Zealand", "test", 32, 35, 9470, 30),
    ("Tom Latham", "New Zealand", "test", 15, 28, 5500, 0),
    ("Trent Boult", "New Zealand", "test", 0, 2, 800, 330),
    ("Tim Southee", "New Zealand", "test", 0, 5, 2000, 380),
    ("Ross Taylor", "New Zealand", "test", 19, 37, 7683, 0),
    ("Henry Nicholls", "New Zealand", "test", 8, 18, 3000, 0),
    ("Neil Wagner", "New Zealand", "test", 0, 1, 800, 260),

    # ==================== SRI LANKA ====================
    ("Dasun Shanaka", "Sri Lanka", "odi", 2, 10, 1500, 40),
    ("Kusal Mendis", "Sri Lanka", "odi", 5, 15, 3000, 0),
    ("Wanindu Hasaranga", "Sri Lanka", "odi", 0, 3, 800, 60),
    ("Pathum Nissanka", "Sri Lanka", "odi", 8, 12, 2500, 0),
    ("Maheesh Theekshana", "Sri Lanka", "odi", 0, 0, 100, 50),
    ("Charith Asalanka", "Sri Lanka", "odi", 3, 10, 1800, 10),
    ("Dushmantha Chameera", "Sri Lanka", "odi", 0, 0, 200, 70),

    ("Wanindu Hasaranga", "Sri Lanka", "t20", 0, 2, 500, 100),
    ("Kusal Mendis", "Sri Lanka", "t20", 1, 8, 1200, 0),
    ("Pathum Nissanka", "Sri Lanka", "t20", 2, 6, 1000, 0),
    ("Dasun Shanaka", "Sri Lanka", "t20", 0, 4, 800, 25),
    ("Maheesh Theekshana", "Sri Lanka", "t20", 0, 0, 50, 40),
    ("Bhanuka Rajapaksa", "Sri Lanka", "t20", 0, 5, 700, 0),

    ("Dimuth Karunaratne", "Sri Lanka", "test", 16, 18, 6500, 0),
    ("Angelo Mathews", "Sri Lanka", "test", 15, 40, 8000, 30),
    ("Dinesh Chandimal", "Sri Lanka", "test", 15, 25, 5500, 0),
    ("Prabath Jayasuriya", "Sri Lanka", "test", 0, 0, 200, 120),
    ("Dhananjaya de Silva", "Sri Lanka", "test", 10, 18, 4500, 40),
    ("Kasun Rajitha", "Sri Lanka", "test", 0, 0, 300, 80),

    # ==================== WEST INDIES ====================
    ("Shai Hope", "West Indies", "odi", 18, 28, 5000, 0),
    ("Nicholas Pooran", "West Indies", "odi", 5, 15, 2500, 0),
    ("Jason Holder", "West Indies", "odi", 2, 10, 2200, 160),
    ("Alzarri Joseph", "West Indies", "odi", 0, 0, 200, 100),
    ("Shimron Hetmyer", "West Indies", "odi", 3, 12, 1800, 0),
    ("Rovman Powell", "West Indies", "odi", 2, 8, 1500, 20),
    ("Akeal Hosein", "West Indies", "odi", 0, 1, 500, 70),
    ("Brandon King", "West Indies", "odi", 4, 10, 2000, 0),

    ("Nicholas Pooran", "West Indies", "t20", 1, 12, 1800, 0),
    ("Rovman Powell", "West Indies", "t20", 0, 6, 1000, 10),
    ("Andre Russell", "West Indies", "t20", 0, 5, 1000, 40),
    ("Alzarri Joseph", "West Indies", "t20", 0, 0, 30, 35),
    ("Akeal Hosein", "West Indies", "t20", 0, 0, 200, 30),
    ("Kyle Mayers", "West Indies", "t20", 1, 8, 1200, 15),

    ("Kraigg Brathwaite", "West Indies", "test", 12, 25, 5500, 0),
    ("Jermaine Blackwood", "West Indies", "test", 8, 15, 3500, 0),
    ("Jason Holder", "West Indies", "test", 3, 15, 3000, 160),
    ("Kemar Roach", "West Indies", "test", 0, 3, 1200, 280),
    ("Shannon Gabriel", "West Indies", "test", 0, 1, 400, 170),
    ("Nkrumah Bonner", "West Indies", "test", 4, 8, 1500, 0),

    # ==================== BANGLADESH ====================
    ("Shakib Al Hasan", "Bangladesh", "odi", 9, 55, 7570, 317),
    ("Litton Das", "Bangladesh", "odi", 6, 18, 2500, 0),
    ("Mustafizur Rahman", "Bangladesh", "odi", 0, 0, 150, 170),
    ("Mushfiqur Rahim", "Bangladesh", "odi", 9, 45, 7500, 0),
    ("Mehidy Hasan", "Bangladesh", "odi", 0, 5, 1000, 100),
    ("Tamim Iqbal", "Bangladesh", "odi", 14, 52, 8357, 0),
    ("Mahmudullah", "Bangladesh", "odi", 4, 28, 5500, 40),
    ("Taskin Ahmed", "Bangladesh", "odi", 0, 0, 200, 90),

    ("Shakib Al Hasan", "Bangladesh", "t20", 0, 12, 2400, 140),
    ("Litton Das", "Bangladesh", "t20", 1, 10, 1500, 0),
    ("Mustafizur Rahman", "Bangladesh", "t20", 0, 0, 40, 60),
    ("Najmul Hossain Shanto", "Bangladesh", "t20", 1, 8, 1200, 0),
    ("Towhid Hridoy", "Bangladesh", "t20", 0, 6, 800, 0),
    ("Mahedi Hasan", "Bangladesh", "t20", 0, 1, 300, 30),

    ("Mominul Haque", "Bangladesh", "test", 12, 18, 4000, 0),
    ("Shakib Al Hasan", "Bangladesh", "test", 3, 25, 4500, 240),
    ("Mushfiqur Rahim", "Bangladesh", "test", 10, 28, 5500, 0),
    ("Taijul Islam", "Bangladesh", "test", 0, 2, 800, 200),
    ("Mehidy Hasan", "Bangladesh", "test", 5, 12, 2500, 170),
    ("Tamim Iqbal", "Bangladesh", "test", 10, 30, 5500, 0),

    # ==================== AFGHANISTAN ====================
    ("Rashid Khan", "Afghanistan", "odi", 0, 0, 1200, 180),
    ("Mohammad Nabi", "Afghanistan", "odi", 2, 18, 3500, 160),
    ("Rahmanullah Gurbaz", "Afghanistan", "odi", 6, 10, 1800, 0),
    ("Ibrahim Zadran", "Afghanistan", "odi", 5, 12, 2000, 0),
    ("Mujeeb Ur Rahman", "Afghanistan", "odi", 0, 0, 300, 100),
    ("Hashmatullah Shahidi", "Afghanistan", "odi", 4, 15, 2800, 0),
    ("Naveen-ul-Haq", "Afghanistan", "odi", 0, 0, 150, 60),
    ("Azmatullah Omarzai", "Afghanistan", "odi", 1, 8, 1200, 30),

    ("Rashid Khan", "Afghanistan", "t20", 0, 0, 500, 175),
    ("Mohammad Nabi", "Afghanistan", "t20", 0, 5, 1800, 80),
    ("Rahmanullah Gurbaz", "Afghanistan", "t20", 2, 10, 1500, 0),
    ("Najibullah Zadran", "Afghanistan", "t20", 0, 8, 1200, 0),
    ("Mujeeb Ur Rahman", "Afghanistan", "t20", 0, 0, 100, 50),
    ("Fazalhaq Farooqi", "Afghanistan", "t20", 0, 0, 50, 45),
    ("Gulbadin Naib", "Afghanistan", "t20", 0, 3, 700, 25),

    ("Hashmatullah Shahidi", "Afghanistan", "test", 5, 10, 2000, 0),
    ("Rahmat Shah", "Afghanistan", "test", 7, 15, 3500, 0),
    ("Rashid Khan", "Afghanistan", "test", 0, 1, 500, 40),
    ("Mohammad Nabi", "Afghanistan", "test", 2, 8, 1500, 35),
    ("Ibrahim Zadran", "Afghanistan", "test", 3, 8, 1800, 0),

    # ==================== IRELAND ====================
    ("Paul Stirling", "Ireland", "odi", 14, 30, 5500, 40),
    ("Andrew Balbirnie", "Ireland", "odi", 8, 20, 3500, 0),
    ("Joshua Little", "Ireland", "odi", 0, 0, 200, 100),
    ("Curtis Campher", "Ireland", "odi", 2, 8, 1200, 30),
    ("Lorcan Tucker", "Ireland", "odi", 3, 10, 1500, 0),
    ("Mark Adair", "Ireland", "odi", 0, 3, 800, 80),

    ("Paul Stirling", "Ireland", "t20", 1, 15, 3500, 20),
    ("Andrew Balbirnie", "Ireland", "t20", 0, 10, 2000, 0),
    ("Joshua Little", "Ireland", "t20", 0, 0, 50, 50),
    ("Gareth Delany", "Ireland", "t20", 0, 5, 800, 20),
    ("Harry Tector", "Ireland", "t20", 1, 8, 1200, 0),

    ("Andy McBrine", "Ireland", "test", 2, 8, 1500, 50),
    ("Paul Stirling", "Ireland", "test", 3, 10, 1800, 5),
    ("Mark Adair", "Ireland", "test", 1, 5, 1000, 40),

    # ==================== ZIMBABWE ====================
    ("Sikandar Raza", "Zimbabwe", "odi", 3, 20, 4000, 80),
    ("Sean Williams", "Zimbabwe", "odi", 5, 25, 5500, 40),
    ("Blessing Muzarabani", "Zimbabwe", "odi", 0, 0, 200, 90),
    ("Craig Ervine", "Zimbabwe", "odi", 4, 18, 3500, 0),
    ("Wesley Madhevere", "Zimbabwe", "odi", 1, 8, 1200, 20),
    ("Richard Ngarava", "Zimbabwe", "odi", 0, 0, 150, 60),
    ("Ryan Burl", "Zimbabwe", "odi", 2, 10, 1800, 50),

    ("Sikandar Raza", "Zimbabwe", "t20", 0, 8, 1500, 40),
    ("Sean Williams", "Zimbabwe", "t20", 0, 10, 1800, 20),
    ("Wesley Madhevere", "Zimbabwe", "t20", 0, 5, 800, 15),
    ("Luke Jongwe", "Zimbabwe", "t20", 0, 2, 500, 25),
    ("Blessing Muzarabani", "Zimbabwe", "t20", 0, 0, 30, 30),

    ("Craig Ervine", "Zimbabwe", "test", 6, 12, 3000, 0),
    ("Sean Williams", "Zimbabwe", "test", 8, 18, 4000, 20),
    ("Blessing Muzarabani", "Zimbabwe", "test", 0, 1, 300, 50),
    ("Donald Tiripano", "Zimbabwe", "test", 0, 3, 800, 40),
]

cursor.executemany(
    "INSERT INTO players (name, team, format, hundreds, fifties, runs, wickets) VALUES (?, ?, ?, ?, ?, ?, ?)",
    players
)

conn.commit()
conn.close()
print(f"Database recreated successfully with {len(players)} players from 12 teams across ODI, T20 & Test!")