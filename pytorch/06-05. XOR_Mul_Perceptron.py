import torch
import torch.nn as nn

device = 'cuda' if torch.cuda.is_available() else 'cpu'

torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

X = torch.FloatTensor([[0, 0], [0, 1], [1, 0], [1, 1]]).to(device)
Y = torch.FloatTensor([[0], [1], [1], [0]]).to(device)

# 다층 퍼셉트론 설계 입력층, 은닉층1, 은닉층2, 은닉층3, 출력층
model = nn.Sequential(
    nn.Linear(2,10, bias=True), # inpyt layer = 2, hidden layer1 = 10
    nn.Sigmoid(),
    nn.Linear(10,10,bias=True), # hidden1 = 10, hidden2 = 10
    nn.Sigmoid(),
    nn.Linear(10,10,bias=True), #hidden2 = 10, hidden3 = 10
    nn.Sigmoid(),
    nn.Linear(10,1,bias=True), # hidden3 = 10, output = 1
    nn.Sigmoid()
    ).to(device)

# 비용 함수와 옵티마이저 선언
# nn.BCELoss() -> 이진 분류에 사용하는 크로스엔트로피 함수
criterion = torch.nn.BCELoss().to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=1) 

for epoch in range(10001):
    optimizer.zero_grad()
    # forward 연산
    hypothesis = model(X)

    # 비용 함수
    cost = criterion(hypothesis, Y)
    cost.backward()
    optimizer.step()

    # 100의 배수에 해당되는 에포크마다 비용을 출력
    if epoch % 100 == 0:
        print(epoch, cost.item())

with torch.no_grad():
    hypothesis = model(X)
    predicted = (hypothesis > 0.5).float()
    accuracy = (predicted == Y).float().mean()
    print('모델의 출력값(Hypothesis): ', hypothesis.detach().cpu().numpy())
    print('모델의 예측값(Predicted): ', predicted.detach().cpu().numpy())
    print('실제값(Y): ', Y.cpu().numpy())
    print('정확도(Accuracy): ', accuracy.item())
