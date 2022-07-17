#
# class Settings(BaseSettings):
#
#     # Metadata
#     appTitle: str = "Goodpods-V2-API: Sanic"
#     appDescription: str = "Welcome to the auto-docs for Sanic, the Goodpods V2 API"
#     appVersion: str = get_version()
#
#     # GCP project name
#     #  Note that this (and environment type) must be defined either in
#     #   config.py or an .env file, so that we can load other vars from
#     #   google's secrets manager thingy. @see get_settings
#     PROJECT_NAME ="seismic-handler-240905"
#
#     # Development
#     DEBUG: bool = False
#     ENVIRONMENT_TYPE: str = EnvironmentTypes.local
#     LOCAL_DEV: bool = False  # Used by Sam's local env
#
#     # If this is true, tests marked with @mark.slow will not be run by default
#     # and you'll need to use 'pytest --slow' to run them
#     SKIP_SLOW_TESTS: bool = False
#
#     # Constants:
#
#     # NOTE: This *MUST* end with a slash!
#     BUCKET_BASE_URL: str = "https://storage.googleapis.com/goodpods-images-bucket/"
#
#     SLACK_WEBHOOK_QUEUES_URL: str = "https://hooks.slack.com/services/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"
#     FAILURE_TTL: int = 86400 * 2  # Time to keep failed jobs (2 days)
#     # CORS exceptions for v2-endpoint
#     GOODPODS_ADMIN = 'https://admin.goodpods.com'
#     UAT_ADMIN = 'http://uatadmin.goodpods.com'
#     DEV_ADMIN = 'http://devadmin.goodpods.com'
#     WEBAPP_DEV = 'https://goodpods-web.uc.r.appspot.com'
#
#     # Connection to Local TestDB
#     DATABASE_HOST: str = 'localhost'
#     DATABASE_USER: str = 'postgres'
#     DATABASE_PASSWORD: str = 'cognativ28'
#     DATABASE_NAME: str = 'django'
#     DATABASE_CONNECTION_TYPE: str = 'appengine'  # 'postgres' or 'appengine' to set connection string format.
#
#     # Connection to Elastic
#     ELASTIC_PROTOCOL: str = 'https'
#     ELASTIC_HOST: str = 'localhost'
#     ELASTIC_PORT: str = '9250'
#     ELASTIC_USER: str = 'elastic'
#     ELASTIC_PASSWORD: str = 'localpassword'
#
#     # settings for elastic
#     ELASTIC_USER_PROFILE_INDE X ='user_profiles'
#     ELASTIC_PODCAST_EPISODE_INDE X ='podcast_episodes'
#
#     # Redis task queue connection
#     PYTHON_RQ_HOST: str = 'localhost'
#
#     # Password for endpoints
#     ADMIN_AUTH_PASSWORD: str = 'cognativ28'
#
#     # Database to use in manual scripts
#     SCRIPT_DB_USER: str = "XXX"
#     SCRIPT_DB_PASSWORD: str = "XXX"
#     SCRIPT_DB_HOST: str = "XXX"
#     SCRIPT_DB_NAME: str = "XXX"
#
#     # API Keys (.env)
#     HTML_CSS_TO_IMAGE_USER_ID: str = "XXX"
#     HTML_CSS_TO_IMAGE_API_KEY: str = "XXX"
#     BRANCHIO_API_KEY: str = "XXX"
#     SHORT_PIXEL_API_KEY: str = "XXX"
#
#     # The default storage auth file in the repo is just a placeholder and not useful.
#     # You should set this var in your .env file to point to a service account key file
#     #   You can get a keyfile from the server, it's called storage-auth.json.
#     GOOGLE_CLOUD_AUTH_JSON_LOCATION: str = "default-storage-auth.json"
#     SENDGRID_API_KEY = "XXX"
#     KRAKEN_API_KEY = "XXX"
#     KRAKEN_API_SECRET = "XXX"
#     SENTRY_DSN_KEY = "XXX"
#
#     ########################
#     # Firebase settings
#     #
#     # The location of the key file to use for authenticating the firebase
#     #   service account.
#     #
#     # you should download a key file from:
#     #
#     # https://console.firebase.google.com/project/seismic-handler-240905/settings/serviceaccounts/adminsdk
#     #
#     #  and then put it in v2-api/sanic/ with this filename
#     FIREBASE_SERVICE_ACCOUNT_KEY_FILE = ".firebase-secret.json"
#
#     # The project ID for firebase auth.
#     # This should be populated automatically from the service account info,
#     #   but we specify it to be sure.
#     FIREBASE_PROJECT_ID = 'seismic-handler-240905' # we specify the project ID to avoid any ambiguity.
#
#     # UID used for the firebase guest user (in users_user.firebase_uid, we
#     #   pretend all firebase users have this UID)
#     FIREBASE_GUEST_UID = "_GUEST_USER_"
#
#     #
#     ########################
#
#     # Twitter Keys
#     TWITTER_CLIENT_I D ='XXX'
#     TWITTER_CLIENT_SECRE T ='XXX'
#
#     # Sendgrid settings
#     FROM_EMAIL = 'hello@goodpods.com'
#     UNSUBSCRIBE_GROUP_ID = 13738
#
#     ########################
#     # SENDGRID EMAIL TEMPLATE IDS
#
#     # This is a blank template intended for sending reports on automated tasks.
#     # Give it a 'html' variable with your report.
#     TASK_REPORT_TEMPLATE_ID = "d-da5279c96d6a452ab591286e04f2bfe1"
#
#     FIRST_WELCOME_EMAIL_ID = "d-50298367afab452abfef91e514722713"
#     SECOND_WELCOME_EMAIL_ID = "d-ee8cdd2029414c3190d2bfd5e2777057"
#     THIRD_WELCOME_EMAIL_ID = "d-f7d6621059014399b004e02a810deb3e"
#     GROUP_JOIN_MEMBER_ID = "d-9c22176942134ba9a48fcde26688e803"
#     GROUP_CREATED_ADMIN_ID = "d-89c468fb221a47d1a425eca154a88e65"
#     GROUP_TWO_WEEKS_NO_MEMBERS_ID = "d-b645bc014240403597233e032c49305e"
#     GROUP_TWO_MONTHS_NO_MEMBERS_ID = "d-ad7548e241c246ca958b7c728c1e8159"
#     WEEKLY_EMAIL_ID = "d-1a72bc1747ca4432871881db55b32fe1"
#     PODCAST_CLAIM_VERIFICATION_EMAIL_ID = "d-2d614234b2994f7c9c9f57f1d6789139"
#
#     LEADERBOARD_EMAIL_TEMPLATE_ID = "d-232aa90742374197a93cdbabf5d0aa5a"
#
#     RESET_PASSWORD_TEMPLATE_ID = 'd-4ca240703ac2414d8549b22d509897f2'
#     # this is a "you need to use <provider> to reset your password" email:
#     RESET_PASSWORD_WITH_SOCIAL_TEMPLATE_ID = 'd-d99c1ee998f14e76a9ffc8ea3541f3b1'
#
#     ########################
#
#     # Push Notifications
#
#     # Android
#     FCM_API_KEY = "xxx"
#
#     # iOS
#     TEAM_ID = "P7XBNL3JZG"
#     BUNDLE_ID = "com.goodsearch.goodpods"
#     APNS_KEY_ID = "XXX"
#     APNS_KEY = "XXX"
#
#     # For Groups Photo uploads
#     BUCKET_NAME = 'goodpods-images-bucket'
#     GROUPS_BUCKET_FOLDER_NAME = 'groups_images'
#
#     # For User Profile photo Upload
#     USER_BUCKET_FOLDER_NAME = 'user_images'
#     # API supported versions
#     # Ideally this would be a list, but we need it to be parseable in .env,
#     # so it's a comma-separated string:
#     SUPPORTED_API_VERSIONS = '21,22,23,24,25'
#
#     # default initial recommendations:
#     INITIAL_RECOMMENDED_EPISODE_ID = 20298479
#
#     # default profile pic path
#     DEFAULT_PROFILE_IMAGE = "default_profile/default_profile.png"
#
#     class Config:
#         env_file = ".env"
#
#     def __getitem__(self ,key):
#         """
#         You can access settings as if it was a dict
#         some_value = settings['SOME_SETTING']
#         """
#         if key in self.__dict__: return self.__dict__[key]
#
#     def __setitem__(self ,key ,val):
#         """
#         You can set a settings value as if settings was a dict:
#         settings['SOME_SETTING'] = some_value
#         """
#         self.__dict__[key] = val
