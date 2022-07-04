from django import forms
from django.contrib.auth.forms import UserCreationForm

# 유저 정보 변경
class AccountUserUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #입력 불가능
        self.fields['username'].disabled = True
        #help_text
        self.fields['username'].help_text = "아이디는 변경 불가능 합니다"
        self.fields['password1'].help_text = "특수문자,숫자,문자 모두 포함해야 합니다"
        self.fields['password2'].help_text = "패스워드를 다시 입력하세요"
        #rename
        self.fields['username'].label="아이디"
        self.fields['password1'].label="패스워드"
        self.fields['password2'].label="패스워드확인"
        
class AccountUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #help_text
        self.fields['username'].help_text = ""
        self.fields['password1'].help_text = "특수문자,숫자,문자 모두 포함해야 합니다"
        self.fields['password2'].help_text = "패스워드를 다시 입력하세요"
        #rename
        self.fields['username'].label="아이디"
        self.fields['password1'].label="패스워드"
        self.fields['password2'].label="패스워드확인"