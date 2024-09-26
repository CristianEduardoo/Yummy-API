from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Variables Globales
env = environ.Env()
env_file = os.path.join(BASE_DIR, ".env")  # Asegúrate que la ruta aquí sea correcta
env.read_env(env_file)  # Lee el archivo .env desde la ruta especificada

ENVIRONMENT = env("ENVIRONMENT", default="production")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
if ENVIRONMENT == "development":
    DEBUG = True
else:
    DEBUG = False


ALLOWED_HOSTS = [
    "restaurantapi.pythonanywhere.com",
    "localhost",
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    "API",  # aplicacion creada para la API
    "Users",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "Users.middleware.AutoLogoutMiddleware",  # Middleware personalizado en la app users
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    "GET",
]

ROOT_URLCONF = 'RestaurantAPI.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")], # Referenciando a todos los templates del directorio
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'RestaurantAPI.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

if ENVIRONMENT == "development":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "DDBB_Restaurant_API",
            "USER": "root",
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "3306",
        }
    }
else :
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "yummy$default",
            "USER": env("USER"),
            "PASSWORD": env("PASSWORD"),
            "HOST": "yummy.mysql.pythonanywhere-services.com",
            "PORT": "3306",
        }
    }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),  # first 1
]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =============== LOGIN =============== #
LOGIN_REDIRECT_URL = "/admin/" # Donde el usuario autenticado será redirigido después de iniciar sesión
LOGIN_URL = "login"  # Define la URL donde se encuentra el formulario de login
# Django redirigirá al usuario a la página de inicio de sesión, lo tiene por defecto, solo hay que crear el template

# =============== LOGOUT =============== #
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Esto garantiza que la sesión se cierre al cerrar el navegador.


# =============== AUTOESQUEMA => ARCHIVO DE DOCUMENTACIÓN DE LA API =============== #
REST_FRAMEWORK = {
    # "DEFAULT_PERMISSION_CLASSES": [
    #     "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    # ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


# Configuraciones por defecto:
SPECTACULAR_SETTINGS = {
    "TITLE": "Restaurant-API",
    "DESCRIPTION": "API del restaurante para gestionar el menú diario",
    "VERSION": "4.2.10",
    "SERVE_INCLUDE_SCHEMA": True,
}
# despues de incluir el AutoEsquema, generarlo => python3 manage.py spectacular --color --file schema.yml


# =============== Custom User =============== #
AUTH_USER_MODEL = "Users.User"
