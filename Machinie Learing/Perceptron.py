import numpy as np
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

def perceptron(x, y, digit, epochs=10, lr=0.1):
    # 숫자를 긍정 클래스로 설정, 나머지는 부정 클래스
    y_digit = np.where(y == digit, 1, -1)

    # 가중치 초기화 (특성 수 + 1 , 편향)
    W = np.zeros(x.shape[1] + 1)

    # 입력 데이터에 편향 추가
    x = np.insert(x, 0, 1, axis=1)

    for epoch in range(epochs):
        # 데이터를 위한 랜덤 인덱스 섞기
        indices = np.arange(x.shape[0])
        np.random.shuffle(indices)
        
        # 데이터셋을 순회하며 가중치 업데이트
        for idx in indices:
            xi = x[idx]
            yi = y_digit[idx]
            
            # 틀린 샘플에 대한 가중치 업데이트
            if yi * (np.dot(W, xi)) <= 0:
                W += lr * yi * xi

    return W

# MNIST 데이터 로드 및 전처리
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train = x_train.reshape(-1, 28*28) / 255.0  # 데이터 전처리

# 각 숫자에 대한 퍼셉트론 훈련
weight = []
for i in range(10):
    W = perceptron(x_train, y_train, i)
    weight.append(W)

# 확인
fig, axes = plt.subplots(2, 10, figsize=(18, 4))
for i in range(10):
     ax1 = axes[0, i]
     ax2 = axes[1, i]
     
     # 가중치(이미지) 시각화
     ax1.imshow(weight[i][1:].reshape(28, 28), cmap='gray')
     ax1.set_title(f"Weight {i}")
     ax1.axis('off')

     # 원본 이미지 비교
     original_image = x_train[y_train == i][0].reshape(28, 28)
     ax2.imshow(original_image, cmap='gray')
     ax2.set_title(f"Digit {i}")
     ax2.axis('off')

plt.tight_layout()
plt.show()
