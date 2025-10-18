import torch
from torch import nn

#Data
weight, bias = 1.1, 2.2
X = torch.arange(0, 1, 0.02).unsqueeze(1)   # (N, 1)
y = weight * X + bias                       # (N, 1)

# Train/test split (80/20)
n_train = int(0.8 * len(X))
X_train, y_train = X[:n_train], y[:n_train]
X_test,  y_test  = X[n_train:], y[n_train:]

#Model
class LinearRegressionModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(1, 1)  # y = w*x + b
    def forward(self, x):
        return self.linear(x)

torch.manual_seed(42)
model = LinearRegressionModel()

loss_fn = nn.L1Loss()                       # MAE
opt = torch.optim.SGD(model.parameters(), lr=0.01)


for _ in range(300):
    model.train()
    pred = model(X_train)
    loss = loss_fn(pred, y_train)
    opt.zero_grad()
    loss.backward()
    opt.step()


w = model.linear.weight.item()
b = model.linear.bias.item()
print("Learned params:", {"weight": round(w,4), "bias": round(b,4)})

model.eval()
with torch.inference_mode():
    y_pred = model(X_test)

print("\nFirst 5 rows [X, y_true, y_pred]:")
print(torch.hstack([X_test[:5], y_test[:5], y_pred[:5]]))