from rest_framework.test import APITestCase

from django.urls import reverse

from .models import Log


class LogViewSetTest(APITestCase):
    def setUp(self):
        Log.objects.create(user_id=123, command='/weather Москва', response='Тестовый ответ')
        Log.objects.create(user_id=13, command='/weather Санкт-Петербург', response='Тестовый ответ')
        Log.objects.create(user_id=456, command='/weather Уфа', response='Тестовый ответ')

    def test_get_All_logs(self):
        url = reverse("logs-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 2)

    def test_pagination(self):
        url = reverse("logs-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 2)

    def test_retrieve_log_detail(self):
        log = Log.objects.first()
        url_detail = reverse('logs-detail', args=[log.id])
        response = self.client.get(url_detail)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], log.id)
        self.assertEqual(response.data['user_id'], log.user_id)
        self.assertEqual(response.data['command'], log.command)
        self.assertEqual(response.data['response'], log.response)
