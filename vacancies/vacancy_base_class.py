class VacancyBaseClass:
    """
    Базовый класс вакансий
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
        self.employer_name: str = kwargs["employer_name"]
        self.area: str = kwargs["area"]
        self.vacancy_name: str = kwargs["vacancy_name"]

        if not kwargs["salary_from"] is None:
            self.salary_from: int = kwargs["salary_from"]
        else:
            self.salary_from = 0
        if not kwargs["salary_to"] is None:
            self.salary_to: int = kwargs["salary_to"]
        else:
            self.salary_to = 0
        if not kwargs["requirement"] is None:
            self.requirement: str = kwargs["requirement"]
        else:
            self.requirement = "не указано"

        self.experience: str = kwargs["experience"]
        self.description: str = kwargs["description"]
        self.employment: str = kwargs["employment"]
        self.url: str = kwargs["url"]

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Компания: {self.employer_name}\n" \
               f"Позиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: от {self.salary_from} до {self.salary_to} руб\n" \
               f"Требования к соискателю: {self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\n" \
               f"Ссылка на вакансию: {self.url}\n" \
               f""

    def __str__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса
        :return: строка с представлением экземпляра класса
        :rtype: str
        """
        return f"Компания: {self.employer_name}\n" \
               f"Позиция: {self.vacancy_name}, г.{self.area}\n" \
               f"Зарпалата: от {self.salary_from} до {self.salary_to} руб\n" \
               f"Требования к соискателю: {self.requirement}\n" \
               f"Опыт работы: {self.experience}\n" \
               f"Обязанности: {self.description}\n" \
               f"Тип занятости: {self.employment}\n" \
               f"Ссылка на вакансию: {self.url}\n" \
               f""
