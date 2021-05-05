# Author: Seth Kimpler

from django.contrib.auth import login, authenticate
from django.shortcuts import render, get_object_or_404, redirect
import requests

import yfinance as yf
from plotly.offline import plot
import plotly.express as px
import pandas as pd

from .models import GPUModel, Notification, populate
from .forms import UserForm

cryptos = ['BTC-USD', 'ETH-USD', 'LTC-USD']

'''
Functions for rendering pages
'''


def graphs(request):
    return render(request, 'client/graphs.html', {'btc_price': get_btc_price(),
                                                  'eth_price': get_eth_price(),
                                                  'ltc_price': get_ltc_price(),
                                                  'price_graph': crypto_graph(cryptos)})


def home_view(request):
    populate()

    gpu_list = GPUModel.objects.all()
    return render(request, 'client/home.html', {'gpu_list': gpu_list,
                                                'btc_price': get_btc_price(),
                                                'eth_price': get_eth_price(),
                                                'ltc_price': get_ltc_price(),
                                                'user': request.user})


def gpu_card(request, pk):
    card = get_object_or_404(GPUModel, pk=pk)
    hist_prices = card.get_hist_prices_tuple()
    hist_prices_df = pd.DataFrame(hist_prices)
    hist_prices_df.columns = ['price', 'date']
    hist_prices_graph = reg_graph(hist_prices_df)
    try:
        notification = Notification.objects.get_or_create(gpu=card, user=request.user)
    except TypeError:
        notification = 1
    return render(request, 'client/card.html', {'gpu': card,
                                                'btc_price': get_btc_price(),
                                                'eth_price': get_eth_price(),
                                                'ltc_price': get_ltc_price(),
                                                'hist_prices_graph': hist_prices_graph,
                                                'notification': notification})


# references-
# https://www.geeksforgeeks.org/django-modelform-create-form-from-models/
# https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html
def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/gpu')
    else:
        form = UserForm()
    return render(request, 'registration/signup.html', {'form': form})


'''
Helper functions
'''


# API: https://min-api.cryptocompare.com/documentation?key=Price&cat=multipleSymbolsFullPriceEndpoint
def get_btc_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD').json()['USD']


def get_eth_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD').json()['USD']


def get_ltc_price():
    return requests.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD').json()['USD']


# Reference:
# https://plotly.com/python/line-charts/
def crypto_graph(ticker_list):
    data_frame_list = list()
    for ticker in ticker_list:
        data_frame = yf.download(tickers=ticker, group_by=ticker, period='1wk', interval='60m')
        data_frame['Ticker'] = ticker
        data_frame_list.append(data_frame)
    dfl = pd.concat(data_frame_list)
    print(dfl)
    fig = px.line(dfl,
                  x=dfl.index,
                  y=((dfl['High'] + dfl['Low']) / 2),
                  color='Ticker',
                  title='Cryptocurrency Prices Over Last Week',
                  labels={
                      "Datetime": "Date",
                      "y": "Price USD"
                  }
                  )
    return plot(fig, output_type='div')


def reg_graph(*args):
    print(args[0])
    fig = px.line(args[0],
                  x='date',
                  y='price',
                  # title='Price of Product Over Time',
                  # labels={
                  #     "Datetime": "Date",
                  #     "y": "Price USD"
                  # }
                  )
    return plot(fig, output_type='div')
