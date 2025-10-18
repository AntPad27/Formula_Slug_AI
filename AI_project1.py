import torch


def part1():
    print("Part 1: What is a tensor? Vectors and matrices")
    scalar = torch.tensor(7)
    print(scalar)

    vector = torch.tensor([1, 2, 3])
    print("Vector: ",vector)

    matrix = torch.tensor([[1, 2],
                           [3, 4]
                           ])
    print("Matrix: ",matrix)

    TENSOR = torch.tensor([[[1, 2, 3],
                        [3, 6, 9],
                        [2, 4, 5]]])
    print("Tensor: ",TENSOR)

def part2():
    print("Part 2: Addition, subtraction, multiplication")

    a = torch.tensor([10, 20, 30])
    b = torch.tensor([1, 2, 3])
    print("A: ",a)
    print("B: ",b)
    add=a+b
    print("Addition: ",add)
    sub=a-b
    print("Subtration: ",sub)
    mul=a*b
    print("Multiplication: ",mul)
    div=a/b
    print("Division: ",div)
    print()

def part3():
    print("Part 3: Squeezing, unsqueezing, and transforming")

    x = torch.arange(1., 8.)
    x, x.shape
    x_reshaped = x.reshape(1, 7)
    x_reshaped, x_reshaped.shape

    x_squeezed = x_reshaped.squeeze()
    print(f"\nNew tensor: {x_squeezed}")
    print(f"New shape: {x_squeezed.shape}")

    print(f"Previous tensor: {x_squeezed}")
    print(f"Previous shape: {x_squeezed.shape}")

    x_unsqueezed = x_squeezed.unsqueeze(dim=0)
    print(f"\nNew tensor: {x_unsqueezed}")
    print(f"New shape: {x_unsqueezed.shape}")


if __name__ == "__main__":
    print("PyTorch version:", torch.__version__)
    part1()
    part2()
    part3()