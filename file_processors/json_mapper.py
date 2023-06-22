class JSONMapper:
    """
    Класс для маппинга после получения по API
    """

    @staticmethod
    def map_hh_json_data(data) -> list[dict]:
        """
        Маппит полученный от API список словарей с данными вакансий.
        :param data: данные из API
        :type data: list[dict]
        :return: унифицированный формат данных вакансии
        :rtype: list[dict]
        """

        formatted_dicts_list = []
        for item in data:
            formatted_dicts_list.append(
                {
                    "service": "HeadHunter",
                    "id": item["id"],
                    "name": item["name"],
                    "city": {
                        "id": item["area"]["id"],
                        "name": item["area"]["name"]
                    },
                    "salary_from": item["salary"]["from"],
                    "salary_to": item["salary"]["to"],
                    "url": item["alternate_url"],
                    "employer": item["employer"]["name"],
                    "requirement": item["snippet"]["requirement"],
                    "responsibility": item["snippet"]["responsibility"],
                    "experience": {
                        "id": item["experience"]["id"],
                        "name": item["experience"]["name"]
                    },
                    "employment": {
                        "id": item["employment"]["id"],
                        "name": item["employment"]["name"]
                    }

                }
            )
        return formatted_dicts_list

    @staticmethod
    def map_sj_json_data(data) -> list[dict]:
        """
        Маппит полученный от API словарь с данными вакансий.
        :param data: данные из API
        :type data: dict
        :return: унифицированный формат данных вакансии
        :rtype: list[dict]
        """
        formatted_dicts_list = []
        for item in data["objects"]:
            formatted_dicts_list.append(
                {
                    "service": "SuperJob",
                    "id": item["id"],
                    "name": item["profession"],
                    "city": {
                        "id": item["town"]["id"],
                        "name": item["town"]["title"]
                    },
                    "salary_from": item["payment_from"],
                    "salary_to": item["payment_to"],
                    "url": item["link"],
                    "employer": item["client"]["title"],
                    "requirement": None,
                    "responsibility": item["candidat"],
                    "experience": {
                        "id": item["experience"]["id"],
                        "name": item["experience"]["title"]
                    },
                    "employment": {
                        "id": item["type_of_work"]["id"],
                        "name": item["type_of_work"]["title"]
                    }
                }
            )
        return formatted_dicts_list