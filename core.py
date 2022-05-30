import requests
import os


version = 5.131
access_token = os.getenv('access_token') # поменять на свой access_token
my_client_id = 8176141


def get_authorization_address(client_id):
    redirect_uri = 'https://oauth.vk.com/blank.html'
    display = 'page'
    scope = 'friends'
    response_type = 'token'
    state = 123456
    address = 'https://oauth.vk.com/authorize'
    return f'{address}?client_id={client_id}&display={display}&redirect_uri={redirect_uri}&scope={scope}&response_type={response_type}&v={version}&state={state}'


def get_friends_request(user_id, count):
    request_address = 'https://api.vk.com/method'
    method = 'friends.get'
    fields = 'nickname'
    return f'{request_address}/{method}?access_token={access_token}&user_id={user_id}&count={count}&fields={fields}&v={version}'


def read_int(text):
    input_str = ''
    try:
        input_str = input(text)
        result = int(input_str)
        return result
    except ValueError:
        print(f"{input_str} should be integer")


def format_response(response):
    if response.status_code == 200:
        response_as_json = response.json()
        if 'error' in response_as_json:
            yield response.json()['error']['error_msg']
        else:
            count = response_as_json['response']['count']
            items = response_as_json['response']['items']
            yield f"{len(items)} / {count} friends"
            for friend in items:
                yield f"{friend['first_name']} {friend['last_name']}"
    else:
        yield 'Response status code: ' + str(response.status_code)


if __name__ == '__main__':
    user_id = None
    count = None
    while user_id is None:
        user_id = read_int('write user id: ')
    while count is None:
        count = read_int('write how many friends you want to see: ')

    response = None
    try:
        response = requests.get(get_friends_request(user_id, count))
    except requests.exceptions.ConnectionError:
        print("Connection error was raised. Make sure you have access to the internet")

    if response is not None:
        for line in format_response(response):
            print(line)
