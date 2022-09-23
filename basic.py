from inspect import Parameter
import numpy as np

def forward_prop(X, paramaters):
    pass
def loss(a3, Y):
    pass

def model(X, Y, learning_rate, epochs):
    grads = {}
    costs = []
    paramaters = np.zeros(X.shape)
    for i in range(epochs):
        a3 = forward_prop(X, paramaters)
        cost = loss(a3, Y)
        grads = back_prop(X, Y)
        paramaters = update_params(paramaters, grads, learning_rate)