from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Post,Account,Comment,Reply
from django.contrib.auth.models import User

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'
        extra_kwargs = {'id':{'read_only':True}}
    def create(self,validated_data):
        account = Account.objects.create(**validated_data)
        return account
class PostSerializer(ModelSerializer):
    by_name = serializers.CharField(source='by.__str__', read_only=True) 
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs=  {'id':{'read_only':True}}
    def create(self,validated_data):
        post = Post.objects.create(**validated_data)
        return post
class CommentSerializer(ModelSerializer):
    by_name = serializers.CharField(source='by.__str__', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs=  {'id':{'read_only':True}}
    def create(self,validated_data):
        comment = Comment.objects.create(**validated_data)
        return comment
class ReplySerializer(ModelSerializer):
    by_name = serializers.CharField(source='by.__str__', read_only=True)
    class Meta:
        model = Reply
        fields = '__all__'
        extra_kwargs = {'id': {'read_only': True},'created': {'read_only': True}}
        
    def create(self,validated_data):
        reply = Reply.objects.create(**validated_data)
        return reply
class UserSerializer(ModelSerializer):
   class Meta:
       model = User
       fields ='__all__'
       extra_kwargs = {'password': {'write_only': True}}
   def create(self, validated_data):
       user = User.objects.create_user(**validated_data)  # ** operator --> validated_data = {
#     'username': 'john_doe',
#     'email': 'john@example.com',  
#     'password': 'securepassword123'  to  user = User.objects.create_user(username='john_doe', email='john@example.com', password='securepassword123')
# }
       return user