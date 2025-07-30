#welcome here

print("Welcome to China!")
print("You are a woman and people in our village thinks you're weird.")
print("Also, your dad is sick but he just got a letter saying he has to go to war.")
print("Do you wanna take his place and pretend to be a man?")

warChoice = input("> ")

if(warChoice == "yes"):
    print("You steal the letter, his sword and horse, and go to the camp.")
    print("People also don't like you very much here.")
    print("You get your commander so angry that he starts singing.")
    print("Do you wanna sing along?")

    singChoice = input("> ")

    if(singChoice == "yes"):
        print("The power of music fills your heart and makes you overcome obstacles.")
        print("You are accepted by your comrades and become a valuable soldier.")
        print("While traveling, you are attacked by an army of enemies. The leader advances against you, and you have a explosive.")
        print("Do you wanna aim to the leader?")

        killChoice = input("> ")

        if(killChoice == "yes"):
            print("You aim your explosive in the leader. He's dead!")
            print("So are you, because you were too close. And your comrades are killed by rest of the enemies.")
            print("The war goes on without you, as a new enemy's leader emerges, but you will be know for killing the first one.")

        elif(killChoice == "no"):
           print("You aim to the mountains instead and starts an avalanche!")
           print("The enemies get burried and your comrades survive. Sadly, you were injured, and they discover you're a woman.")
           print("You are abandoned in the mountains for having a vagina. You are about to go back home, but notice some of the enemies are actually alive.")
           print("Do you go after your comrades and warn them?")

           warnChoice = input("> ")

           if(warnChoice == "yes"):
              print("You go after them. They don't believe you at first, but when the emperor is kidnapped right in front of them, they decide to heard your.")
              print("With your brain and the power of crossdress, you infiltrate the castle, kills the enemies and saves the emperor.")
              print("There are even fireworks!")
              print("The emperor is grateful for your help and offers you a job as his counselor. Do you accept?")

              counselorChoice = input("> ")

              if(counselorChoice == "yes"):
                 print("You got a new job!")
                 print("Being a counselor is interesting and you get a lot of luxuries, which is nice")
                 print("You see right through the noble's bullshit, and makes some new enemies in the process.")
                 print("After 2 years you got poisoned and died, but as an honor to your family.")

              elif(counselorChoice == "no"):
                 print("You decide to go back home and bring some souvenirs back.")
                 print("Your dad is very happy to see you again and you're welcomed back.")
                 print("Your commander also followed you and now is trying to flirt.")
                 print("Do you invite him to stay for dinner?")

                 dinnerChoice = input("> ")

                 if(dinnerChoice == "yes"):
                    print("Your commander stays for dinner.")
                    print("You eventually get engaged, and this leads to a second movie of dubious quality.")
                    print("At the end you get married tho, inherit you dad's farm, and live happily.")

                 elif(dinnerChoice == "no"):
                    print("You and the commander stay in an ankward silence until he leaves.")
                    print("Now everyone in the village likes you. You're weird, but famous, so now you're 'eccentric'.")
                    print("You live the rest of your life happily with your family and at some point become renowned a kung-fu teacher.")

                 else:
                    print("Invalid choice. Enter yes or no.")

              else:
                 print("Invalid choice. Enter yes or no.")
              
           elif(warnChoice == "no"):
              print("You decide to go home. They were assholes to you anyway.")
              print("Your family is mad at you for running away but they're happy you're alive.")
              print("Some time after, you get the news that the emperor was killed and now the country is being runned by the enemies.")
              print("Your village is really too far away from anything, tho, so it doesn't change anything in your life.")
              print("At least the war is over.")

           else:
              print("Invalid choice. Enter yes or no.")




        else:
            print("Invalid choice. Enter yes or no")

    elif(singChoice == "no"):
        print("You watch an impressive training montage.")
        print("Sadly, none of this affects you.")
        print("You commander will never make a man out of you. You desert the army and spend the rest of your days as a beggar.")

    else:
        print("Invalid choice. Enter yes or no")

elif(warChoice == "no"):
 print("Your dad goes to war and you stay home.")
 print("He dies pretty quickly and you're married off to survive.")
 print("Congratulations! Now you have a 60-year-old husband and 5 kids.")

else:
 print("Invalid choice. Enter yes or no")


input("Press ENTER to exit")