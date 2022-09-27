import matplotlib
import numpy as np
from matplotlib import pyplot as plt


# He
eps_He = 11.00963377
sig_He = 0.2639781646
B_He = 4 * eps_He * sig_He**12
A_He = 4 * eps_He * sig_He**6

# Ne
eps_Ne = 42.36165080
sig_Ne = 0.2759124561
B_Ne = 4 * eps_Ne * sig_Ne**12
A_Ne = 4 * eps_Ne * sig_Ne**6

# Kr
eps_Kr = 201.0821392
sig_Kr = 0.357999364
B_Kr = 4 * eps_Kr * sig_Kr**12
A_Kr = 4 * eps_Kr * sig_Kr**6

# Interatomic distance, in nm
r = np.linspace(0.2, 1, 1000)
# Interatomic potential
U_He = B_He/r**12 - A_He/r**6
U_Ne = B_Ne/r**12 - A_Ne/r**6
U_Kr = B_Kr/r**12 - A_Kr/r**6
# Interatomic force
# F = -12*B/r**13 + 6*A/r**7

plt.figure()
plt.plot(r, U_He, 'k', lw=2, label='He')
plt.plot(r, U_Ne, 'b', lw=2, label='Ne')
plt.plot(r, U_Kr, 'r', lw=2, label='Kr')
plt.xlim(0.2, 0.8)
plt.ylim(-220, 200)
plt.legend()
plt.xlabel('r (nm)')
plt.ylabel('U (K)')
plt.savefig('compareU.png')
plt.show()
