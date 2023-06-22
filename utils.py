from parsers.headhunter_parser import HeadHunterParser
from parsers.superjob_parser import SuperJobParser


def get_search_experience_id(experience_index_input: int) -> list:
    """
    Вспомогательная функция получения id
    выбранного параметра опыта из справочников API
    :param experience_index_input:
    индекс строчного элемента списка возможных вариантов опыта,
    соотв. пользовательскому вводу
    :type experience_index_input: int
    :return: строка или список строк
    :rtype: str, list
    """
    experience_list = []

    #  получение id опыта для запроса к API HH
    hh_all_experience_dicts: list = HeadHunterParser().get_additional_dicts()["experience"]
    hh_experience_dict = hh_all_experience_dicts[experience_index_input - 1]
    experience_list.append(hh_experience_dict["id"])

    #  получение id опыта для запроса к API SJ
    sj_experience_dict: dict = SuperJobParser().get_additional_data_dicts()["experience"]
    for key in sj_experience_dict.keys():
        if str(experience_index_input) == key:
            experience_list.append(int(key))

    return experience_list


def get_city_id(search_city: str) -> list:
    """
    Вспомогательная функция полчуения id города, введеного пользователем
    :param search_city: название города с пользовательского ввода
    :type search_city: str
    :return: список id городов для запроса к обоим API
    :rtype: list
    """
    cities_list = []
    hh_areas_list: dict = HeadHunterParser().get_area_dicts()["areas"]
    for area in hh_areas_list:

        # проверка наличия города вне региона (напр. Москва)
        if search_city in area["name"]:
            cities_list.append(str(area["id"]))
        else:
            for city in area["areas"]:  # спуск до городов внутри регионов
                if search_city in city["name"]:
                    cities_list.append(str(city["id"]))

    sj_towns_list: list = SuperJobParser().get_towns_dict()["objects"]
    for item in sj_towns_list:
        if search_city == item["title"]:
            cities_list.append(item["id"])

    return cities_list