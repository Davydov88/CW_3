import json

from file_processors.file_processor_base_class import FileProcessorBaseClass
from file_processors.json_mapper import JSONMapper
from parsers.superjob_parser import SuperJobParser


class SuperJobFileProcessor(FileProcessorBaseClass):
    """
    Класс для работы с файлами вакансий, полученных через API
    """
    def save_vacancies_to_file(self, *args, **kwargs) -> None:
        """
        Переопределяет метод базового класса. Сохраняет данные вакансии в файл
        :param args: имя файла для сохранения данных, параметры запроса к API
        :type args: str, int
        :param kwargs: имя файла для сохранения данных, параметры запроса к API
        :type kwargs: str, int
        :return: None
        :rtype: None
        """
        filename = kwargs["filename"]
        data: dict = SuperJobParser().get_vacancies_data(**kwargs)
        mapped_data: list[dict] = JSONMapper().map_sj_json_data(data)
        with open(filename, "w", encoding="UTF-8") as file:
            json.dump(mapped_data, file, indent=2, ensure_ascii=False)