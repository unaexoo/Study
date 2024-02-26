'''
과적합을 막는 방법
1. 데이터의 양 늘리기
2. 모델의 복잡도 줄이기
- 인공신경망의 복잡도는 은닉층의 수나 매개변수의 수 등으로 결정됨

3. 가중치 규제 적용하기
- L1 규제 : 가중치 w들의 절대값 합계를 비용 함수에 추가
- L2 규제 : 모든 가중치 w들의 제곱합을 비용 함수에 추가

4. 드롭아웃
- 학습 과정에서 신경망의 일부를 사용하지 않는 방법
'''
import torch
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml

# 2. 모델의 복잡도 줄이기
class Architecture1(nn.module) :
    def __init__(self, input_size,hidden_size, num_classes):
        super(Architecture1, self).__init__()
        self.fc1 = nn.Linear(input_size,hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size,hidden_size)
        self.relu = nn.ReLU()
        self.fc3 = nn.Linear(hidden_size,num_classes)

    def forward(self,x):
        out = self.fc1(x)
        out = self.relu(out)
        out = self.fc2(out)
        out = self.relu(out)
        out = self.fc3(out)
        return out
    
# 위의 코드가 과적합을 보인다면
class Architecture1(nn.Module):
  def __init__(self, input_size, hidden_size, num_classes):
    super(Architecture1, self).__init__()
    self.fc1 = nn.Linear(input_size, hidden_size)
    self.relu = nn.ReLU()
    self.fc2 = nn.Linear(hidden_size, num_classes)

  def forward(self, x):
    out = self.fc1(x)
    out = self.relu(out)
    out = self.fc2(out)
    return out


# 3. 가중치 규제
model = Architecture1(10, 20, 2)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-4, weight_decay=1e-5)
