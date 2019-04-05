import distance

text1 = "삼성전자, 1분기 어닝쇼크에도 보합세 지속"
text2 = "삼성전자 어닝쇼크, 1분기 보합세 지속"

sim = distance.jaccard(text1,text2)
print(sim)
