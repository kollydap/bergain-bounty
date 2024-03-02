from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer,EmailSerializer,ResetPasswordSerializer
from django.contrib.auth.models import User
from rest_framework import generics, viewsets
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode




@api_view(['GET'])
def list_user(request,username):
    user=User.objects.get(username=username)
    serializer=UserSerializer(user,many=False)
    if user:
        return Response(serializer.data)
    return Response("user does not exist")




@api_view(["POST"])
def login(request):
    #getting the user with the username
    user=get_object_or_404(User,username=request.data["username"])

    if not user.check_password(request.data['password']):

        return Response({"details": "Details Not Found"}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created=Token.objects.get_or_create(user=user)

    serializer=UserSerializer(instance=user)

    return Response({"token": token.key, "user":serializer.data})

    


@api_view(["POST"])
def signup(request):
    #creating an instance of the serializer based on the data passed
    serializer=UserSerializer(data=request.data)

    if serializer.is_valid():

        #saving the user object
        user=serializer.save()
        #hashing the user password

        user.set_password(request.data["password"])
        #saving the user
        user.save()
        #creating a token for the saved user
        token=Token.objects.create(user=user)
        #retrun a response with the token
        return Response({"token": token.key, "user": serializer.data})
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def log_out(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response({"Message": "you are logged out"}, status=status.HTTP_200_OK)


class PasswordReset(generics.GenericAPIView):

    serializer_class =EmailSerializer

    def post(self, request):
    
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.data["email"]
        user = User.objects.filter(email=email).first()
        if user:
            encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
            token = PasswordResetTokenGenerator().make_token(user)
            reset_url = reverse(
                "reset-password",
                kwargs={"encoded_pk": encoded_pk, "token": token},
            )
            reset_link = f"localhost:8000{reset_url}"

            # send the rest_link as mail to the user.

            return Response(
                {
                    "message": 
                    f"Your password rest link: {reset_link}"
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"message": "User doesn't exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )



class ResetPasswordAPI(generics.GenericAPIView):
    """
    Verify and Reset Password Token View.
    """

    serializer_class =ResetPasswordSerializer

    def patch(self, request, *args, **kwargs):
        
        
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Password reset complete"},
            status=status.HTTP_200_OK,
        )