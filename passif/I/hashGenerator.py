import sys
import hashlib

salt1 = "hei568d3"
salt2 = "kkoek693"
flagPrefix = "FLAG-"

class HashGenerator:

	def generateHash(self, flag):
		saltedFlag = salt1 + flag + salt2
		return hashlib.sha256(saltedFlag.encode("utf-8")).hexdigest()
		
	def validate(self, flag):
		if not flag.startswith(flagPrefix):
			print("flag is invalid, should start with the proper prefix")
			return False;
		coreFlag = flag[len(flagPrefix):]
		if len(coreFlag) < 8:
			print("flag is invalid, too short")
			return False;
		if len(coreFlag) > 8:
			print("flag is invalid, too long ....")
			return False;
		if not coreFlag.isdigit():
			print("flag is invalid, except prefix everything should be numbers ....")
			return False;
		print("flag is valid. " + flagPrefix + "********")
		return True;


if __name__ == "__main__":
	hashGenerator = HashGenerator()
	flaghash = cdb4a34ff782b0493874a40475f84ec958fb4541886d1e9be7c7ac70976107b1
	for num in range(0,99999999999999):
		if salt1 + num + salt2 == flaghash:
			print(num)
	if hashGenerator.validate(flag):
		hash = hashGenerator.generateHash(flag)
		print("the super secret hash is: " + hash)