from django.contrib.auth.models import User

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True, required=False)
    old_password = serializers.CharField(write_only=True, required=False)
    username = serializers.CharField(read_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data) # creates new user objects using
                                                     # validated_data fields
        user.set_password(password)
        user.save()

        return user

    def update(self, instance, validated_data):
        try:
            user = instance
            password = validated_data.pop('password')
            old_password = validated_data.pop('old_password')
            if user.check_password(old_password):
                user.set_password(password)
            else:
                raise Exception("Old password is incorrect.")
            user.save()
        except Exception as error:
            raise serializers.ValidationError({'info': error})
        return super(UserSerializer, self).update(instance, validated_data)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email',
                  'first_name', 'last_name', 'email',
                  'password', 'old_password'
                  ]
