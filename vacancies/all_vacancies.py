from vacancies.vacancy_base_class import VacancyBaseClass


class AllVacancies(VacancyBaseClass):
    """
    Класс всех вакансий с HeadHunter и SuperJob
    """

    def __init__(self, *args, **kwargs) -> None:
        """
        Конструктор класса, инициализируется именованными аргументами,
        получаемыми из файла вакансий
        :param args: значения словаря с данными вакансий
        :type args: int, str
        :param kwargs: значения словаря с данными вакансий
        :type kwargs: int, str
        """
        super().__init__(*args, **kwargs)

        self.service: str = kwargs["service"]

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Сервис поиска работы: {self.service}\n" \
               f"Компания: {self.employer_name}\n" \
               f"Позиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: от {self.salary_from} до {self.salary_to} руб\n" \
               f"Требования к соискателю:\n{self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\n" \
               f"Ссылка на вакансию: {self.url}\n"

    def __str__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Сервис поиска работы: {self.service}\n" \
               f"Компания: {self.employer_name}\n" \
               f"Позиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: от {self.salary_from} до {self.salary_to} руб\n" \
               f"Требования к соискателю:\n{self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\n" \
               f"Ссылка на вакансию: {self.url}\n"