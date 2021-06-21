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


# sort: 'most_liked'
def get_creation_list(game: str = 'all', creation_type: str = 'all',
                      page: int = 0, per_page: int = 16,
                      sort_order: str = 'desc', campaign_ids=None,
                      time: int = 0, sort: int = 0,
                      featured: int = 0, is_winner: bool = False,
                      is_finalist: bool = False, popular: int = 0,
                      almost_finalist: int = 0, user_id: int = 0,
                      voted_on: int = 0, similar_to: int = 0,
                      home_page: int = 0, video_featured: int = 0) -> dict:
    if campaign_ids is None:
        campaign_ids = []
    campaign_ids = [str(_id) for _id in campaign_ids]

    data = {
        'Game': game,
        'CreationType': creation_type,
        'Page': page,
        'PerPage': per_page,
        'SortOrder': sort_order,
        'Campaign': campaign_ids,
        'Time': time,
        'Sort': sort,
        'Featured': int(featured),
        'Winner': int(is_winner),
        'Finalist': int(is_finalist),
        'Popular': popular,
        'AlmostFinalist': almost_finalist,
        'UserId': user_id,
        'VotedOn': voted_on,
        'SimilarTo': similar_to,
        'HomePage': home_page,
        'VideoFeatured': video_featured
    }

    return get_json_from_server('/CreationList', data)


def get_characters(language: str = 'en') -> dict:
    data = {
        'lang': language,
    }

    return get_json_from_server('/CharacterList', data)


def get_sceneries(language: str = 'en') -> dict:
    data = {
        'lang': language,
    }

    return get_json_from_server('/SceneryList', data)


def get_heroes(game: str = '', page: int = 0,
               per_page: int = 16, sort: str = 'most_liked',
               sort_order: str = 'desc', search_term: str = '',
               language: str = 'en') -> dict:
    data = {
        'lang': language,

        'Game': game,
        'Page': page,
        'PerPage': per_page,
        'Sort': sort,
        'SortOrder': sort_order,
        'SearchTerm': search_term
    }

    return get_json_from_server('/HeroList', data)


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
    # download('https://maksupercell.com/en/creation/kragale-krampus-gale')
