def get_newton_sqrt(value, steps):
    a=value #number to get square root of
    x0=2
    for i in range(steps):
        #x_(n+1)= 0.5*(x_n+a/x_n)

if i !=0 : value =( value + a/value)*0.5
else: value=(x0 + a/x0) * 0.5

 return float(value)


 def test_get_newton_sqrt():

    assert get_newton_sqrt(5,6)
    assert get_newton_sqrt(8,9)
    assert get_newton_sqrt(7,9)


     test_get_newton_sqrt();
