print()
print("   Amino acid sequence maker            Made by Yong Jun Jeon  ")
print()
print(" +---------------------+--- Codon Table -----------------------+")
print(" |  Leucine       (L)  |   UUA   UUG   CUU   CUC   CUA   CUG   |")
print(" |  Arginine      (R)  |   AGA   AGG   CGU   CGC   CGA   CGG   |")
print(" |  Serine        (S)  |   AGU   AGC   UCU   UCC   UCA   UCG   |")
print(" |  Proline       (P)  |   CCU   CCC   CCA   CCG               |")
print(" |  Threonine     (T)  |   ACU   ACC   ACA   ACG               |")
print(" |  Valine        (V)  |   GUU   GUC   GUA   GUG               |")
print(" |  Alanine       (A)  |   GCU   GCC   GCA   GCG               |")
print(" |  Glycine       (G)  |   GGU   GGC   GGA   GGG               |")
print(" |  Isoleucine    (I)  |   AUU   AUC   AUA                     |")
print(" |  Phenylalanine (F)  |   UUU   UUC                           |")
print(" |  Tyrosine      (Y)  |   UAU   UAC                           |")
print(" |  Cysteine      (C)  |   UGU   UGC                           |")
print(" |  Histidine     (H)  |   CAU   CAC                           |")
print(" |  Glutamine     (Q)  |   CAA   CAG                           |")
print(" |  Asparagine    (N)  |   AAU   AAC                           |")
print(" |  Lysine        (K)  |   AAA   AAG                           |")
print(" |  Aspartic acid (D)  |   GAU   GAC                           |")
print(" |  Glutamic acid (E)  |   GAA   GAG                           |")
print(" |  Tryptophan    (W)  |   UGG                                 |")
print(" |  Methionine    (M)  |   AUG   (START codon)                 |")
print(" |  STOP codon         |   UAA    UAG   UGA                    |")
print(" +---------------------+---------------------------------------+")


#DNA single strand input (codon)
print('[ DNA template strand sequence ]')
a = input()
A = a.upper()

#mRNA sequence
print()
print("[ mRNA sequence ]")
mRNA = str.maketrans('ATCG', 'TAGC')
b = A.translate(mRNA)
print(b)
#5'capping
#poly A tailing
#slicing (eliminate intron - 무의미한 반복서열 제거)
#intron과 exon의 차이점을 이용해 slicing

#3개 단위로 쪼개기 to list
length = 3
listb = [b[i:i+length] for i in range(0, len(a), length)]
#print()
#print(listb)

#시작~종결서열 slice
print()
start_list=list(filter(lambda e:listb[e] == 'AUG', range(len(listb))))
print('start = ', start_list)
stop_list1=list(filter(lambda e:listb[e] == 'UAA', range(len(listb))))
stop_list2=list(filter(lambda e:listb[e] == 'UAG', range(len(listb))))
stop_list3=list(filter(lambda e:listb[e] == 'UGA', range(len(listb))))
stop_list = stop_list1 + stop_list2 + stop_list3
stop_list.sort()
print('stop = ', stop_list)

print("[ 1st Sequence ]")
k1 = listb[start_list[0]:stop_list[0]]
#k = listb[listb.index('AUG'):listb.index('UAA')]
print(k1)
print()

print("[ 2nd Sequence ]")
k2 = listb[start_list[1]:stop_list[1]]
print(k2)
print()

print("[ 3rd Sequence ]")
k3 = listb[start_list[2]:stop_list[2]]
print(k3)
print()

#list to string
#print()
#print(', '.join(f'{x}' for x in lista))

from io import StringIO

def return_print(*message):
    io = StringIO()
    print(*message, file=io, end="")
    return io.getvalue()

result1 = return_print(' '.join(f'{x}' for x in k1))
print()
#print(result1)


#{Codon : Amino acid} Dictionary 
varL = {'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L'}
varR = {'AGA': 'R', 'AGG': 'R', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R'}
varS = {'AGU': 'S', 'AGC': 'S', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S'}
varP = {'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P'}
varT = {'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T'}
varV = {'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V'}
varA = {'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A'}
varG = {'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
varI = {'AUU': 'I', 'AUC': 'I', 'AUA': 'I'}
varX = {'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'}
varF = {'UUU': 'F', 'UUC': 'F'}
varY = {'UAU': 'Y', 'UAC': 'Y'}
varC = {'UGU': 'C', 'UGC': 'C'}
varH = {'CAU': 'H', 'CAC': 'H'}
varQ = {'CAA': 'Q', 'CAG': 'Q'}
varN = {'AAU': 'N', 'AAC': 'N'}
varK = {'AAA': 'K', 'AAG': 'K'}
varD = {'GAU': 'D', 'GAC': 'D'}
varE = {'GAA': 'E', 'GAG': 'E'}
varW = {'UGG': 'W'}
varM = {'AUG': 'M'}

#if s in tuple[0]:
#    return tuple[1]


varW.update(varM);varE.update(varW);varD.update(varE);varK.update(varD)
varN.update(varK);varQ.update(varN);varH.update(varQ);varC.update(varH)
varY.update(varC);varF.update(varY);varX.update(varF);varI.update(varX)
varG.update(varI);varA.update(varG);varV.update(varA);varT.update(varV)
varP.update(varT);varS.update(varP);varR.update(varS);varL.update(varR)

#amino acid sequence output
print()
print("<amino acid sequence output>")
for Key,value in varL.items():
    result1 = result1.replace(Key, value)
print(result1)
