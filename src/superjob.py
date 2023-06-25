import json
import requests
from src.abc.abc_job_api import JobApi


class SuperJob(JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой SuperJob,
    и класса, для работы с файлом, содержащем вакансии superjob.ru"""

    _API_KEY = "v3.r.127253021.e26c9a2e287fcc53ee2e9b7707c48cbca371f507.9d915df4e26d27b87fa2066897b5442326417a2e"
    _API_LINK = "https://api.superjob.ru/2.0/vacancies"

    def __init__(self):
        pass

    def __str__(self):
        return "superjob.ru"

    def get_vacancies_api(self, **kwargs):
        """
        :param kwargs:
        keyword - Ключевое слово для поиска
        town - Город (4 - Москва)
        count - Количество вакансий
        """

        headers = {
            'X-Api-App-Id': self._API_KEY
        }

        params = {}
        for key, value in kwargs.items():
            params[key] = value

        response = requests.get(self._API_LINK, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def get_search_vacancies(self, search_data, n=15):
        return self.get_vacancies_api(keyword=search_data, count=n)

    def get_region_vacancies(self, region, n=15):
        return self.get_vacancies_api(town=region, count=n)
