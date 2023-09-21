from django.shortcuts import render
from rest_framework.response import Response # for rest framework api views
from rest_framework.decorators import api_view,permission_classes,parser_classes
from rest_framework.permissions import IsAuthenticated
from .models import Post,Comment,Reply,Account
from .serializers import PostSerializer,AccountSerializer,CommentSerializer,ReplySerializer,UserSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer # for auth
from rest_framework_simplejwt.views import TokenObtainPairView # for auth
from rest_framework import status
from rest_framework.parsers import MultiPartParser  # for imgs

# I dont remember if i copied this, ig yes.. jwt websitr for details;
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
# May be this is also copied
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

# Create your views here.
@api_view(['GET'])
def getPost(request):
    return Response('SocMed API')


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getPosts(request):
    # user = request.user
    # posts = user.post_set.all()
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many =True)
    
    return Response(serializer.data) 

@api_view(['GET'])
def getComments(request):
     comments = Comment.objects.all()
     serializer = CommentSerializer(comments,many =True)  
     return Response(serializer.data)

@api_view(['GET'])
def getReplies(request):
     replies = Reply.objects.all()
     serializer = ReplySerializer(replies,many =True)  
     return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data = request.data)
    print (request.data)
    if serializer.is_valid():
        user=serializer.save()
        accserializer = AccountSerializer(data= {'user':user.pk})
        if(accserializer.is_valid()):
            accserializer.save()
            return Response({'message': 'User registered and Account created successfully'}, status=status.HTTP_201_CREATED)
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postreply(request):
    serializer = ReplySerializer(data = request.data)
    print(request.data, 'valid? ',serializer.is_valid())
    
    if serializer.is_valid():
         user = serializer.save()
         
         return Response({'message': 'Reply posted successfully'}, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def postcomment(request):
    serializer = CommentSerializer(data = request.data)
   # print(request.data, 'valid? ',serializer.is_valid())
    
    if serializer.is_valid():
         user = serializer.save()
         
         return Response({'message': 'Comment posted successfully'}, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def newPost(request):
    # print('request accepted')
    # serializer = PostSerializer(data = request.data)
    # print(request.data, 'valid? ',serializer.is_valid())

    content = request.data.get('content')
    by = request.data.get('by')
    by_name = request.data.get('by_name')
    likes = request.data.get('likes')
    shares = request.data.get('shares')
    # if request.FILES.image:
    #  image = request.FILES.get('image')
    # else:
    #  image= null -- TO BE WORKED ON...

    # Assuming you have a serializer for the Post model called PostSerializer
    serializer = PostSerializer(data={
        'content': content,
        'by': by,
        'by_name': by_name,
        'likes': likes,
        'shares': shares,
        #'image':request.FILES.get('image'),
    },)
    
    if serializer.is_valid():
         post = serializer.save()
        #  if image:
        #      post.image = image
        #      post.save()
         
         return Response({'message': 'Posted successfully'}, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        # Perform any validation or permission checks here
        # (e.g., check if the user has permission to delete the post)

        post.delete()
        return Response({'message': 'Post deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    except Post.DoesNotExist:
        return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def likePost(request,postpk,accountpk):
   try:
       post = Post.objects.get(pk=postpk) 
       try: 
        account = Account.objects.get(pk=accountpk)
        if not post.AccountsLiked.filter(pk=accountpk).exists():
          post.AccountsLiked.add(account)
          post.likes = post.AccountsLiked.count()
          post.save()
          return Response({'message': 'Post liked'}, status=201)
        
        return Response({'message': 'Post liked already'}, status=201)
       except Account.DoesNotExist:
         return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
   except Post.DoesNotExist:
        return Response({'message': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
      
@api_view(['PUT'])
def likeComment(request,compk,accountpk):
   try:
       comment = Comment.objects.get(pk=compk) 
       try: 
        account = Account.objects.get(pk=accountpk)
        if not comment.AccountsLiked.filter(pk=accountpk).exists():
          comment.AccountsLiked.add(account)
          comment.likes = comment.AccountsLiked.count()
          comment.save()
          return Response({'message': 'Comment liked'}, status=201)
        
        return Response({'message': 'Comment liked already'}, status=201)
       except Account.DoesNotExist:
         return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
   except Comment.DoesNotExist:
        return Response({'message': 'Comment not found'}, status=status.HTTP_404_NOT_FOUND)
   

@api_view(['PUT'])
def likeReply(request,reppk,accountpk):
   try:
       reply = Reply.objects.get(pk=reppk) 
       try: 
        account = Account.objects.get(pk=accountpk)
        if not reply.AccountsLiked.filter(pk=accountpk).exists():
          reply.AccountsLiked.add(account)
          reply.likes = reply.AccountsLiked.count()
          reply.save()
          return Response({'message': 'Reply liked'}, status=201)
        
        return Response({'message': 'Reply liked already'}, status=201)
       except Account.DoesNotExist:
         return Response({'message': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)
   except Reply.DoesNotExist:
        return Response({'message': 'Reply not found'}, status=status.HTTP_404_NOT_FOUND)
      