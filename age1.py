import sympy as smp
from scipy.integrate import quad

def f(x, om_m, om_r):
    om_l = 1 - om_m - om_r
    return 1 / ((om_m / x) + (om_r / x ** 2) + (om_l * x ** 2)) ** (smp.Rational(1, 2))

integral = quad(f, 0, 1, args=(0.303, 8.8443*10**-5))
age = float(integral[0]) / float(2.2197 * 10 ** -18)
print("age of the universe in seconds", age)
years = float(age) / 31536000
print("age of the universe in years", years)