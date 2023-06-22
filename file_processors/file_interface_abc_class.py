from abc import ABC, abstractmethod


class FileInterfaceABC(ABC):
    """
    Абстрактный класс для работы с файлами вакансий
    """

    @abstractmethod
    def save_vacancies_to_file(self, *args, **kwargs):
        """
        Абстрактный метод сохранения информации в файл
        """
        pass

    @abstractmethod
    def load_vacancies_from_file(self):
        """
        Абстрактный метод загрузки информации из файла
        """
        pass

    @abstractmethod
    def delete_vacancy_from_file(self, *args, **kwargs):
        """
        Абстрактный метод удаления информации из файла по id вакансии
        """
        pass