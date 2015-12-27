# Integrating Braintree Payments System to Django

This is mainly a python sample, there is nothing Django specific on this code. We 
are just using Django to render HTML/CSS


## Setup Django project

```
virtualenv -p python3 env
source env/bin/activate
pip install django
pip install braintree
django-admin startproject myproj
cd myproj
python manage.py startapp app
mkdir app/templates
touch app/templates/base.html
touch app/templates/home.html
touch app/api_keys.json
```

All installed, project created, not lets start coding. First, append 'app' to our `INSTALLED_APPS` on settings.py. 
Go to Braintree website and register a sandbox. On your sandbox dashboard, look for "Sandbox Keys & Configuration". 
You are going to need Merchant ID, Public Key and Private Key.

Edit the `app/api_keys.json` that we created before as:

```
{
    "merchant_id": "MERCHANT ID",
    "public_key": "PUBLIC KEY",
    "private_key": "PRIVATE KEY"
}
```

## Create the  templates

The app will have just one page, where the user pays. Following a sample `app/templates/base.html`:

```
{% load staticfiles %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <title>Braintree Payments Sample</title>

    <!-- Bootstrap -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
    
    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
  </head>
  <body>
    
    {% block main_content %}
    {% endblock %}

    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
  </body>
</html>
```

And a sample of the Braintree form `app/templates/home.html`:

```
{% block main_content %}
    <form id="checkout" method="post" action="/checkout/">
      {% csrf_token %}
      <div id="payment-form"></div>
      <input type="number" name="amount" id="amount" placeholder="11.99" "required"/>
      <input type="submit" value="Pay!">
    </form>

    <script src="https://js.braintreegateway.com/v2/braintree.js"></script>
    <script>
    // We generated a client token for you so you can test out this code
    // immediately. In a production-ready integration, you will need to
    // generate a client token on your server (see section below).
    var clientToken = "{{ client_token }}";

    braintree.setup(clientToken, "dropin", {
      container: "payment-form"
    });
    </script>

{% endblock %}
```

## Now lets add the Braintree Python integration

Edit `app/views.py` as:

```
from django.shortcuts import render, redirect
from django.views.generic import View
import json
import braintree

with open('app/api_keys.json') as json_data:
    api_keys = json.load(json_data)

braintree.Configuration.configure(braintree.Environment.Sandbox,
    merchant_id = api_keys['merchant_id'],
    public_key = api_keys['public_key'],
    private_key = api_keys['private_key']
)

class HomeView(View):
    def get(self, request):
        context = {"client_token": braintree.ClientToken.generate()}
        return render(request, 'home.html', context)
    
class CheckoutView(View):
    def post(self, request):
        nonce = request.POST.get("payment_method_nonce")
        amount = request.POST.get("amount")
        result = braintree.Transaction.sale({
            "amount": amount,
            "payment_method_nonce": nonce
        })
        return redirect('/')
```

## Finalize hooking the URLs

Edit `myproj.settings.py` as follows:

```
from django.conf.urls import url
from django.contrib import admin
from app.views import HomeView, CheckoutView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^checkout/', CheckoutView.as_view()),
    url(r'^$', HomeView.as_view()),
]
```

## So, where is my money!?

That is it! `python manage.py runserver` and go to http://localhost:8000

You sould see a Braintree form but don't waste your time(like I did), trying to fill the form, the sandbox doesn't take real cards. 
Just fill the card number as `4111 1111 1111 1111`, add some valid expiration date/amount and submit. It may take few seconds processing and just clear the form right? Well, on Braintree dashboard just look for the transaction you just did, you may be rich :)


Is there anything wrong or could anything be done better?

Fork/Fix it! Pull requests are welcome :)

If you prefer, open an issue or contact me at menezes.victor@gmail.com