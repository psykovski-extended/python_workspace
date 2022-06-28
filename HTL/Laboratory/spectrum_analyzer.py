import glob
import os
path = "c://Users//domin//OneDrive - HTBLuVA St. Pölten//Labor//5AHET//08_Spektrum_Analyzer//data//"
os.chdir(path)
files = glob.glob("*.txt")

for file in files:
    res = []
    with open(path + file, "r") as cf:
        for line in cf.readlines():
            res.append(line.replace("\t\t\t", "\t").replace("\t\t", "\t").replace("\t", ";").replace(",", ".").replace(
                ";", ","))
    with open(path + file.replace(".txt", ".csv"), "w") as cf:
        for line in res:
            cf.write(line)
