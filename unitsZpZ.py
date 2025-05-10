import math

number = 10
# bigNumber:
#  denotes number! We consider the group Z/(bigNumber)Z
bigNumber =  math.factorial(number)
# primeDecompPrimes:
#   primes in the prime decomposition of number (not includinmg 2
#   used to calculate the units of Z/(bigNumber)Z
primeDecompPrimes = [3,5,7]

units = []
# Sieve of units.
# We start by adding only odd numbers to the sieve.
# In this way we avoid removing multiples of 2.
for k in range(math.floor(bigNumber/2)):
    units.append(2*k+1)

# We remove all the elements not co-prime with (bigNumber)
# using the information in primeDecompPrimes.
for prime in primeDecompPrimes:
    i = 1
    while i*prime < bigNumber:
        # We try to remove the number i*prime.
        # If the number was removed before, an exception will be launch.
        # In such a case, we catch the exception and ignore it.
        try:
            units.remove(i*prime)
        except:
            pass
        i += 1

# We write the units of Z/(bigNumber)Z into a file so that
# it does not need to be recalculated.
fileNameUnits ='units_'+str(bigNumber)
fileUnits = open(fileNameUnits, 'w')
for n in units:
    fileUnits.write(str(n)+'\n')
fileUnits.close()

# We calculate the twin units in Z/(bigNumber)Z.
twinUnits = []
for n in range(len(units)-1):
    if units[n+1] - units[n] == 2:
        twinUnits.append(units[n])
if units[-1] == bigNumber -1:
    twinUnits.append(units[-1]) 

# We save the twin units so that we do not need to calculate them again.
fileNameTwinUnits ='twinUnits_'+str(bigNumber)
fileTwinUnits = open(fileNameTwinUnits, 'w')
for n in twinUnits:
    fileTwinUnits.write(str(n)+'\n')
fileTwinUnits.close()


# We load the list of twin primes up to 10^9.
# This list was calculated from the list of primes under 10^9,
# generated using the prime_sieve package (see https://pypi.org/project/prime-sieve/)
fileNameTwinPrimes =  'list-of-twinsSieve.txt'
fileTwinPrimes = open(fileNameTwinPrimes, 'r')
twinPrimes =[]
for line in fileTwinPrimes:
    twinPrimes.append(int(line))
fileTwinPrimes.close()

# Finally we calculate the list of twin primes having 
# a twin unit of Z/(bigNumber)Z as residue when
# taking modulo (bigNumber).
# We remove those residues from the list of twin units
# and add them to the file finalList_(number).

fileNameFinalList = 'finalList_' + str(number)
fileFinalList = open(fileNameFinalList, 'w')
finalList=[]
for prime in twinPrimes:
    numberToCheck = prime % bigNumber
    if numberToCheck in twinUnits:
        twinUnits.remove(numberToCheck)
        finalList.append(numberToCheck)
        fileFinalList.write(str(numberToCheck)+'\n')
fileFinalList.close()