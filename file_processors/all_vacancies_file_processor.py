import json

from file_processors.file_processor_base_class import FileProcessorBaseClass
from file_processors.headhunter_file_processor import HeadHunterFileProcessor
from file_processors.superjob_file_processor import SuperJobFileProcessor


class AllVacanciesFileProcessor(FileProcessorBaseClass):
    """
    Класс работы с вакансиями из всех сервисов
    """

    def save_vacancies_to_file(self, *args: str, **kwargs: str) -> None:
        """
        Сохраняет вакансии из файлов-хранилищ, полученных по API всех сервисов
        :param args: имена файлов,
        из которых загружать данные и в который сохранять
        :type args: str
        :param kwargs: имена файлов,
        из которых загружать данные и в который сохранять
        :type kwargs: str
        """
        filename: str = kwargs["filename"]
        hh_filename: str = kwargs["hh_filename"]
        sj_filename: str = kwargs["sj_filename"]
        hh_data: list[dict] = HeadHunterFileProcessor().load_vacancies_from_file(
            filename=hh_filename
        )
        sj_data: list[dict] = SuperJobFileProcessor().load_vacancies_from_file(
            filename=sj_filename
        )
        with open(filename, "w", encoding="UTF-8") as file:
            combined_data = []
            for item in zip(hh_data, sj_data):
                for dictionary in item:
                    combined_data.append(dictionary)
            json.dump(combined_data, file, indent=2, ensure_ascii=False)