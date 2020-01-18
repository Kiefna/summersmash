import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@bdo_hi=h4srg2dh1((o21svgj3mmhtyll3els@1j(@)tf7#ef'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
TEMPLATE_DEBUG = DEBUG

SIMPLE_SOCIALAUTH_SECURE = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.redirects',
    'bootstrap3',
    'django_extensions',
    'django_summernote',
    'pipeline'
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

ROOT_URLCONF = 'summersmash.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'summersmash.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

BOOTSTRAP3 = {
    'horizontal_label_class': 'col-sm-3',
    'horizontal_field_class': 'col-sm-9'
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '_static_root')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, '_static'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

# using these as finders prevents unnecessary copying of source
# css/less/js files to STATIC_ROOT
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.CachedFileFinder',
    'pipeline.finders.PipelineFinder'
)

PIPELINE = {
    # 'PIPELINE_ENABLED': True,
    'CSS_COMPRESSOR': 'pipeline.compressors.cssmin.CSSMinCompressor',
    'JS_COMPRESSOR': 'pipeline.compressors.uglifyjs.UglifyJSCompressor',
    'COMPILERS': [
        'pipeline.compilers.less.LessCompiler',
    ],
    'LESS_ARGUMENTS': '-ru',  # relative URLs in less/css files are rewritten appropriately
    'JAVASCRIPT': {
        'site': {
            'source_filenames': (
                '_src/vendor/jquery-3.3.1.js',
                '_src/vendor/jquery-migrate-3.0.0.js',
                '_src/vendor/jquery.cookie.js',
                '_src/vendor/bootstrap-4/js/bootstrap.js',
                '_src/vendor/select2/select2.js',
                '_src/vendor/moment.js',
                '_src/vendor/bootstrap-datetimepicker/bootstrap-datetimepicker.js',
                '_src/vendor/datetime-picker/jquery.pickmeup.twitter-bootstrap.js',
                '_src/vendor/datetime-picker/pickmeup.js',
                '_src/vendor/bootstrap-slider/bootstrap-slider.js',
                '_src/vendor/jquery-bar-rating/jquery.barrating.js',
                '_src/vendor/json2.js',
                '_src/vendor/history/history.adapter.jquery.js',
                '_src/vendor/history/history.js',
                '_src/vendor/social-likes/social-likes.js',
                '_src/vendor/jcrop/Jcrop.js',
                '_src/vendor/jdenticon.js',
                '_src/vendor/jquery.formset.js',
                '_src/vendor/jquery.mousewheel.js',
                '_src/vendor/velocity/velocity.min.js',
                '_src/vendor/velocity/velocity.ui.min.js',
                '_src/vendor/GSAP/TweenMax.js',
                '_src/vendor/scrollmagic/ScrollMagic.js',
                '_src/vendor/scrollmagic/plugins/animation.velocity.js',
                '_src/vendor/scrollmagic/plugins/jquery.ScrollMagic.js',
                '_src/vendor/scrollmagic/plugins/debug.addIndicators.js',
                '_src/vendor/fontawesome-pro-5.1.0-web/all.js',
                '_src/vendor/imagesloaded.pkgd.min.js',
                'summernote/summernote.min.js',
                '_src/js/site.js'
            ),
            'output_filename': 'js/site.js'
        }
    },
    'STYLESHEETS': {
        'site': {
            'source_filenames': (
                '_src/less/site.less',
            ),
            'output_filename': 'css/site.css',
            'extra_context': {
                'media': 'screen,projection'
            }
        }
    }
}

SUMMERNOTE_CONFIG = {
    'prettifyHtml': False,
    'iframe': False,
    'attachment_filesize_limit': 1024 * 1024 * 1024,
    'lazy': True,
    'summernote': {
        'lang': None,
        'disableDragAndDrop': True,
        'toolbar': [
            ['style', ['style']],
            ['style', ['bold', 'italic', 'underline', 'clear']],
            ['para', ['ul', 'ol', 'hr']],
            ['insert', ['link', 'picture', 'video']],
        ],
    },
    'codemirror': {
        'lineNumbers': 'true',
        'lineWrapping': True,
    }
}
