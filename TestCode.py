from scipy.stats import binom

# 给定的参数
L = 1e6  # 1 Mbps
r = 64e3  # 64 Kbps
p = 0.1

from scipy.stats import binom

# 给定的参数
L = 1e6  # 1 Mbps
r = 64e3  # 64 Kbps
p = 0.1


# 计算P(X <= MC) 的值，然后用1减去得到P(X > MC)
P_2MC = 1 - sum(binom.pmf(k, 30, p) for k in range(16))
P_4MC = 1 - sum(binom.pmf(k, 60, p) for k in range(31))

print(f"P(X > MC) for 2MC users: {P_2MC}")
print(f"P(X > MC) for 4MC users: {P_4MC}")


