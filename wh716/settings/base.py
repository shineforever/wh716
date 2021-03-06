#! coding: utf-8
"""
Django settings for wh716 project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).split('/')[:-1]
BASE_DIR = ('/').join(BASE_DIR)
sys.path.insert(0,os.path.join(BASE_DIR,'apps'))   #多个app集中放入到apps目录下时需要
sys.path.insert(0,os.path.join(BASE_DIR,'extra_apps'))  # 添加extra_apps目录到环境变量；
# print BASE_DIR
# print os.path.join(BASE_DIR,'../apps')
# print os.path.join(BASE_DIR,'../extra_apps')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^4%=$7tbbn@=wa&^#b#t1i$1(m_1*z8!(_vvm2q-4i%h!ycq$r'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

#重载user模块,APP名称+class
AUTH_USER_MODEL = "users.UserProfile"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'qiniustorage',
    'users',
    'baoming',
    'xadmin',
    'crispy_forms',

]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wh716.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',   #配置这行让html支持 MEDID_URL
            ],
        },
    },
]

WSGI_APPLICATION = 'wh716.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'wh716',    ## 数据库名称
        'USER': 'root',
        'PASSWORD': '!@#QWE',    ## 安装 mysql 数据库时，输入的 root 用户的密码
        'HOST': '127.0.0.1',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'  #中文支持，django1.8以后支持；1.8以前是zh-cn

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False   #默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#
# STATICFILES_DIRS = [
#     (os.path.join(BASE_DIR, 'static'))
# ]
#
# #文件上传路径
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')

#七牛云相关参数配置：

#七牛给开发者分配的 AccessKey
QINIU_ACCESS_KEY = ""
#七牛给开发者分配的 Secret
QINIU_SECRET_KEY = ""
#用来存放文件的七牛空间(bucket)的名字
QINIU_BUCKET_NAME = "test"
#对象存储对应的域名
QINIU_BUCKET_DOMAIN = "static.wh716.info"
#是否通过 HTTPS 来访问七牛云存储上的资源(若为'是', 可填True, true 或 1；若为'否', 可填False, false 或 0) 默认为否
QINIU_SECURE_URL = False

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = '/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = 'http://img.wh716.info/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = '/static/'

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = 'http://static.wh716.info/static/'


#存放用户上传的资源，如图片；
DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'
#存放js，css等静态资源
STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'