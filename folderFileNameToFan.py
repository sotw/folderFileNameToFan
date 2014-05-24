import os
import sys
from jianfan import jtof
from subprocess import Popen
from subprocess import PIPE

global tPath

def prepareRenamePara(oldName,newName):
	iOut = []
	iOut.append('mv')
	iOut.append(oldName)
	iOut.append(newName)
	return iOut

def scanAndProduceStack(aPath):
	outStack = []
	for dirPath, dirNames, fileNames in os.walk(aPath):
		outStack.append(dirPath)
		for f in fileNames:
			outStack.append(os.path.join(dirPath,f))
	return outStack

def main():
	FileNamePathSet = scanAndProduceStack(unicode(tPath))
	#use pop
	while len(FileNamePathSet) != 0:
		oldPath = FileNamePathSet.pop()
		newPath = jtof(oldPath)
		#print u"o:(%s) n:(%s)" %(oldPath,newPath)
		if newPath != oldPath:
			process = Popen(prepareRenamePara(oldPath,newPath))
			process.wait()

def verify():
	argc = len(sys.argv)
	if argc < 2 or argc > 2 :
		print "Format : Python %s <foldername>" %(sys.argv[0])
		exit(1)
	global tPath
	tPath = sys.argv[1]

if __name__ == '__main__':
	verify()
	main()
