p = float(input('Digite o preço do produto: R$ '))
t = p - (p * 5 / 100)
print(f'O valor do produto que custava R${p:.2f} com 5% de desconto fica R${t:.2f}')