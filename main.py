import os

gDriveid = input("Masukkan id Google Drive = ")

print(gDriveid)
comm = f"cd download && gdown https://drive.google.com/uc?id={gDriveid}"

print(comm)

run_Command = os.system(comm)

print(run_Command)