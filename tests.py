import unittest

from core import *


class CoreTests(unittest.TestCase):
    def test_get_friends_request(self):
        expected = f'https://api.vk.com/method/friends.get?access_token={access_token}&user_id=1&count=1&fields=nickname&v=5.131'
        actual = get_friends_request(1, 1)
        assert actual == expected

    def test_format_response(self):
        response = f'https://api.vk.com/method/friends.get?access_token={access_token}&user_id=121287168&count=10&fields=nickname&v=5.131'
        expected = ['10 / 91 friends', 'Михаил Каданцев', 'Кристина Логвиненко', 'Андрей Остроумов', 'Мария Булатова',
                    'Александр Яскевич', 'Константин Колмогорцев', 'Ксюша Шорохова', 'Полина Осетрова',
                    'Ярослав Иванов', 'Варвара Петрова']

        actual = list(format_response(requests.get(response)))
        assert expected == actual