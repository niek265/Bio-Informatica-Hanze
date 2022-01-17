#/usr/bin/python3
'''
Name:			aminoacid.py
Purpose:		Can be used as a tool to learn the names, three letter codes and one letter codes of the 20 humane amino acids.
				At the end it prints the amount of mistakes that were made, plus the time it took to answer the questions.
Author:			Lonneke Scheffer
Created:		September 21, 2014
Latest update:	November 3, 2014

Please contact me if any bugs are found;
lonsch96@live.nl
'''

import random, time

class AminoAcid():
	mistakes = 0
	def __init__(self, full_name, three_letter_code, one_letter_code, group):
		self.full_name = full_name
		self.three_letter_code = three_letter_code
		self.one_letter_code = one_letter_code
		self.group = group
		
		self.from_name = False
		self.from_three_letter_code = False
		self.from_one_letter_code = False
	
	def __str__(self):
		'''
		Returns a string representation of the AminoAcid object.
		'''
		return "Amino acid: {} - {} - {}\nGuessed from name? {}\nGuessed from three letter code? {}\nGuessed from one letter code? {}".format(self.full_name, self.three_letter_code, self.one_letter_code, self.from_name, self.from_three_letter_code, self.from_one_letter_code)
	
	def question(self, print_statement, first_question, first_answer, second_question, second_answer):
		'''
		Prints the first statement (for instance, the name), then asks the two questions (for instance, three letter code and one letter code)
		Only returns True if both answers are right at the first try
		'''
		both_right = True
		
		print(print_statement)
		
		for question, answer in [(first_question, first_answer), (second_question, second_answer)]:
			user_answer = input(question)
			while user_answer.upper() != answer.upper():
				both_right = False
				AminoAcid.mistakes += 1
				user_answer = input("Try again; "+question)
		
		return both_right
		
	def group_guess(self):
		'''
		Comparable with method 'question', asks for the amino acid group and returns wether it was guessed at the first try or not.
		'''
		
		answer_true = True
		
		user_answer = input("The group of {} is: ".format(self.full_name))
		while not user_answer.upper() in self.group:
			answer_true = False
			AminoAcid.mistakes += 1
			user_answer = input("Try again: ")
			
		return answer_true
	
	def guess(self):
		'''
		Checks what question needs to be asked and calls the question() function.
		Sets the from_name, from_three_letter_code and from_one_letter_code to True if they are guessed.
		Only returns True if all questions are right.
		'''
		if not self.from_name:
			self.from_name = self.question("Name: "+self.full_name, "Three letter code: ", self.three_letter_code, "One letter code: ", self.one_letter_code)
			return False
		elif not self.from_three_letter_code:
			self.from_three_letter_code = self.question("Three letter code: "+self.three_letter_code, "Name: ", self.full_name, "One letter code: ", self.one_letter_code)
			return False
		elif not self.from_one_letter_code:
			self.from_one_letter_code = self.question("One letter code: "+self.one_letter_code, "Name: ", self.full_name, "Three letter code: ", self.three_letter_code)
			return False
		else:
			return True
			

def createAminoAcids():
	'''
	Creates the amino acids (objects) that are going to be used,
	returns a list of AminoAcid objects.
	
	Remove or add amino acids here if neccessary.
	'''
	
	apolar = ["APOLAR", "AP"]
	polar_uncharged = ["POLAR UNCHARGED", "POLAR", "P"]
	acidic = ["POLAR ACIDIC", "ACIDIC", "AC"]
	basic = ["POLAR BASIC", "BASIC", "B"]
	
	a = AminoAcid("Alanine", "Ala", "A", apolar)
	r = AminoAcid("Arginine", "Arg", "R", basic)
	n = AminoAcid("Asparagine", "Asn", "N", polar_uncharged)
	d = AminoAcid("Aspartic Acid", "Asp", "D", acidic)
	c = AminoAcid("Cysteine", "Cys", "C", polar_uncharged)
	e = AminoAcid("Glutamic Acid", "Glu", "E", acidic)
	q = AminoAcid("Glutamine", "Gln", "Q", polar_uncharged)
	g = AminoAcid("Glycine", "Gly", "G", apolar)
	h = AminoAcid("Histidine", "His", "H", basic)
	i = AminoAcid("Isoleucine", "Ile", "I", apolar)
	l = AminoAcid("Leucine", "Leu", "L", apolar)
	k = AminoAcid("Lysine", "Lys", "K", basic)
	m = AminoAcid("Methionine", "Met", "M", apolar)
	f = AminoAcid("Phenylalanine", "Phe", "F", apolar)
	p = AminoAcid("Proline", "Pro", "P", apolar)
	s = AminoAcid("Serine", "Ser", "S", polar_uncharged)
	t = AminoAcid("Threonine", "Thr", "T", polar_uncharged)
	w = AminoAcid("Tryptophan", "Trp", "W", apolar)
	y = AminoAcid("Tyrosine", "Tyr", "Y", polar_uncharged)
	v = AminoAcid("Valine", "Val", "V", apolar)
	
	return [a, r, n, d, c, e, q, g, h, i, l, k, m, f, p, s, t, w, y, v]


def main():
	all_amino_acids = createAminoAcids()
	guess_name = list(all_amino_acids)
	guess_group = list(all_amino_acids)
	
	startTime = time.time()
	
	while guess_name:
		current_amino_acid = random.choice(guess_name)
		if current_amino_acid.guess() == True:
			guess_name.remove(current_amino_acid)

	# Uncomment this part if you want to practice the amino acid groups too		
	while guess_group:
		current_amino_acid = random.choice(guess_group)
		if current_amino_acid.group_guess() == True:
			guess_group.remove(current_amino_acid)
			
	print(time.strftime("\n\nTimer: %H:%M:%S", time.gmtime(time.time() - startTime)))
	print("{} mistakes were made\n".format(AminoAcid.mistakes))
	
if __name__ == "__main__":
	main()
else:
	main()
