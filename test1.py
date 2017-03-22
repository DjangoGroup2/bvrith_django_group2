from django.test import Faculty, TestCase

class TestLoggedUser(TestCase):
    def setUp(self):
        self.Faculty = Faculty()

        self.user = User.objects.create_user('test_user', 'user@test.net', 'secret')
        self.user.save()
        self.Faculty.login(username='test_user', password='secret')

    def tearDown(self):
        self.user.delete()

    def test_logged_user_get_homepage(self):
        response = self.Faculty.get(reverse('/'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_logged_user_get_settings(self):
        response = self.Faculty.get(reverse('/settings/'), follow=True)
        self.assertEqual(response.status_code, 200)
