import os
import json



class JSONJobFile:
    def __init__(self, file_path):
        self.file_path = file_path

    def add_vacancy(self, vacancy):
        vacancies = self.get_vacancies()
        vacancies.append(vacancy)
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False)
        return self.file_path

    def get_vacancies(self):
        if not os.path.isfile(self.file_path):
            return []
        with open(self.file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    def delete_vacancy(self, vacancy_id):
        vacancies = self.get_vacancies()  # Получить список вакансий
        updated_vacancies = [vacancy for vacancy in vacancies if
                             vacancy.get('id') != int(vacancy_id)]  # Удалить вакансию по id
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(updated_vacancies, file, ensure_ascii=False)
        return self.file_path


