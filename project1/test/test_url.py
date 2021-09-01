from django.conf.urls import url
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from travel.views import index, register, login, logout

class TestUrls(SimpleTestCase):

    def test_index_url_resolved(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, index)
    
    def test_register_url_resolved(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, register)
    
    def test_login_url_resolved(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, login)
    
    def test_logout_url_resolved(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, logout)

