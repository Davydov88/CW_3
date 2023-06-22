import os

import requests
from dotenv import load_dotenv


from datetime import datetime, timedelta

from parsers.parser_abc_class import ApiParserABCClass


class SuperJobParser(ApiParserABCClass):
    """
    Класс получения данных по API SuperJob
    """

    def get_vacancies_data(self, *args, **kwargs) -> dict:
        """
        Получает отфильтрованные данные вакансий по API
        :param kwargs: параметры запроса к API:
        keyword, payment_from, town, experience
        :type kwargs: keyword:
        str, payment_from: int, area: int, experience: str
        :return: Словарь с данными вакансий
        :rtype: dict
        """
        load_dotenv()
        __api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{__api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        params = {
            "count": 100,
            "page": 0,
            "no_agreement": 1,
            "date_published_from": datetime.today() - timedelta(days=30)
        }
        for key, value in kwargs.items():
            params[f"{key}"] = value

        response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                params=params,
                                headers=headers
                                )
        all_vacancies: list[dict] = response.json()["objects"]

        #  цикл получения всех вакансий,
        #  выполняется, пока API не вернет 'more': False
        vacancies_left = True
        while vacancies_left:
            response = requests.get("https://api.superjob.ru/2.0/vacancies/",
                                    params=params,
                                    headers=headers
                                    )
            params["page"] += 1
            all_vacancies.extend(response.json()["objects"])

            # цикл закончился т.к. API вернул False
            vacancies_left: list[dict] = response.json()["more"]
        return response.json()

    def get_additional_data_dicts(self) -> dict:
        """
        Получает словарь со справочниками
        дополнительных параметров запросов к API
        :return: словарь со справочниками
        :rtype: dict
        """
        load_dotenv()
        __api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{__api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.get("https://api.superjob.ru/2.0/references/",
                                headers=headers
                                )
        additional_dicts: dict = response.json()
        return additional_dicts

    def get_towns_dict(self) -> dict:
        """
        Получает словарь со справочниками городов
        :return: словарь со справочниками
        :rtype: dict
        """
        load_dotenv()
        __api_token: str = os.environ.get("SJ_API_KEY")
        headers = {
            "X-Api-App-Id": f"{__api_token}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        response = requests.get("https://api.superjob.ru/2.0/towns/?all=true",
                                headers=headers
                                )
        towns_dict: dict = response.json()
        return towns_dict
