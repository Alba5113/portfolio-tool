import sqlite3

skills = [ (_,) for _ in (['Python', 'SQL', 'API', 'Discord'])]
statuses = [ (_,) for _ in (['Prototip Oluşturma', 'Geliştirme Aşamasında', 'Tamamlandı, kullanıma hazır', 'Güncellendi', 'Tamamlandı, ancak bakımı yapılmadı'])]

class DB_Manager():
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        conn = sqlite3.connect(self.database)

        with conn:
                        # oluşturing al-tablo "projects"
            conn.execute("""
                    CREATE TABLE IF NOT EXISTS projects(
                        project_id INTEGER PRIMARY_KEY,
                        user_id INTEGER NOT NULL,
                        project_name TEXT NOT NULL,
                        description TEXT NOT NULL,
                        url TEXT NOT NULL,
                        status_id INTEGER,
                        FOREIGN KEY(status_id) REFERENCES status(status_id)
                             );
                    """)
            
                        # skills tablosunu oluşturma
            conn.execute('''CREATE TABLE skills (
                            skill_id INTEGER PRIMARY KEY,
                            skill_name TEXT
                        )''')

            # Bağlantı tablosu oluşturma - project_skills
            conn.execute('''CREATE TABLE project_skills (
                            project_id INTEGER,
                            skill_id INTEGER,
                            FOREIGN KEY(project_id) REFERENCES projects(project_id),
                            FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
                        )''')
            
            conn.execute('''CREATE TABLE status (
                            status_id INTEGER PRIMARY KEY,
                            status_name TEXT
                        )''')

            # Değişiklikleri kaydetme ve bağlantıyı kapatma
            conn.commit()

if __name__ == '__main__':
    manager = DB_Manager("data.db")
    manager.create_tables()