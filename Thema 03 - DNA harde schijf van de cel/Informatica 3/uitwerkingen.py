# === OPGAVE 1 ====

l = [0,1,1,2,3,6,8,12,21,28,34,55]
new_l = filter (lambda x: x<30 and x%3==0, l)
assert (list(new_l) == [0, 3, 6, 12, 21])


# === OPGAVE 2 ===
l1 = [1, 2, 3]
l2 = [4, 5, 6]

new_l = map(lambda x: x[0]+x[1], zip(l1,l2))
assert (list(new_l) == [5, 7, 9])

# === OPGAVE 3 ====
import re
rna = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGAAAAAAAA'
reg = r'^AUG[AUCG]{30,1000}A{5,10}$'
if re.match(reg,rna):
  print ('check')



# === OPGAVE 4 ====

class MRNAError(RuntimeError):
  def __init__(self, str):
    super().__init__(str)



class MRNA:
  def __init__(self, str):
    if (self.check_rna(str)):
      self.rna = str
    else:
      raise MRNAError('Geen valide RNA string')

  def __str__(self):
    rv = ''.join([ self.rna[i:i+3]+'-' for i in range(0, len(self.rna), 3)])
    # met deze constructie komt er een streepje te veel aan het eind van de string.
    # die haal ik met de onderstaande slice weer weg. Dit kan vast beter...
    return rv[:-1]

  def check_rna(self, str):
    if (len(str)%3 != 0):
      return False

    for i in str:
      if (i not in ['A','C','G','U']):
        return False

    return True


try:
  obj = MRNA('ACAGGUGCAACA')
  assert (type(obj) == MRNA)

  print(obj)

  obj2 = MRNA('FOOBAR')

except AssertionError:
  print ('Het object is niet van het goede type')
except NameError:
  print ('De klasse heeft niet de juiste naam')
except MRNAError:
  print ('De string is geen valide mRNA')







