from configs.default import *  # noqa
import os

DEBUG = False

SENTRY_DSN = os.environ["SENTRY_DSN"]

DB_HOST = os.environ["DB_HOST"]
DB_NAME = os.environ["DB_NAME"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
PW_DB_URL = "mysql+pool://{user}:{password}@{host}/{name}".format(
    host=DB_HOST, name=DB_NAME, user=DB_USER, password=DB_PASSWORD
)

CACHE_HOST = os.environ["CACHE_HOST"]
CACHE_PASSWORD = os.environ["CACHE_PASSWORD"]

CELERY_BROKER_URL = os.environ["CELERY_BROKER_URL"]

MEDIA_PUB_IMG_BUCKET = "media-image1"
MEDIA_PUB_AUD_BUCKET = "media-audio1"
MEDIA_PUB_VID_BUCKET = "media-video1"

MEDIA_PRI_IMG_BUCKET = "media-image0"
MEDIA_PRI_AUD_BUCKET = "media-audio0"
MEDIA_PRI_VID_BUCKET = "media-video0"

MEDIA_QINIU_ACCESS_KEY = os.environ["MEDIA_QINIU_ACCESS_KEY"]
MEDIA_QINIU_SECRET_KEY = os.environ["MEDIA_QINIU_SECRET_KEY"]

MEDIA_ALIYUN_ACCESS_ID = os.environ["MEDIA_ALIYUN_ACCESS_ID"]
MEDIA_ALIYUN_SECRET_KEY = os.environ["MEDIA_ALIYUN_SECRET_KEY"]

MEDIA_KEY_SECRET = os.environ["MEDIA_KEY_SECRET"]
MEDIA_SIGN_SECRET = os.environ["MEDIA_SIGN_SECRET"]

MEDIA_ALIYUN_CDN_SIGN_KEY = os.environ["MEDIA_ALIYUN_CDN_SIGN_KEY"]
MEDIA_QINIU_CDN_SIGN_KEY = {
    MEDIA_PRI_IMG_BUCKET: os.environ["MEDIA_QINIU_CDN_SIGN_KEY_PRI_IMG"],
    MEDIA_PRI_AUD_BUCKET: os.environ["MEDIA_QINIU_CDN_SIGN_KEY_PRI_AUD"],
    MEDIA_PRI_VID_BUCKET: os.environ["MEDIA_QINIU_CDN_SIGN_KEY_PRI_VID"],
}

JWT_SECRET = os.environ["JWT_SECRET"]

SHANBAY_LOGIN_URL = "https://www.shanbay.com/api/v1/account/login/"
SHANBAY_ACCOUNT = "douyatest1"
SHANBAY_PASSWORD = "douyatest123456"

WECHAT_MINI_APP_CLIENT_ID = os.environ["WECHAT_MINI_APP_CLIENT_ID"]
WECHAT_MINI_APP_CLIENT_SECRET = os.environ["WECHAT_MINI_APP_CLIENT_SECRET"]
