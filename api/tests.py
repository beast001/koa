from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Point
from .serializers import PointSerializer


# Create your tests here.
class ClosestPointsAPITestCase(TestCase):
    def setUp(self):
        self.post1 = Point.objects.create(id=100, points='4,3;0,3;20,11;4,5')
        self.post2 = Point.objects.create(id=101, points='5,4;0,3;20,11;4,5')

    def test_create_post(self):
        url = reverse('api')
        data = {
            'id': 102,
            'points': '4,3;0,3;20,11;4,5',
            'close_points':'4,3:4,3'
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(Point.objects.count(), 3)
        self.assertEqual(Point.objects.last().points, '4,3;0,3;20,11;4,5')
    
    def test_get_all_posts(self):
        url = reverse('api')

        response = self.client.get(url)

        posts = Point.objects.all()
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_unique_column(self):
        objects = Point.objects.all()
        column_values = set()
        for obj in objects:
            column_value = obj.id 
            column_values.add(column_value)
        self.assertEqual(len(objects), len(column_values))
