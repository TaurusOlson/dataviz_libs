# Example 1:
data1 = stats.poisson(2).rvs(100)
data2 = stats.poisson(5).rvs(120)
max_data = np.r_[data1, data2].max()
bins = np.linspace(0, max_data, max_data + 1)
plt.hist(data1, bins, normed=True, color="#6495ED", alpha=.5)
plt.hist(data2, bins, normed=True, color="#F08080", alpha=.5);


# Example 2:
x1 = np.random.normal(10, 1, size=1000)
x2 = np.random.normal(8, 1, size=1000)
max_data = np.r_[x1, x2].max()
bins = np.linspace(0, max_data, max_data + 1)
plt.hist(x1, bins=bins, alpha=0.5, normed=True);
plt.hist(x2, bins=bins, alpha=0.5, normed=True);
