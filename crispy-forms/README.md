# Django Crispy Forms Sampe

This is a sample of Django Crispy Forms rendering Twitter Bootstrap3 template.

Tired of copying template snippets from Bootstrap website? Crispy can easily 
substitute the outdates "as_p()" or "as_table()" generating instead Bootstrap3 form elements for you.

The steps are as follow:

- pip install django-crispy-forms
- on settings.py add it to INSTALLED_APPS = (..., crispy_forms,)
- still on settings.py, create a constant to set the render template CRISPY_TEMPLATE_PACK = 'bootstrap3'
- load Crispy on your templates with {% load crispy_forms_tags %}
- get the formset you and render it with crispy using {{ form|crispy }}


Is there anything wrong or could anything be done better?

Fork/Fix it! Pull requests are welcome :)

If you prefer, open an issue or contact me at menezes.victor@gmail.com
