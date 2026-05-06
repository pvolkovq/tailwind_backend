from tailwind.models import Artwork, Portfolio, User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class ArtworkAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.portfolio = Portfolio.objects.create(user=self.user, information="Test info")
        self.artwork = Artwork.objects.create(
            title="Test Artwork",
            portfolio=self.portfolio,
            image="test_image.jpg"
        )

    def test_get_artwork_list(self):
        url = reverse('artwork-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Artwork")

    def test_get_artwork_detail(self):
        url = reverse('artwork-detail', args=[self.artwork.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Artwork")