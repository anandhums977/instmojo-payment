from django.shortcuts import render,redirect
from instamojo_wrapper import Instamojo

# API_KEY ='test_b2ccbec82235d11b609cbb10869'
# AUTH_TOKEN = 'test_44581cb098b82108afc82655aea'
API_KEY ='test_bbc8a301db5f633726f8f9467ae'
AUTH_TOKEN = 'test_0e24c51bc615429e6e9f6cf7e13'


# Create your views here.
api = Instamojo(api_key=API_KEY,auth_token=AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')

def checkout(request):
    if request.POST:
        name = request.POST['name']
        purpose = request.POST['purpose']
        email = request.POST['email']
        amount = request.POST['amount']
        response = api.payment_request_create(
            amount=amount,
            purpose=purpose,
            buyer_name=name,
            send_email=True,
            email=email,
            redirect_url='http://127.0.0.1:8003/success/'
        )
        print(response)
        #52ec3d47a1ac4de5bbf7ba782ec996fe
        return redirect(response['payment_request']['longurl'])

    return render(request,'pay.html')


def success(request):
    print(request.GET['payment_request_id'])

    return render(request,'success.html')

    