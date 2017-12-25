#coding=utf-8
import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-i','--input',help='unicode string you want to convert')
args=parser.parse_args()

if __name__=='__main__':
	str=args.input
	print 'you typed in: '+str
	if str==None:
		print 'for usage: ' + __file__ + ' --help'
		exit(2)
	print 'result: '+str.decode('unicode-escape')
