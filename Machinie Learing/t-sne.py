import numpy as np
import keras.datasets.cifar10
from sklearn.manifold import TSNE
from sklearn.datasets import load_digits, load_iris
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

# 데이터 불러오기
mnist = load_digits()  # MNIST 데이터
iris = load_iris() # IRIS 데이터
(x_train, y_train), (x_test, y_test) = keras.datasets.cifar10.load_data() # CIFAR10 데이터

# MNIST t-sne
x_mnist = mnist.data
y_mnist = mnist.target

# iris t-SNE
x_iris = iris.data
y_iris = iris.target

# CIFAR-10 t-SNE
x_cifar = x_train.reshape(x_train.shape[0], -1)[:1000]  #1000개에 대해서만
y_cifar = y_train.ravel()[:1000]

mnist_proj = TSNE(random_state=0, n_iter=10000).fit_transform(x_mnist)
iris_proj = TSNE(random_state=0, n_iter=10000).fit_transform(x_iris)
cifar_proj = TSNE(random_state=0, n_iter=10000).fit_transform(x_cifar)

# 시각화
plt.figure(figsize=(24, 8))

# mnist
plt.subplot(131)
plt.scatter(mnist_proj[:, 0], mnist_proj[:, 1], c=y_mnist, cmap='tab10')
plt.title('t-SNE of MNIST Dataset')

# iris
plt.subplot(132)
plt.scatter(iris_proj[:, 0], iris_proj[:, 1], c=y_iris, cmap='tab10')
plt.title('t-SNE of Iris Dataset')

# cifar10
plt.subplot(133)
plt.scatter(cifar_proj[:, 0], cifar_proj[:, 1], c=y_cifar, cmap='tab10')
plt.title('t-SNE of CIFAR-10 Dataset')

plt.show()
