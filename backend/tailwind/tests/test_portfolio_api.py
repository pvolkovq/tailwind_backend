from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from tailwind.models import Portfolio, User

class PortfolioAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        # self.client.login(username=self.user.username, password="testpassword")
        self.portfolio = Portfolio.objects.create(user=self.user, description="Test info")
        for i in range(5):
            user = User.objects.create_user(username=f"testuser_{i}", password="testpassword")
            Portfolio.objects.create(user=user, description=f"Test info {i}", is_commissioning_open=(i % 2 == 0))

    def test_get_portfolios_list(self):
        url = reverse('portfolio-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_portfolio_detail(self):
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["description"], "Test info")
    
    def test_create_portfolio(self):
        url = reverse('portfolio-list')
        data = {
            "user": self.user.id,
            "description": "New portfolio info",
            "is_commissioning_open": True
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_delete_portfolio(self):
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filters_portfolio_by_is_commissioning_open(self):
        url = reverse('portfolio-list')
        response = self.client.get(url, {'is_commissioning_open': True})
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_portfolio_by_username(self):
        url = reverse('portfolio-list')
        response = self.client.get(url, {'search': 'testuser'})
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_portfolio_for_authenticated_user(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_portfolio_not_from_creator(self):
        other_user = User.objects.create_user(username="otheruser", password="testpassword")
        self.client.login(username=other_user.username, password="testpassword")
        url = reverse('portfolio-detail', args=[self.portfolio.id])
        data = {
            "user": self.user.id,
            "description": "change test",
            "is_commissioning_open": False
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_portfolio_list_allow_any(self):
        url = reverse('portfolio-view-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_portfolio_create_allow_any(self):
        url = reverse('portfolio-view-list')
        data = {
            "user": 3,
            "description": "not auth user",
            "is_commissioning_open": False
        }
        response = self.client.post(url, )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_portfolio_update_allow_any(self):
        url = reverse('portfolio-view-detail', args=[self.portfolio.id])
        data = {
            "user": 3,
            "description": "not auth user",
            "is_commissioning_open": False
        }
        response = self.client.put(url, )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)