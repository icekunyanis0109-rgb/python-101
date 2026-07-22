print('MPH\tKPH')
print('-----------------')

for MPH in range(60, 131,10):
    KPH = MPH / 0.6214
    print(MPH, '\t', f"{KPH:.1f}")