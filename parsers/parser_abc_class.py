from abc import ABC, abstractmethod


class ApiParserABCClass(ABC):
    """
    Абстрактный класс получения данных по API
    """

    @abstractmethod
    def get_vacancies_data(self, *args, **kwargs):
        """
        Абстрактный метод получения данных по API
        """
        pass