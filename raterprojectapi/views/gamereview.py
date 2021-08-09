"""View module for handling requests about games"""
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from raterprojectapi.models import Review, Game
from django.contrib.auth.models import User


class GameReviewView(ViewSet):
    """gamerrater reviews"""

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized game instance
        """

        # Uses the token passed in the `Authorization` header

        # Create a new Python instance of the Game class
        # and set its properties from what was sent in the
        # body of the request from the client.
        review = Review()
        review.article = request.data["article"]

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameTypeId` in the body of the request.
        game = Game.objects.get(pk=request.data["game_id"])
        review.game = game

        review.player = request.auth.user
     
        try:
            review.save()
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)



    # def retrieve(self, request, pk=None):
    #     """Handle GET requests for single game

    #     Returns:
    #         Response -- JSON serialized game instance
    #     """
    #     try:
    #         # `pk` is a parameter to this function, and
    #         # Django parses it from the URL route parameter
    #         #   http://localhost:8000/games/2
    #         #
    #         # The `2` at the end of the route becomes `pk`
    #         game = Game.objects.get(pk=pk)
    #         serializer = GameSerializer(game, context={'request': request})
    #         return Response(serializer.data)
    #     except Exception as ex:
    #         return HttpResponseServerError(ex)

    # def update(self, request, pk=None):
    #     """Handle PUT requests for a game

    #     Returns:
    #         Response -- Empty body with 204 status code
    #     """
    #     gamer = Gamer.objects.get(user=request.auth.user)

    #     # Do mostly the same thing as POST, but instead of
    #     # creating a new instance of Game, get the game record
    #     # from the database whose primary key is `pk`
    #     game = Game.objects.get(pk=pk)
    #     game.title = request.data["title"]
    #     game.description = request.data["description"]
    #     game.designer = request.data["designer"]
    #     game.year_released = request.data["year_released"]
    #     game.num_of_players = request.data["num_of_players"]
    #     game.play_time = request.data["play_time"]
    #     game.recommended_age = request.data["recommended_age"]

    #     game_type = GameType.objects.get(pk=request.data["gameTypeId"])
    #     game.game_type = game_type
    #     game.save()

    #     # 204 status code means everything worked but the
    #     # server is not sending back any data in the response
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk=None):
    #     """Handle DELETE requests for a single game

    #     Returns:
    #         Response -- 200, 404, or 500 status code
    #     """
    #     try:
    #         game = Game.objects.get(pk=pk)
    #         game.delete()

    #         return Response({}, status=status.HTTP_204_NO_CONTENT)

    #     except Game.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

    #     except Exception as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to review resource

        Returns:
            Response -- JSON serialized list of categories
        """
        # Get all game records from the database
        reviews = Review.objects.all()

        # Support filtering games by type
        #    http://localhost:8000/games?type=1
        #
        # That URL will retrieve all tabletop games
        # game_type = self.request.query_params.get('type', None)
        # if game_type is not None:
        #     games = games.filter(game_type__id=game_type)

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(serializer.data)

class ReviewSerializer(serializers.ModelSerializer):
    """JSON serializer for reviews

    Arguments:
        serializer type
    """
    class Meta:
        model = Review
        fields = '__all__'
        depth = 1