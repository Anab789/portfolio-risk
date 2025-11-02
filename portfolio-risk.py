import math

rA = float(input("Expected return of Asset A (%): ")) / 100
rB = float(input("Expected return of Asset B (%): ")) / 100
sdA = float(input("Standard deviation of Asset A (%): ")) / 100
sdB = float(input("Standard deviation of Asset B (%): ")) / 100
rho = float(input("Correlation coefficient between A and B: "))
wA = float(input("Weight of Asset A (0–1): "))
wB = 1 - wA

E_port = wA*rA + wB*rB
var_port = (wA*sdA)**2 + (wB*sdB)**2 + 2*wA*wB*sdA*sdB*rho
sd_port = math.sqrt(var_port)
print(sd_port)
