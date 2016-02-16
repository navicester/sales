from settings import *


DEBUG = TEMPLATE_DEBUG = True

MEDIA_ROOT = ''

SESSION_COOKIE_AGE = 60 * 60 * 24 * 14

#STATIC_ROOT = 'E:/PythonWeb/code/voith_sales/Rail/static'
#SETTINGS_PATH = os.path.normpath(os.path.dirname(__file__))  
#STATIC_ROOT = os.path.join(SETTINGS_PATH, '../static')
STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')

STATICFILES_DIRS = (  
    # Put strings here, like "/home/html/static" or "C:/www/django/static".  
    # Always use forward slashes, even on Windows.  
    # Don't forget to use absolute paths, not relative paths.  
    "d:/Python27/Lib/site-packages/django/contrib/admin/static/",  
)

STATICFILES_FINDERS = (  
    'django.contrib.staticfiles.finders.FileSystemFinder',  
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',  
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',  
) 

