import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--testScore1",help="Subject First")
parser.add_argument("--testScore2",help="Subject Second")
parser.add_argument("--testScore3",help="Subject Third")
parser.add_argument("--Operation",help="Operation",choices=["Average","Total","Scores"])

rrr=parser.parse_args()
print(rrr.testScore1)
print(rrr.testScore2)
print(rrr.testScore3)
print(rrr.Operation)

s1=int(rrr.testScore1)
s2=int(rrr.testScore2)
s3=int(rrr.testScore3)
result=None

if rrr.Operation=="Average":
    result=(s1+s2+s3)//3
elif rrr.Operation=="Total":
    result=s1+s2+s3
elif rrr.Operation=="Scores":
    result=("Subject First:"+str(s1)+" "+"Subject Second:"+str(s2) +" " +" Subject Third:"+str(s3))
else:
    print("Unsupported Operation ")

print("Result :",result)