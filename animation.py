import os, time

os.system('cls')

filenames = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt', '8.txt', '9.txt', '10.txt', '11.txt', '12.txt', '13.txt', '14.txt', '15.txt', '16.txt', '17.txt', '18.txt', '19.txt', '20.txt', '21.txt', '22.txt', '23.txt', '24.txt', '25.txt', '26.txt', '27.txt', '28.txt', '29.txt', '30.txt', '31.txt', '32.txt', '33.txt', '34.txt', '35.txt', '36.txt', '37.txt', '38.txt', '39.txt', '40.txt', '41.txt', '42.txt', '43.txt', '44.txt', '45.txt', '46.txt', '47.txt', '48.txt', '49.txt', '50.txt', '51.txt', '52.txt', '53.txt', '54.txt', '55.txt', '56.txt', '57.txt', '58.txt', '59.txt', '60.txt', '61.txt', '62.txt', '63.txt', '64.txt', '65.txt', '66.txt', '67.txt', '68.txt', '69.txt']
frames=[]

for name in filenames:
	with open(name, "r", encoding="utf8") as f:
			frames.append(f.readlines())

for frame in frames:
	print("".join(frame))
	time.sleep(1.50)
	os.system("cls")

