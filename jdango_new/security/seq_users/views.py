import json
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from security.seq_users.models import SeqUser
from security.seq_users.repositories import SeqUserRepository
from security.seq_users.serializers import SeqUserSerializer
from security.seq_users.services import SeqUserService
from rest_framework.authtoken.models import Token

# Create your views here.
@api_view(["POST","PUT","PATCH","DELETE","GET"])
@parser_classes([JSONParser])
def sequser(request):
    if request.method == 'POST':
        new_user = request.data
        print(f"리액트에서 들옥한 신규 사용자 {new_user}")
        serializer = SeqUserSerializer(data=new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : 'SUCCESS'})
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        return None
    elif request.method == 'PUT':
        repo = SeqUserRepository()
        modify_user = repo.find_user_by_email(request.data["user_email"]) # 리액트
        db_user = repo.find_by_id(modify_user.id)
        serializer = SeqUserSerializer(data=db_user)
        if serializer.is_valid():
            serializer.update(modify_user,db_user)
            return JsonResponse({'result' : 'SUCCESS'})

    elif request.method == 'DELETE':
        repo = SeqUserRepository()
        delete_user = repo.find_user_by_email(request.data["user_email"])  # 리액트
        db_user = repo.find_by_id(delete_user.id)
        db_user.delete()
        return JsonResponse({'result': 'SUCCESS'})
    elif request.method == 'GET':
        return Response(SeqUserRepository().find_user_by_email(request.data['user_email']))

@api_view(["GET"])
@parser_classes([JSONParser])
def sequser_list(request):
    return SeqUserRepository().get_all()



@api_view(["POST"])
@parser_classes([JSONParser])
def login_seq(request):
    return SeqUserRepository().login(user_email = request.data['user_email'],password = request.data['password'])


@api_view(["GET"])
@parser_classes([JSONParser])
def list_by_name(request):
    return Response(SeqUserRepository().find_user_by_name(request.data["user_name"]))

@api_view(["GET"])
@parser_classes([JSONParser])
def list_by_job(request):
    return Response(SeqUserRepository().find_user_by_name(request.data["job"]))

@api_view(["GET"])
@parser_classes([JSONParser])
def exist_email(request, email):
    exist = SeqUser.objects.all().filter(user_emial = email).values()[0]
    if not email == exist['user_email']:
        return JsonResponse({"result": "SUCESS"})

## REST API 보안
    '''
    iss: 토큰 발급자 (issuer)
    sub: 토큰 제목 (subject)
    aud: 토큰 대상자 (audience)
    exp: 토큰의 만료시간 (expiraton), 시간은 NumericDate 형식으로 되어있어야 하며 (예: 1480849147370) 언제나 현재 시간보다 이후로 설정되어있어야합니다.
    nbf: Not Before 를 의미하며, 토큰의 활성 날짜와 비슷한 개념입니다. 여기에도 NumericDate 형식으로 날짜를 지정하며, 이 날짜가 지나기 전까지는 토큰이 처리되지 않습니다.
    iat: 토큰이 발급된 시간 (issued at), 이 값을 사용하여 토큰의 age 가 얼마나 되었는지 판단 할 수 있습니다.
    jti: JWT의 고유 식별자로서, 주로 중복적인 처리를 방지하기 위하여 사용됩니다. 일회용 토큰에 사용하면 유용합니다.



    # Header ############################
    {
        "alg": "HS256",
        "typ": "JWT"
    }

    # Payload ###########################
    {
        "sub": "1234567890",
        "name": "John Doe",
        "iat": 1516239022
    }

    # Signature #########################
    HMACSHA256(
      base64UrlEncode(header) + "." +
      base64UrlEncode(payload),
      secret)'''
