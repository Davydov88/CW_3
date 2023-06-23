import requests
import json
from parsers.parser_abc_class import ApiParserABCClass


class HeadHunter(JobApi):
    """
    Класс получения данных по API HeadHunter
    """

    def get_vacancies_data(self, *args, **kwargs) -> list[dict]:
        """
        Получает отфильтрованные данные по вакансии по API
        :param kwargs: параметры запроса к API
        :type kwargs: int, str, array
        :return: Список словарей с данными вакансий
        :rtype: list[dict]
        """
        params = {
            "per_page": 100,  # указание количества вакансий на страницу
            "page": 0,  # запрос начинается с нулевой страницы
            "period": 30,  # период размещения вакансий от текущей даты
            "only_with_salary": True,  # возвращать вакансии только с зарплатой
            "area": 113,  # страна поиска Россия
            "search_field": "name"  # в какой обаласти вакансии
                                    # искать ключевое слово
        }

        #  распаковка аргументов и подставновка в параметры запроса
        for key, value in kwargs.items():
            params[f"{key}"] = value

        response = requests.get("https://api.hh.ru/vacancies", params=params)
        if not response.status_code == 200:
            print(response.status_code, response.text)
        vacancies_description = response.json()["items"]

        # получение количества страниц из ответа
        pages = response.json()["pages"]

        # обновление номера страницы в запросе к API
        for page in range(1, pages):
            params["page"] = page
            response = requests.get("https://api.hh.ru/vacancies",
                                    params=params
                                    )
            vacancies_description.extend(response.json()["items"])
        return vacancies_description

    def get_additional_dicts(self) -> dict:
        """
        Получает справочник дополнительных параметров запросов к API
        :return: словарь со справочником дополнительных параметров
        для запросов к API
        :rtype: dict
        """
        response = requests.get("https://api.hh.ru/dictionaries")
        if not response.status_code == 200:
            print(response.text)
        additional_dicts: dict = response.json()
        return additional_dicts

    def get_area_dicts(self) -> dict:
        """
        Получает справочник городов для запроса к API
        :return: словарь со справочником городов для запросов к API
        :rtype: dict
        """
        response = requests.get("https://api.hh.ru/areas/113")
        if not response.status_code == 200:
            print(response.text)
        area_dicts: dict = response.json()
        return area_dicts