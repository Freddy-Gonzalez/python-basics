monto = float(input("Ingrese el monto en moneda local "))

USD_RATE = 0.050
EUR_RATE = 0.047
GBP_RATE = 0.039
JPY_RATE = 7.71

usd = monto * USD_RATE
eur = monto * EUR_RATE
gbp = monto * GBP_RATE
jpy = monto * JPY_RATE

print(f"""
      Valor en moneda local {monto:.2f}
      Valor en USD {usd:.2f}
      Valor en EUR {eur:.2f}
      Valor en GBP {gbp:.2f}
      Valor en JPY {jpy:.2f}
      """)
