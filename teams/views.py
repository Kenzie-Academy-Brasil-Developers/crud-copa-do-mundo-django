from rest_framework.views import APIView, status
from rest_framework.response import Response
from django.forms.models import model_to_dict
import ipdb

from .models import Team

class TeamView(APIView):
    def get(self, request):
        teams_list = []
        
        teams = Team.objects.all()
        
        for team in teams:
            t = model_to_dict(team)
            teams_list.append(t)
            
        return Response(teams_list)
    
    def post(self, request):
        team = Team.objects.create(**request.data)
        
        team_dict = model_to_dict(team)
        
        return Response(team_dict, status.HTTP_201_CREATED)
                

class TeamDatailView(APIView):
    def get(self, request, team_id):  
        
        if not team_id:
            return Response(status=status.HTTP_404_NOT_FOUND)
              
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
        
        if team == None:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
        
        team_dict = model_to_dict(team)

        return Response(team_dict)
    
    def patch(self, request, team_id):
        if not team_id:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        try:
            team = Team.objects.filter(id=team_id).first()
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
        
        if team == None:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
        
        for key, value in request.data.items():
            setattr(team, key, value)
        
        team.save()
        
        team_dict = model_to_dict(team)
        
        return Response(team_dict, 200)
    
    def delete(self, request, team_id):
        if not team_id:
            return Response(status=status.HTTP_404_NOT_FOUND)        
        
        try:
            team = Team.objects.filter(id=team_id).first()
        except Team.DoesNotExist:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
        
        if team == None:
            return Response({'message': 'Team not found'}, status.HTTP_404_NOT_FOUND)
        
        team.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
