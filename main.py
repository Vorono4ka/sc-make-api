import requests
import json


server_url = 'https://3c18w2n4l7.execute-api.us-east-1.amazonaws.com'


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

    return get_json_from_server('/prod/CampaignList', data)


def get_campaign(_id: int,
                 language: str = 'en') -> dict:
    data = {
        'Id': str(_id),
        'lang': language
    }

    return get_json_from_server('/prod/CampaignGet', data)


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

    return get_json_from_server('/prod/CreationList', data)


def get_creation(_id: int,
                 language: str = 'en') -> dict:
    data = {
        'Id': _id,
        'UserToken': '',
        'UserId': '',
        'lang': language,
    }

    return get_json_from_server('/prod/CreationGet', data)


if __name__ == '__main__':
    print(get_campaign_list())
    print(get_creation_list(1, 8, [26]))
    # download('https://make.supercell.com/en/creation/kragale-krampus-gale')
