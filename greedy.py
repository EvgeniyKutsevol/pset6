def main():
   print("Give me money:")
   value = (float)(input())
   
   toCent = value * 100;
   
   
   quarter = 25
   dimes = 10
   nikel = 5
   penni = 1 
   
   coinCounter = 0
   
   while toCent >= quarter:
      toCent = toCent - quarter
      coinCounter+=1

   while toCent >= dimes:
      toCent = toCent - dimes
      coinCounter+=1

   while toCent >= nikel:
      toCent = toCent - nikel
      coinCounter+=1

   while toCent >= penni:
      toCent = toCent - penni
      coinCounter+=1

   print("Coins: ")    
   print(coinCounter)
   
   
if __name__ == "__main__":
    main()