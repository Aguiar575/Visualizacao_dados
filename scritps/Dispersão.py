from numpy.random import randn
from matplotlib import pyplot

data1 = 20 * randn(1000) + 100
data2 = data1 + (70 * randn(1000) + 40)

# plot
pyplot.scatter(data1, data2)
pyplot.title('Gráfico de Dispersão entre data1 e data2')
pyplot.show()