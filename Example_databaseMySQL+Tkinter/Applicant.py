import mysql.connector

class Applicant():

    def __init__(self, host, user, password, database):
        self.mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    # знаходить пошти та паролі вступників з бази данних

    def fetch_applicants(self):
        mycursor = self.mydb.cursor()

        applicants_query = "SELECT applicant_email, applicant_password FROM abikpi.applicants;"

        mycursor.execute(applicants_query)

        result = mycursor.fetchall()

        mycursor.close()
        return result

    # внесення нового користувача до бази данних

    def registration_applicants(self, name, gender, quota, email, password):
        # Створення курсора для виконання SQL-запитів
        mycursor = self.mydb.cursor()

        # Запит для отримання максимального applicant_id з таблиці applicants
        mycursor.execute("SELECT MAX(applicant_id) FROM abikpi.applicants;")
        result1 = mycursor.fetchone()
        last_applicant_id = result1[0] if result1[0] is not None else 0

        # Генерація нового applicant_id
        new_applicant_id = last_applicant_id + 1

        # Запит для отримання максимального document_id з таблиці applicants
        mycursor.execute("SELECT MAX(document_id) FROM abikpi.applicants;")
        result2 = mycursor.fetchone()
        last_document_id = result2[0] if result2[0] is not None else 0

        # Генерація нового document_id
        new_document_id = last_document_id + 1

        # Запит для вставки нового апліканта в таблицю applicants
        applicants_query = (
            "INSERT INTO abikpi.applicants "
            "(applicant_id, applicant_name, document_id, gender, quota, applicant_email,applicant_password) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )

        # Дані нового апліканта
        data_applicant = (new_applicant_id, name, new_document_id, gender, quota, email, password)

        # Виконання SQL-запиту для вставки нового апліканта
        mycursor.execute(applicants_query, data_applicant)

        # Збереження змін у базі даних
        self.mydb.commit()

        # Закриття курсора
        mycursor.close()

        '''fetchone() - це метод, який використовується для отримання одного рядка (запису) результатів вибірки з бази даних'''







