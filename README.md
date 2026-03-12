
 
 A mini video blog platform built with **Django** and **Bootstrap 5** 
(RTL support).

## Features

- 🎥 Video listing with thumbnails
- 🔍 Search functionality
- 📱 Responsive dark theme design
- 🔄 Pagination with search persistence
- ♿ Accessibility optimized

## Requirements

```
asgiref==3.11.1
Django>=5.2,<6.1
pillow==12.1.1
psycopg2-binary==2.9.11
python-dotenv==1.2.2
sqlparse==0.5.5

```

## Project Structure

```
vidblog/
├── templates/          # HTML templates
│   └── index.html
|   └── watch.html
├── static/
│   └── css/
│       └── style.css  # Custom styles
|       └── watch.css
├── pages/
│   ├── models.py      # Video, Category models
│   ├── views.py       # Index, Watch views
│   └── urls.py        # URL routing
└── vidblog/
    └── settings.py    # Django settings
```

## Configuration

### Required Settings

```python
# settings.py
INSTALLED_APPS = [
    'pages.apps.PagesConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] 

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

### URL Configuration

```python
# urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

```

## Template Tags

| Tag | Description |
|-----|-------------|
| `{% url 'index' %}` | Home page |
| `{% url 'watch' video.slug %}` | Video player |
| `{{ query\|default:'' }}` | Search query |
| `{{ page_obj }}` | Paginator object |

## License

MIT License

---

Feel free to customize this with your actual repo URL, additional 
features, or specific setup instructions! 🚀

