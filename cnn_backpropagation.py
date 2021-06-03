import numpy as np

X = np.array([0.1,1.2], dtype=float)
X1 = X[0]
X2 = X[1]
print("X1 : ",X1)
print("X2 : ",X2)

Y = np.array([1.4], dtype=float)

b1=b2=1

Error = 0.01
n= 0.001

W = np.array(([0.05,0.1],[-0.8,-0.4]))
W1 = W[0][0]
W2 = W[0][1]
W3 = W[1][0]
W4 = W[1][1]
print("W1 : ",W1)
print("W2 : ",W2)
print("W3 : ",W3)
print("W4 : ",W4)

V = np.array(([0.2],[-0.5]))
V1 = V[0]
V2 = V[1]
print("V1 : ",V1)
print("V2 : ",V2)

def tansig(value):
    tansig = ((np.exp(value)-np.exp(-value))/(np.exp(value)+np.exp(-value)))
    return tansig

def derTansig(value):
    tansig = 1 - ((np.exp(value) - np.exp(-value)) / (np.exp(value) + np.exp(-value))) ** 2
    return tansig

def backPro1(name,Ovalue,h3,yhat,v):
    derZ3 = 2 * (Y - yhat)

    dero3 = derTansig(h3)

    #print(o)
    derV = Ovalue

    deltaV = derZ3 * dero3 * derV

    print("Delta",deltaV)
    result = v - deltaV * n

    print("Updated",name,result)
    return result


def backPro2(w,x,h,v,h3,y,o3):

    first = x

    second = derTansig(h)

    third = v

    forth = derTansig(h3)

    fifth = 2*(y-o3)

    result = first*second*third*forth*fifth
    print("Delta", result)

    final = w- result * n

    return final

z2 = np.dot(X, W) +b1
h1 = z2[0]
h2 = z2[1]
print("h1 : ",h1)
print("h2 : ",h2)

OValues = tansig(z2)
O1 = OValues[0]
O2 = OValues[1]
print("O1 : ",O1)
print("O2 : ",O2)

h3 = np.dot(OValues, V) +b2
yhat = tansig(h3)
print("h3 : ",h3)
print("YHat : ",yhat)

error = (Y-yhat)*(Y-yhat)
print("Error : ",error)

if error > Error:

    """
    Calculate V1 aNd V2
    """

    #Calculates UPDATED V1

    DeltaV1 = backPro1("V1",O1, h3, yhat, V1)

    DeltaV2 = backPro1("V2", O2, h3, yhat, V2)



    """
       Calculate W1 W2 W3 W4
       """

    # Calculates UPDATED W1


    updatedW1 = backPro2(W1, X1, h1, V1, h3, Y, yhat)
    print("Updated W1",updatedW1)

    updatedW3 = backPro2(W3, X2, h1, V1, h3, Y, yhat)
    print("Updated W3", updatedW3)

    updatedW2 = backPro2(W2, X1, h2, V2, h3, Y, yhat)
    print("Updated W2", updatedW2)

    updatedW4 = backPro2(W4, X2, h2, V2, h3, Y, yhat)
    print("Updated W4", updatedW4)
