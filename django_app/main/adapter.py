from django.conf import settings
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect


class DefaultSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        print('pre_social_login')
        print(sociallogin.account.extra_data)

        print(request.user)
        # 현재 로그인 돼 있는 계정의 특정 필드에 소셜 로그인 정보 업데이트
        # 새 계정 생성 아님

