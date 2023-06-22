#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 16:51:50 2021

@author: RafaĹ Biedrzycki
Kodu tego mogÄ uĹźywaÄ moi studenci na Äwiczeniach z przedmiotu WstÄp do Sztucznej Inteligencji.
Kod ten powstaĹ aby przyspieszyÄ i uĹatwiÄ pracÄ studentĂłw, aby mogli skupiÄ siÄ na algorytmach sztucznej inteligencji.
Kod nie jest wzorem dobrej jakoĹci programowania w Pythonie, nie jest rĂłwnieĹź wzorem programowania obiektowego, moĹźe zawieraÄ bĹÄdy.

Nie ma obowiÄzku uĹźywania tego kodu.
"""
import statistics
import time
import numpy as np
import matplotlib.pyplot as plt

# ToDo tu prosze podac pierwsze cyfry numerow indeksow
p = [4, 1]

L_BOUND = -5
U_BOUND = 5

def q(x):
    return np.sin(x * np.sqrt(p[0] + 1)) + np.cos(x * np.sqrt(p[1] + 1))


x = np.linspace(L_BOUND, U_BOUND, 100)
y = q(x)

np.random.seed(1)


# f logistyczna jako przykĹad sigmoidalej
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
    # alternatywnie tanh
    #return np.tanh(x)


# pochodna fun. 'sigmoid'
def d_sigmoid(x):
    s = 1 / (1 + np.exp(-x))
    return s * (1 - s)
    #alternatywnie tanh
    # tanh_x = np.tanh(x)
    # return 1 - tanh_x ** 2


# f. straty
def nloss(y_out, y):
    return (y_out - y) ** 2


# pochodna f. straty
def d_nloss(y_out, y):
    return 2 * (y_out - y)


class DlNet:
    def __init__(self, x, y, neuron_number, learning_rate):
        self.x = x
        self.y = y
        self.y_out = 0

        self.HIDDEN_L_SIZE = neuron_number
        self.LR = learning_rate

        np.random.seed(int(time.time()))
        self.first_weights = np.random.randn(self.HIDDEN_L_SIZE, 1)
        self.first_biases = np.zeros([self.HIDDEN_L_SIZE, 1])

        #self.second_weights = np.zeros([1, self.HIDDEN_L_SIZE])
        #self.second_bias = np.zeros([1, 1])
        #alternatywne, losowe generowanie wag w drugiej warstwie (lepsze rezultaty)
        self.second_weights = np.random.randn(1, self.HIDDEN_L_SIZE)
        self.second_bias = np.zeros([1, 1])

    def forward(self, x, y):
        yh, values = self.predict(x)
        loss = nloss(yh, y)
        return yh, loss, values

    def predict(self, x):
        first_layer = np.dot(self.first_weights, x)
        first_layer += self.first_biases
        first_z = sigmoid(first_layer)
        second_layer = np.dot(self.second_weights, first_z)
        second_layer += self.second_bias
        yh = sum(second_layer)
        return yh, {"y1": first_layer, "y2": second_layer, "z1":first_z} # słownik potrzebny do propagacji wstecznej

    def backward(self, x, y, y_result, comp_info):
        # Uczenie sieci metodą SGD
        d_loss_y_result = d_nloss(y_result, y)
        d_loss_second = d_loss_y_result * np.sum(self.second_weights)

        self.second_bias = self.second_bias - self.LR * (1/x.shape[1]) * np.dot(d_loss_y_result, np.ones([d_loss_y_result.shape[1], 1]))
        self.second_weights = self.second_weights - self.LR * (1/x.shape[1]) * np.dot(d_loss_y_result, comp_info["z1"].T)

        d_loss_z1 = np.dot(self.second_weights.T, d_loss_second)
        d_loss_first = d_loss_z1 * d_sigmoid(comp_info["y1"])
        self.first_biases = self.first_biases - self.LR * (1/x.shape[1]) * np.dot(d_loss_first, np.ones([d_loss_first.shape[1], 1]))
        self.first_weights = self.first_weights - self.LR * (1/x.shape[1]) * np.dot(d_loss_first, x.T)

    def train(self, x_set, y_set, iters):
        for i in range(iters):
            yh, loss, comp_info = self.forward(x_set, y_set)
            self.backward(x_set, y_set, yh, comp_info)
        return yh, loss

def show_results(x, y, yh):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    plt.plot(x, y, 'r')
    plt.plot(x, yh, 'b')

    plt.show()

if __name__ == "__main__":
    plt.show()
    # parameters
    function_samples = 100 # Wielkość zbioru uczącego
    neuron_number = 9 # liczba neuronów
    learning_rate = 0.15 # współczynnik nauczania(beta)
    iterations = 50000 # liczba iteracji
    #
    loss_list=[]
    for i in range(20):
        x = np.linspace(L_BOUND, U_BOUND, num=function_samples).reshape(1, function_samples)
        y = np.array(q(x)).reshape(1, function_samples)

        nn = DlNet(x, y, neuron_number, learning_rate)
        yh, loss = nn.train(x, y, iterations)
        print(f'Średnia strata: {np.average(loss)}')
        loss_list.append(np.average(loss))
        # funkcja narysowana na czerwono, to funkcja rzeczywista, a na niebiesko, wynik działania algorytmu
        show_results(x.reshape(function_samples), y.reshape(function_samples), yh)

    mean=statistics.mean(loss_list)
    print("Średnia z 20-tu doświadczeń: " + str(mean))