def miles2km(miles):
    kms = 1.6*miles
    return kms

print((miles2km(10)))

k = lambda miles: 1.6*miles
print('kms',k(10))