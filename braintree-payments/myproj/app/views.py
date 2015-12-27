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

