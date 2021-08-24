skymriq_price = float(input())
caca_price = float(input())
palamyd_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())
midi_price = 7.50

palamyd = palamyd_kg * (skymriq_price + (skymriq_price * 0.6))
safrid = safrid_kg * (caca_price + (caca_price * 0.8))
midi = midi_kg * midi_price
total = palamyd + safrid + midi

print(f"{total:.2f}")
