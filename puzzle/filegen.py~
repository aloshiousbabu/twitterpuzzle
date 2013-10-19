import time
from operator import itemgetter
import sys
import puzzle
class FileGenerator():
	def generate(self,name):

		"""create UserDetails() object"""
		userDetails=puzzle.UserDetails()
		
		"""Get details corresponding to 'name' """
		result=userDetails.fetch(name)
		if result!="ratelimit":
			profilePic=result[0]
			followers=result[1]
			f = open("./files/"+str(name),"w")
			"""write profile Details"""
			f.write(str(name)+","+str(profilePic)+"|")
			for follower in followers:
				"""writes follower details"""	
				f.write(str(follower[0])+","+str(follower[2])+","+str(follower[3])+";")
			f.close()
			print "File Generated to ./files"
			
if __name__ == "__main__":
	fileGenerator=FileGenerator()
	fileGenerator.generate(sys.argv[1])
