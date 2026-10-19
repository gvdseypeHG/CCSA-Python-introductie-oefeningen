aantalGeplukteAppels = int(input())

gevuldeKisten = aantalGeplukteAppels // 20
overgeblevenAppels = aantalGeplukteAppels % 20

gevuldePalletten = gevuldeKisten // 35
overgeblevenKisten = gevuldeKisten % 35

print(f"{gevuldePalletten}")
print(f"{overgeblevenKisten}")

print(f"{overgeblevenAppels}")

