str1 = "abcdefghijklmnopqrstuvwxyz"

print(str1[2::3])
#cfilorux

print(str1[20:4:-1])
#utsrqponmlkjihgf

print(str1[:5]+str1[20:4:-1]+str1[21:])
#abcdeutsrqponmlkjihgfvwxyz

a=len(str1)//2
print(str1[a::2])
#nprtvxz

print(str1[20:4:-1])
#utsrqponmlkjihgf

print()


str3='datastructuresandalgorithms'

print(str3[0:4:]+str3[16:3:-1]+str3[17::])
#datadnaserutcurtsalgorithms

print(str3[5:-9:1])
#tructuresanda

print(str3[::-4])
#silaurt

print(str3[0:3:1]+str3[-4:2:-1]+str3[24::])
#dattirogladnaserutcurtsahms

print()
#

print()


str4='artificialintelligence'

print(str4[:10:]+str4[:9:-1])
#artificialecnegilletni

print()
#

print(str4[3::])
#ificialintelligence

print(str4[9::-1]+str4[10::])
#laicifitraintelligence

print(str4[::-2])
#englenliiir

print()


str5='machinelearningmodels'

print(str5[-7:-15:-1])
#gninrael

print(str5[:-15:-1])
#sledomgninrael

print(str5[-15:-4:])
#elearningmo

print()
#

print(str5[15::]+str5[7:15:]+str5[:7:])
#modelslearningmachine

print()


str6='computernetworksandsecurity'

print(str6[:8:]+str6[15:7:-1]+str6[16::])
#computerskrowtenandsecurity

print(str6[19::])
#security

print(str6[:4:]+str6[:3:-1])
#compytirucesdnaskrowtenretu

print()
#

print()
#

print()


str7='objectorientedprogramming'

print(str7[13:5:-1])
#detneiro

print(str7[-5:-21:-1])
#margorpdetneirot

print(str7[:5:]+str7[19:4:-1]+str7[20::])
#objecargorpdetneirotmming

print(str7[:9:-1])
#gnimmargorpdetn

print(str7[::3])
#oeoeerrmg

print()


str8='datascienceandanalytics'

a=len(str8)//2
print(str8[:a:]+str8[:a-1:-1])
#datasciencescitylanadna

print(str8[3:20:2])
#acecadnlt

print(str8[-20::-1]+str8[-19:-9:]+str8[:-10:-1])
#atadscienceandscitylana

print(str8[:a:])
#datascience

print(str8[10::-1]+str8[11:14:]+str8[:-10:-1])
#ecneicsatadandscitylana

print()