from post.models import Post # , PostLike, PostUnLike
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from django.conf import settings

class PostUnLikeSerializer(serializers.ModelSerializer):
    unlike = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = ('unlike',)
        extra_kwargs = {'unlike': {'read_only': True}}

    def update(self, instance, validated_data):
        # print(validated_data.get('like', instance.like).id)
        user_id = validated_data.get('unlike', instance.unlike).id
        if len(instance.unlike.filter(id=user_id)) > 0:
            instance.unlike.remove(user_id)
        else:
            if len(instance.like.filter(id=user_id)) > 0:
                instance.like.remove(user_id)
            instance.unlike.add(user_id)
        instance.save()
        return instance

class PostLikeSerializer(serializers.ModelSerializer):
    like = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ('like',)
        extra_kwargs = {'like': {'read_only': True}}

    def update(self, instance, validated_data):
        # print(validated_data.get('like', instance.like).id)
        user_id = validated_data.get('like', instance.like).id
        if len(instance.like.filter(id=user_id)) > 0:
            instance.like.remove(user_id)
        else:
            if len(instance.unlike.filter(id=user_id)) > 0:
                instance.unlike.remove(user_id)
            instance.like.add(user_id)
        instance.save()
        return instance

class PostCreateSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    Like_This = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='post_like'
    )
    UnLike_This = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name='post_unlike'
    )


    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {'like': {'read_only': True}, 'unlike': {'read_only': True}}
