from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Point
from .serializers import PointSerializer
import math


def find_closest_points(points_str):
        points = points_str.split(';')
        num_points = len(points)
        closest_distance = float('inf')
        closest_points = []

        # Iterate through each pair of points
        for i in range(num_points):
            x1, y1 = map(int, points[i].split(','))

            for j in range(i + 1, num_points):
                x2, y2 = map(int, points[j].split(','))

                # Calculate the Euclidean distance between the two points
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

                # Check if the distance is smaller than the current closest distance
                if distance < closest_distance:
                    closest_distance = distance
                    closest_points = [points[i], points[j]]
                elif distance == closest_distance:
                    closest_points.extend([points[i], points[j]])

        return closest_points


class ClosePoints(APIView):
    
    serializer_class = PointSerializer
    def get(self, request):
        allPoints = Point.objects.all().values()
        return Response({"Message":"List of points and the nearest points Euclidean distance", "Points":allPoints })
    
    
    def post(self, request):

        print("Request data is :", request.data)

        serializer_obj= PointSerializer(data=request.data) 

        if(serializer_obj.is_valid()):
            close_points = find_closest_points(request.data["points"])
            closest_points = ';'.join(close_points) 
        
            Point.objects.create(id=request.data['id'],
                                 points=request.data['points'],
                                close_points = closest_points
                                )

        eucld_point = Point.objects.all().filter(id=request.data["id"]).values()
        return Response({"Message":"New points& euclidean distance added", "Points":eucld_point })
    
