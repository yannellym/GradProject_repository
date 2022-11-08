def main():
    
   dic = {38:17, 42:96, 54:18, 56:56, 81:96} 

   for k in dic:

      ans = dic.get(k, "absent")

      if (ans == "absent"):

         print(k, "is", ans)

      else:

         if (k < ans):

            print(k, "has the smaller", ans)

         else:

            print(k, "has the value", ans)

 

main()