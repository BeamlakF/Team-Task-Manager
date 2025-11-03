## Team Task Manager -- Cleaning Up after my Django skills



###  1. **Core Django Fundamentals **

* **Django project structure** (`manage.py`, `settings.py`, `urls.py`, `wsgi.py`)
* **App structure** (`models.py`, `views.py`, `urls.py`, `admin.py`)
* **Request–Response cycle** in Django
* **URL routing & path converters**
* **Static & media files handling**
* **Template rendering** — using `{% %}` and `{{ }}`, `extends`, `include`, `block`, etc.
* **Django settings** (like `INSTALLED_APPS`, `DATABASES`, `TEMPLATES`)

---

### 🗃️ 2. **Models and ORM **

* **Defining models**

* **Model field types & options** (`CharField`, `TextField`, `DateTimeField`, `ForeignKey`, `ManyToManyField`)
* **Migrations** (`makemigrations`, `migrate`, `showmigrations`)
* **QuerySet methods** (`filter()`, `get()`, `exclude()`, `values()`, `order_by()`)
* **Model relationships** (OneToOne, OneToMany, ManyToMany)
* **Meta class & `__str__` method**
* **Signals (optional but good to mention)**

---

### ⚙️ 3. **Views and URL Dispatching **

* Function-based views (FBV)
* Class-based views (CBV)
* Difference between `render()`, `redirect()`, and `HttpResponse`
* `request.GET` vs `request.POST`
* `@login_required` and other decorators
* URL parameters: `path('books/<int:id>/', views.detail, name='detail')`

---

### 🎨 4. **Templates and Context **

* Template inheritance (`{% extends 'base.html' %}`)
* Template filters (`|upper`, `|date`, etc.)
* Template tags (`{% if %}`, `{% for %}`, `{% url 'name' %}`)
* Passing context from view to template
* Loading static files `{% load static %}`

---

### 🔐 5. **Authentication and Authorization **

* Django’s built-in `User` model
* Login, logout, and signup flows
* `@login_required` decorator and permission checks
* Using `AUTH_USER_MODEL`
* Session vs token authentication basics (if you covered REST)

---

### 🔄 6. **Forms and Validation **

* `forms.Form` vs `forms.ModelForm`
* Form rendering in templates
* Handling `POST` requests and CSRF
* Form validation (`clean()`, `clean_fieldname()`)

---

### 🌐 7. **Django REST Framework **

* Serializers (ModelSerializer vs Serializer)
* Views (`APIView`, `GenericView`, `ViewSet`)
* Routers
* Authentication (SessionAuth, TokenAuth, JWT)
* Permissions (`IsAuthenticated`, `IsAdminUser`, custom permissions)

---

### 🧠 8. **Deployment & Extras**

* Environment variables (`.env`)
* Using `DEBUG` and `ALLOWED_HOSTS`
* Connecting to PostgreSQL or MySQL
* Static files in production (`collectstatic`)
* Admin customization (`list_display`, `search_fields`)

---

### 🔍 Study Strategy

1. **Revise small project** — build or revisit one CRUD project (e.g. a library/bookstore).
2. **Do a dry run:** `python manage.py startapp testapp` and re-create models, URLs, and views from memory.
3. **Read through settings.py** — understand every section.
4. **Skim Django docs:** especially *Models*, *Views*, and *Templates*.

---
