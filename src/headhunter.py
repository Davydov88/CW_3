import requests
from src.abc.abc_job_api import JobApi
from requests import get
import json


class HeadHunter(JobApi):
    """Класс, наследующийся от абстрактного класса,
    для работы с платформой HeadHunter,
    и класса, для работы с файлом, содержащем вакансии hh.ru"""

    _api_link = "https://api.hh.ru/vacancies"

    def __init__(self):
        pass

    def __str__(self):
        return "headhunter.ru"

    def get_vacancies_api(self, **kwargs):
        """
        :param kwargs:
        area - Код региона (1 - Москва)
        text - Поисковый запрос
        per_page - Количество вакансий на странице
        """

        params = {}
        for key, value in kwargs.items():
            params[key] = value

        response = requests.get(self._api_link, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Ошибка при выполнении запроса:", response.status_code)
            return None

    def get_search_vacancies(self, search_data, n=15):
        return self.get_vacancies_api(text=search_data, per_page=n)

    def get_region_vacancies(self, region, n=15):
        return self.get_vacancies_api(area=region, count=n)
