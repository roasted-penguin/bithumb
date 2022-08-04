from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
import pybithumb

apikey = ""
seckey = ""
bithumb = pybithumb.Bithumb(apikey, seckey)

@csrf_exempt
def login(request):
    if request.method == 'GET':
        content = f'''
        <form action="/login/" method="post">
            <p><input type="text" name = "apikey" placeholder="api key"></p>
            <p><input type="text" name = "seckey" placeholder="secret key"></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(content)
    elif request.method == 'POST':
        global apikey, seckey
        apikey = request.POST['apikey']
        seckey = request.POST['seckey']

        f = open("ki.txt", 'r')
        apik = f.readline().strip()
        seck = f.readline().strip()
        f.close()

        if apik == apikey and seck == seckey:
            apikey = apik
            seckey = seck
            return redirect('/index')
        else:
            return redirect('/')

@csrf_exempt
def index(request):
    article = ''
    for ticker in pybithumb.get_tickers() :
        balance = bithumb.get_balance(ticker)
        article += f'''<li>{ticker}:{str(balance)}</1i>'''
    return HttpResponse(article)
