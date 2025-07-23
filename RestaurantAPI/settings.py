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
    "apiyummy.pythonanywhere.com",
    "localhost",
    "127.0.0.1",
]


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "drf_spectacular",
    
    # Customs apps
    "API",
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
    "Users.middleware.AutoLogoutMiddleware",  # Middleware personalizado en la app Users
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
            "NAME": "apiyummy$default",
            "USER": env("USER"),
            "PASSWORD": env("PASSWORD"),
            "HOST": "apiyummy.mysql.pythonanywhere-services.com",
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
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",  # Para autenticación básica HTTP
        "rest_framework.authentication.SessionAuthentication",  # Para autenticación basada en cookies (sessionid)
    ),
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


JAZZMIN_SETTINGS = {
    "site_title": "Yummy API",
    "site_header": "Admin Yummy API",
    "site_brand": "Admin Yummy API",
    "site_icon": "img/icon-32x32.png",
    "site_logo": "img/Yummy-foto.png",
    "welcome_sign": "Admin Yummy API",
    # Links to put along the top menu
    "topmenu_links": [
        {"app": "API"},
        {
            "name": "GitHub Code",
            "url": "https://github.com/CristianEduardoo/Restaurant-API",
            "new_window": True,
        },
    ],
    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [
        # "Users",
    ],
    # Personalizar iconos del menú lateral
    "icons": {
        "API.entrantes": "fas fa-utensils",  # Icono de utensilios de cocina
        "API.principales": "fas fa-hamburger",  # Icono de hamburguesa
        "API.postre": "fas fa-ice-cream",  # Icono de helado
        "API.bebida": "fas fa-coffee",  # Icono de taza de café
        "API.precio": "fas fa-dollar-sign",  # Icono de signo de dólar
    },
    # Ordenar los modelos según tus preferencias
    "order_with_respect_to": [
        "API.entrantes",
        "API.principales",
        "API.postre",
        "API.bebida",
        "API.precio",
    ],
}


JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": False,
    "sidebar": "sidebar-dark-success",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": False,
    "theme": "cosmo",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary rounded-sm",
        "secondary": "btn-outline-secondary rounded-sm",
        "info": "btn-outline-info rounded-sm",
        "warning": "btn-outline-warning rounded-sm",
        "danger": "btn-outline-danger rounded-sm",
        "success": "btn-outline-success rounded-sm",
    },
}
