from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from user_operation.models import AddWrongWordsCte4, AddWrongWordsCte6
from user_operation.models import UserLearnedWordsCte6, UserLearnedWordsCte4
from backend.serializers import WdSerializer

class Cte4Serializer(serializers.ModelSerializer):
    save_cte4_words = WdSerializer()
    class Meta:
        model = AddWrongWordsCte4
        fields = ('save_cte4_words',)

class AW4Serializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=AddWrongWordsCte4.objects.all(),
                fields=('user', 'save_cte4_words'),
                message="已添加过"
            )
        ]
        model = AddWrongWordsCte4
        fields = ('user', 'save_cte4_words')
   
class RCte4Serializer(serializers.ModelSerializer):
    cte4 = WdSerializer()
    class Meta:
        model = UserLearnedWordsCte4
        fields = ('cte4',)

class A4Serializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserLearnedWordsCte4.objects.all(),
                fields=('user', 'cte4'),
                message="已添加过"
            )
        ]
        model = UserLearnedWordsCte4
        fields = ('user', 'cte4')
