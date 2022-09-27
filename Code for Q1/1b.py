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


##### He calculation and plot
B = B_He
A = A_He
# Interatomic distance, in nm
r = np.linspace(0.2, 1, 1000)
# Interatomic potential
U = B/r**12 - A/r**6
# Interatomic force
F = -12*B/r**13 + 6*A/r**7

line1 = plt.plot(r, U, 'k', lw=2, label=r'U(r)_He')
plt.xlabel("r (nm)")
plt.ylabel("U (K)")
plt.xlim(0.2, 0.8)
plt.ylim(-50, 50)

plt.twinx()
line2 = plt.plot(r, F, 'k', ls=':', lw=2, label=r'F(r)_He')
plt.xlim(0.2, 0.8)
plt.ylim(-200, 200)

lines = line1 + line2
labels = []
for line in lines:
    labels.append(line.get_label())
plt.legend(lines, labels)
plt.ylabel("F (K/nm)")
plt.savefig('He.png')
plt.show()


##### Ne calculation and plot
B = B_Ne
A = A_Ne
# Interatomic distance, in nm
r = np.linspace(0.2, 1, 1000)
# Interatomic potential
U = B/r**12 - A/r**6
# Interatomic force
F = -12*B/r**13 + 6*A/r**7

line1 = plt.plot(r, U, 'k', lw=2, label=r'U(r)_Ne')
plt.xlabel("r (nm)")
plt.ylabel("U (K)")
plt.xlim(0.2, 0.8)
plt.ylim(-100, 100)

plt.twinx()
line2 = plt.plot(r, F, 'k', ls=':', lw=2, label=r'F(r)_Ne')
plt.xlim(0.2, 0.8)
plt.ylim(-1000, 1000)

lines = line1 + line2
labels = []
for line in lines:
    labels.append(line.get_label())
plt.legend(lines, labels)
plt.ylabel("F (K/nm)")
plt.savefig('Ne.png')
plt.show()


##### Kr calculation and plot
B = B_Kr
A = A_Kr
# Interatomic distance, in nm
r = np.linspace(0.3, 1, 1000)
# Interatomic potential
U = B/r**12 - A/r**6
# Interatomic force
F = -12*B/r**13 + 6*A/r**7

line1 = plt.plot(r, U, 'k', lw=2, label=r'U(r)_Kr')
plt.xlabel("r (nm)")
plt.ylabel("U (K)")
plt.xlim(0.3, 0.8)
plt.ylim(-250, 200)

plt.twinx()
line2 = plt.plot(r, F, 'k', ls=':', lw=2, label=r'F(r)_Kr')
plt.xlim(0.3, 0.8)
plt.ylim(-1500, 1500)

lines = line1 + line2
labels = []
for line in lines:
    labels.append(line.get_label())
plt.legend(lines, labels)
plt.ylabel("F (K/nm)")
plt.savefig('Kr.png')
plt.show()
