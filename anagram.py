S1 = "stop"
S2 = "pots"

def anagram(S1,S2):
  if (sorted(S1) == sorted(S2)):
    print ("Yes, anagram")
  else:
    print ("Not an anagram")

anagram(S1,S2)
