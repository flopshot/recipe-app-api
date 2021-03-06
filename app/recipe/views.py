from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient, Recipe
from recipe import serializers


class BaseRecipeAttributeViewSet(viewsets.GenericViewSet,
                                 mixins.ListModelMixin,
                                 mixins.CreateModelMixin):
    """Base ViewSet for recipe attributes in database"""

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """return objects for the authenticated user only"""

        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create a new object"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseRecipeAttributeViewSet):
    """Manages tags in database"""

    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseRecipeAttributeViewSet):
    """Manages ingredients in the database"""

    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """manage recipe in database"""

    serializer_class = serializers.RecipeSerializer
    queryset = Recipe.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """retrieve recipes only for authed user"""

        return self.queryset.filter(user=self.request.user)
