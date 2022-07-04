"""
Django settings for probono_fire project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
from pathlib import Path

import os , environ
from django.urls import reverse_lazy
env=environ.Env(
    #set casting , default value
    DEBUG=(bool,False)
)
#env 안에 env파일에서 secret키를 가져온다.
#Build paths inside the project like this:Base_dir
BASE_DIR=Path(__file__).resolve().parent.parent
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))

#reading.env file
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR,'.env')
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

#문제해결SECRET_KEY = env('SECRET_KEY')

#배포 할 때 노출 시키면 안됌 
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.environ.get('SECRET_KEY'))
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appaccount',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'probono_fire.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'probono_fire.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#명g령어를 통해서 스테틱 파일이 어디있는지 알려줌  STATIC_ROOT='staticfiles'
STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles')
#앱에 종속되지 않은 static폴더를 따로 만들어줌  각종 이미지, CSS 등을 한군데 모아주는 역할을 하며개발 단계에서는 잘 안하고 배포단계에서 주로 하더라구요
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static') ,
   #BASE_DIR / "static"  하면안됌 
]



#로그인 추가 
LOGIN_REDIRECT_URL = reverse_lazy('appaccount:hello_world')
LOGOUT_REDIRECT_URL = reverse_lazy('appaccount:login')