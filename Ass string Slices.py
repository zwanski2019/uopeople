#Each time through the loop, the next character in the string is assigned to the variable
#letter . The loop continues until no characters are left.
#The following example shows how to use concatenation (string addition) and a for loop
#to generate an abecedarian series (that is, in alphabetical order). In Robert McCloskey’s
#book Make Way for Ducklings, the names of the ducklings are Jack, Kack, Lack, Mack, Nack,
#Ouack, Pack, and Quack. This loop outputs these names in order:

prefixes = "JKLMN0PQ"
suffix = "ack"
for letter in prefixes:
  print(letter + suffix)
#Output
#Python 3.7.4 (default, Jul  9 2019, 00:06:43)
#[GCC 6.3.0 20170516] on linux
#Jack
#Kack
#Lack
#Mack
#Nack
#0ack
#Pack
#Qack
