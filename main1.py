import tkinter as tk
from tkinter import messagebox

import window as window

from file_processors.all_vacancies_file_processor import AllVacanciesFileProcessor
from file_processors.headhunter_file_processor import HeadHunterFileProcessor
from file_processors.superjob_file_processor import SuperJobFileProcessor
from utils import get_search_experience_id, get_city_id
from vacancies.all_vacancies import AllVacancies
from vacancies.headhunter_vacancy import HeadHunterVacancy
from vacancies.superjob_vacancy import SuperJobVacancy


def display_vacancies(vacancies, top_chart_size):
    result_text = f"Топ-{top_chart_size} вакансий по начальной зарплате:\n\n"
    for vacancy in vacancies[:top_chart_size]:
        result_text += str(vacancy) + "\n\n"
    return result_text

api_service_var = tk.StringVar()

# Create the OptionMenu using api_service_var
api_service_combobox = tk.OptionMenu(window, api_service_var, "HeadHunter", "SuperJob", "Оба сервиса")
api_service_combobox.grid(row=0, column=1, padx=10, pady=5)

def search_button_clicked(api_service_var=None, experience_var=None):
    api_service_value = api_service_var.get()
    if api_service_value == "HeadHunter":
        api_service_index = 1
    elif api_service_value == "SuperJob":
        api_service_index = 2
    else:
        api_service_index = 3

    search_keyword = keyword_entry.get()

    try:
        search_salary = int(salary_entry.get())
    except ValueError:
        result_text_label.configure(text="Зарплата должна быть целым числом")
        return

    experience_value = experience_var.get()
    experience_index_input = {
        "Нет опыта": 1,
        "От 1 года до 3 лет": 2,
        "От 3 до 6 лет": 3,
        "Более 6 лет": 4
    }[experience_value]

    search_city = city_entry.get().capitalize()

    try:
        top_chart_size = int(top_chart_size_entry.get())
    except ValueError:
        result_text_label.configure(text="Необходимо ввести количество вакансий")
        return

    search_experience_list = get_search_experience_id(experience_index_input)
    city_data_list = get_city_id(search_city)

    if api_service_index == 1:
        HeadHunterFileProcessor().save_vacancies_to_file(
            filename="vacancies_hh.json",
            text=search_keyword,
            experience=search_experience_list[0],
            area=city_data_list[0],
            salary=search_salary
        )
        vacancies = HeadHunterFileProcessor().load_vacancies_from_file(
            filename="vacancies_hh.json"
        )
        all_hh_vacancies = [
            HeadHunterVacancy(
                employer_name=item["employer"],
                area=item["city"]["name"],
                vacancy_name=item["name"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"],
                experience=item["experience"]["name"],
                description=item["responsibility"],
                employment=item["employment"]["name"],
                url=item["url"]
            ) for item in vacancies
        ]
        sorted_vacancies = sorted(
            all_hh_vacancies,
            key=lambda cls_object: cls_object.salary_from,
            reverse=True
        )
    elif api_service_index == 2:
        SuperJobFileProcessor().save_vacancies_to_file(
            filename="vacancies_sj.json",
            keyword=search_keyword,
            experience=search_experience_list[1],
            town=city_data_list[1],
            payment_from=search_salary
        )
        vacancies = SuperJobFileProcessor().load_vacancies_from_file(
            filename="vacancies_sj.json"
        )
        all_sj_vacancies = [
            SuperJobVacancy(
                employer_name=item["employer"],
                area=item["city"]["name"],
                vacancy_name=item["name"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"],
                experience=item["experience"]["name"],
                description=item["responsibility"],
                employment=item["employment"]["name"],
                url=item["url"]
            ) for item in vacancies
        ]
        sorted_vacancies = sorted(
            all_sj_vacancies,
            key=lambda cls_object: cls_object.salary_from,
            reverse=True
        )
    else:
        search_experience_hh = search_experience_list[0]
        city_id_hh = city_data_list[0]

        HeadHunterFileProcessor().save_vacancies_to_file(
            filename="vacancies_hh.json",
            text=search_keyword,
            experience=search_experience_hh,
            area=city_id_hh,
            salary=search_salary
        )

        search_experience_sj = search_experience_list[1]
        city_id_sj = city_data_list[1]

        SuperJobFileProcessor().save_vacancies_to_file(
            filename="vacancies_sj.json",
            keyword=search_keyword,
            experience=search_experience_sj,
            town=city_id_sj,
            payment_from=search_salary
        )

        AllVacanciesFileProcessor().save_vacancies_to_file(
            filename="vacancies_all.json",
            hh_filename="vacancies_hh.json",
            sj_filename="vacancies_sj.json"
        )

        vacancies = AllVacanciesFileProcessor().load_vacancies_from_file(
            filename="vacancies_all.json"
        )
        all_vacancies = [
            AllVacancies(
                service=item["service"],
                employer_name=item["employer"],
                area=item["city"]["name"],
                vacancy_name=item["name"],
                salary_from=item["salary_from"],
                salary_to=item["salary_to"],
                requirement=item["requirement"],
                experience=item["experience"]["name"],
                description=item["responsibility"],
                employment=item["employment"]["name"],
                url=item["url"]
            ) for item in vacancies
        ]
        sorted_vacancies = sorted(
            all_vacancies,
            key=lambda cls_object: cls_object.salary_from,
            reverse=True
        )

    result_text = display_vacancies(sorted_vacancies, top_chart_size)
    result_text_label.configure(text=result_text)



# Создание главного окна
window = tk.Tk()
window.title("Поиск вакансий")
window.geometry("500x400")

# Создание и размещение элементов интерфейса
api_service_label = tk.Label(window, text="Выберите сервис поиска вакансий:")
api_service_label.pack()

api_service_combobox = tk.OptionMenu(window, tk.StringVar(), "HeadHunter", "SuperJob", "Оба сервиса")
api_service_combobox.pack()

keyword_label = tk.Label(window, text="Ключевое слово:")
keyword_label.pack()

keyword_entry = tk.Entry(window)
keyword_entry.pack()

salary_label = tk.Label(window, text="Зарплата:")
salary_label.pack()

salary_entry = tk.Entry(window)
salary_entry.pack()

experience_label = tk.Label(window, text="Выберите опыт работы:")
experience_label.pack()

experience_combobox = tk.OptionMenu(window, tk.StringVar(), "Нет опыта", "От 1 года до 3 лет", "От 3 до 6 лет", "Более 6 лет")
experience_combobox.pack()

city_label = tk.Label(window, text="Город:")
city_label.pack()

city_entry = tk.Entry(window)
city_entry.pack()

top_chart_size_label = tk.Label(window, text="Введите количество вакансий в топе для отображения:")
top_chart_size_label.pack()

top_chart_size_entry = tk.Entry(window)
top_chart_size_entry.pack()

search_button = tk.Button(window, text="Поиск", command=search_button_clicked)
search_button.pack()

result_text_label = tk.Label(window, text="")
result_text_label.pack()

# Запуск основного цикла обработки событий
window.mainloop()
