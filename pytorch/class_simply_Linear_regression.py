import torch
import torch.nn as nn 
import torch.nn.functional as F 
import torch.optim as optim 

torch.manual_seed(1)

# 데이터
x_train = torch.FloatTensor([[1],[2],[3]])
y_train = torch.FloatTensor([[2],[4],[6]])

class LinearRegressionModel(nn.Module) :
    def __init__(self) : 
        super().__init__()
        self.linear = nn.Linear(1,1)
        
    def forward(self,x) : 
        return self.linear(x)
    
model = LinearRegressionModel()

# optimizer
optimizer = torch.optim.SGD(model.parameters(),lr = 0.01)

# 전체 훈련 데이터에 대해 경사하강법을 2,000 회 반복
nb_epochs = 2000
for epoch in range(nb_epochs + 1):
    # H(x) 계산
    prediction = model(x_train)
    
    # cost 계산
    cost = F.mse_loss(prediction, y_train) # 파이토치 평균 제곱 오차 함수
    
    # cost로 H(x) 개선, gradient=0 초기화
    optimizer.zero_grad()
    
    # 비용 함수를 미분하여 gradient 계산
    cost.backward() 
    
    # w와 b를  업데이트
    optimizer.step()
    
    if epoch % 100 == 0:
        # 100번마다 로그 출력
      print('Epoch {:4d}/{} Cost: {:.6f}'.format(
          epoch, nb_epochs, cost.item()
      ))
      