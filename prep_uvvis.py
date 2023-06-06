import pandas as pd

df = pd.read_csv('data/uv_vis_prep.csv', skiprows=2, header=None)

columns = ['wavelength', 'transmission']

glas = df[[0, 1]]
glas.columns = columns
glas = glas.assign(probe='glas', repetition=1)

zns1 = df[[2, 3]]
zns1.columns = columns
zns1 = zns1.assign(probe='zns', repetition=1)

zns2 = df[[4, 5]]
zns2.columns = columns
zns2 = zns2.assign(probe='zns', repetition=2)

mgf21 = df[[6, 7]]
mgf21.columns = columns
mgf21 = mgf21.assign(probe='mgf2', repetition=1)

mgf22 = df[[8, 9]]
mgf22.columns = columns
mgf22 = mgf22.assign(probe='mgf2', repetition=2)

mgf23 = df[[10, 11]]
mgf23.columns = columns
mgf23 = mgf23.assign(probe='mgf2', repetition=3)

filter1 = df[[12, 13]]
filter1.columns = columns
filter1 = filter1.assign(probe='filter', repetition=1)

df = pd.concat([glas, zns1, zns2, mgf21, mgf22, mgf23, filter1])
df['prope'] = df.probe.astype('category')
df['wavelength'] = df.wavelength.astype(float)
df['transmission'] = df.transmission.astype(float)

df.to_parquet('data/uv_vis.parquet')
