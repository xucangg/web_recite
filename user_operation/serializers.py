from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import UserSaveWords

class UserSaveWordSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserSaveWords
        validators = [
            UniqueTogetherValidator(
                queryset=UserSaveWords.objects.all(),
                fields=('user', 'Cte4_words', 'Cte6_words'),
                message='已保存'
            )
        ]
