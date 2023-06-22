import json

from file_processors.file_interface_abc_class import FileInterfaceABC


class FileProcessorBaseClass(FileInterfaceABC):
    """
    Базовый класс для работы с файлами вакансий, полученными через API
    """

    def save_vacancies_to_file(self, *args, **kwargs) -> None:
        pass

    def load_vacancies_from_file(
            self,
            *args: str,
            **kwargs: str
    ) -> list[dict]:
        """
        Метод загрузки данных вакансий из файла
        :param args: имя файла для сохранения
        :type args: str
        :param kwargs: имя файла для сохранения
        :type kwargs: str
        :return: список словарей с данными выкансий
        :rtype: list[dict]
        """
        filename: str = kwargs["filename"]
        with open(filename, "r", encoding="UTF-8") as file:
            vacancies_data: list[dict] = json.load(file)
            return vacancies_data

    def delete_vacancy_from_file(self, *args, **kwargs) -> None:
        """
        Удаляет вакансию из указанного файла по ее id
        :param args: id вакансии, имя файла
        :type args:  id: int, filename: str
        :param kwargs: id вакансии, имя файла
        :type kwargs: id: int, filename: str
        :return: None
        :rtype: None
        """
        vacancy_id: int = kwargs["vacancy_id"]
        data: list[dict] = self.load_vacancies_from_file()

        filename: str = kwargs["filename"]
        with open(filename, "w", encoding="UTF-8") as file:

            for item in data:
                if item["id"] == str(vacancy_id):
                    item_index = data.index(item)
                    del data[item_index]
                    print(f"Вакансия id={vacancy_id} удалена")
                    break
                else:
                    print(f"Вакансия id={vacancy_id} не найдена")
                    break
            json.dump(data, file, indent=2, ensure_ascii=False)