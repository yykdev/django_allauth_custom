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
        request.user.last_name = sociallogin.account.extra_data['username']
        request.user.save()
        # 업데이트 잘 됨

        # pre_social_login호출 후 자동으로 /accounts/social/signup/가 아닌
        # 로그인 세션을 유지하면서 다른 url 로 리다이렉트 할 방법은 무엇인가??

    # is_open_for_signup 함수를 오버라이드 하여 False를 return 하게 되면
    # /accounts/social/signup/로 리다이렉트 되면서
    # 회원 가입이 종료 되었다는 메시지가 출력 됨
    # def is_open_for_signup(self, request, sociallogin):
    #     return False