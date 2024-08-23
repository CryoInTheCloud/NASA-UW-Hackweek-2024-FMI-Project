
### designate the range of wavelengths you’re interested in…so this is 950 – 1401 nm by increment of 1
wl = np.array(range(950,1401,1)) 

### convert that to meters because that’s what the model wants
wl = wl*1e-9 

### here’s how you run it a single time
tartes.albedo(wl, SSA=15, g0=0.86, B0=1.6, dir_frac=1,sza=0)

### So in that one dir_frac = 1 means all direct light, no diffuse, and sza=0 means solar zenith angle 0, so ## sun directly overhead. You can change that stuff, and lots of other parameters (see the link in ##email)…whatever you don’t assign, it just goes with the default, so make sure you check what the ##defaults are

### You can also run it for a variety of different SSA values
ssa.array = np.array(range(5,50,10)) 

test = []
for i in range(10):
    albedo = tartes.albedo(wl, SSA=SSAarray, dir_frac=1, sza=0) 
    test.append(albedo) 

### then you can convert it to a dataframe and export it
df = pd.DataFrame(test)
fileout = “some file path”
df.to_csv(fileout)
