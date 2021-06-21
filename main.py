import requests
import json


server_url = 'https://oh14aups3g.execute-api.us-east-1.amazonaws.com/prod'


def get_json_from_server(path: str,
                         data: dict):
    data = json.dumps(data, ensure_ascii=False).encode()

    request = requests.post(server_url + path,
                            data=data)
    return request.json()


def get_campaign_list(language: str = 'en') -> dict:
    data = {
        'lang': language
    }

    return get_json_from_server('/CampaignList', data)


def get_campaign(_id: int,
                 language: str = 'en') -> dict:
    data = {
        'Id': str(_id),
        'lang': language
    }

    return get_json_from_server('/CampaignGet', data)


def get_creation_list(page: int = 0,
                      per_page: int = 8,
                      campaign_ids: list = None,
                      is_finalist: bool = False,
                      is_winner: bool = False) -> dict:
    if campaign_ids is None:
        campaign_ids = []
    else:
        campaign_ids = [str(_id) for _id in campaign_ids]

    data = {
        'UserToken': '',
        'Page': page,
        'PerPage': per_page,
        'Campaign': campaign_ids,
        'Sort': 'most_liked',
        'SortOrder': 'desc',
        'Finalist': int(is_finalist),
        'Winner': int(is_winner),
    }

    return get_json_from_server('/CreationList', data)


def get_creation(_id: str,
                 language: str = 'en') -> dict:
    data = {
        'Id': _id,
        'UserToken': '',
        'UserId': '',
        'lang': language,
    }

    return get_json_from_server('/CreationGet', data)


if __name__ == '__main__':
    print(get_creation_list())
    print(get_creation('kragale-krampus-gale'))
    # download('https://make.supercell.com/en/creation/kragale-krampus-gale')
