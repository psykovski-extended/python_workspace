from matlab import engine

eng = engine.start_matlab()
eng.addpath("C:\\Users\\Dominik Lovetinsky\\Documents\MATLAB\\Magnetischer_Kreis")
L = eng.Induction(200, 10, 0.5, 1000, 1)
L = eng.movmean([0, 1, 2, 5, 6, 4, 7, 94, 32, 11, 2])
print(L)

for i in L:
    print(i)

print('end')
