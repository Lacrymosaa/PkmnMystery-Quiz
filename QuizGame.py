import random as rand
import mysql.connector
  
def Questionary(): 
    Brave = 0
    Calm = 0
    Docile = 0
    Hardy = 0
    Hasty = 0
    Impish = 0
    Jolly = 0
    Lonely = 0
    Naive = 0
    Quirky = 0
    Relaxed = 0
    Sassy = 0
    Timid = 0

    gone = [] #Store the already used ID
    i = 1; #While condition
    while i <= 10:
        r = rand.randint(1,55) #Get a random number
        while r in gone: #Re-randomize the generated number to not repeat
            r = rand.randint(1,55)
        gone.append(r)
        cursor.execute(f"SELECT * FROM questionary WHERE (ID) = {r};") #Select the row of the randomized ID
        result = cursor.fetchall() #Group all the rows in a array
        for row in result:
            id = row[0]
            print("\n" + str(row[1]) + "\n")
            print("1." + str(row[2]))
            print("2." + str(row[3]))
            if not row[4]:                    ###i couldnt make it disappear if its empty
                print("3." + str(row[4]))
            if not row[5]:
                print("4." + str(row[5]))
            n = int(input("Enter the number answer: ")) 

        if id == 1:
            if n == 1:
                Brave += 3
            elif n == 2:
                Hardy += 2
                Brave += 2
            elif n == 3:
                Docile += 1
                Timid += 1
                Relaxed += 1
            elif n == 4:
                Timid += 2
            else:
                quit()
                
        elif id == 2:
            if n == 1:
                Jolly += 3
            elif n == 2:
                Hardy += 2
            elif n == 3:
                Timid += 2
            else:
                quit()
                
        elif id == 3:
            if n == 1:
                Docile += 2
            elif n == 2:
                Naive += 1
                Lonely += 1
            elif n == 3:
                Sassy += 2
            else:
                quit()
                
        elif id == 4:
            if n == 1:
                Timid += 2
            elif n == 2:
                Hardy += 1
                Calm += 2
            elif n == 3:
                Naive += 1
                Brave += 2
                Impish += 1
            else:
                quit()
                
        elif id == 5:
            if n == 1:
                Hardy += 2
            elif n == 2:
                Relaxed += 2
            elif n == 3:
                Impish += 2
            else:
                quit()
                
        elif id == 6:
            if n == 1:
                Hardy += 1
                Impish += 2
            elif n == 2:
                Quirky += 2
                Sassy += 1
            else:
                quit()
                
        elif id == 7:
            if n == 1:
                Naive += 1
                Jolly += 2
            elif n == 2:
                Quirky += 1
                Sassy += 1
            else:
                quit()
                
        elif id == 8:
            if n == 1:
                Sassy += 1
                Relaxed += 2
            elif n == 2:
                Hardy += 2
                Hasty += 1
            else:
                quit()
                
        elif id == 9:
            if n == 1:
                Hardy += 2
                Docile += 1
            elif n == 2:
                Quirky += 2
            else:
                quit()
                
        elif id == 10:
            if n == 1:
                Brave += 3
            elif n == 2:
                Quirky += 2
            elif n == 3:
                Sassy += 2
            else:
                quit()
                
        elif id == 11:
            if n == 1:
                Calm += 1
                Docile += 2
            elif n == 2:
                Quirky += 1
                Sassy += 2
            else:
                quit()
                
        elif id == 12:
            if n == 1:
                Naive += 2
                Jolly += 1
            elif n == 2:
                Calm += 1
            else:
                quit()
                
        elif id == 13:
            if n == 1:
                Sassy += 2
                Impish += 1
            elif n == 2:
                Calm  += 2
            else:
                quit()
                
        elif id == 14:
            if n == 1:
                Calm += 2
            elif n == 2:
                Impish += 2
            else:
                quit()
                
        elif id == 15:
            if n == 1:
                Calm += 1
                Relaxed += 2
            elif n == 2:
                Hardy += 2
            else:
                quit()
                
        elif id == 16:
            if n == 1:
                Timid += 1
                Lonely += 2
            elif n == 2:
                Sassy += 2
            else:
                quit()
                
        elif id == 17:
            if n == 1:
                Relaxed += 2
            elif n == 2:
                Hasty += 2
            else:
                quit()
                
        elif id == 18:
            if n == 1:
                Timid += 1
                Lonely += 2
            elif n == 2:
                Impish += 2
            else:
                quit()
                
        elif id == 19:
            if n == 1:
                Naive += 3
                Impish += 1
            elif n == 2:
                Jolly += 2
            elif n == 3:
                Sassy += 2
            else:
                quit()
                
        elif id == 20:
            if n == 1:
                Impish += 2
            elif n == 2:
                Docile += 1
                Relaxed += 1
            else:
                quit()
                
        elif id == 21:
            if n == 1:
                Timid += 2
                Impish += 1
            elif n == 2:
                Calm += 2
                Lonely += 1
            else:
                quit()
                
        elif id == 22:
            if n == 1:
                Naive += 2
            elif n == 2:
                Hasty += 2
            else:
                quit()
                
        elif id == 23:
            if n == 1:
                Lonely += 1
                Jolly += 2
            elif n == 2:
                Timid += 1
            else:
                quit()
                
        elif id == 24:
            if n == 1:
                Calm += 2
                Relaxed += 1
            elif n == 2:
                Hardy += 1
                Hasty += 2
            else:
                quit()
                
        elif id == 25:
            if n == 1:
                Calm += 2
                Docile += 1
            elif n == 2:
                Hardy += 2
            else:
                quit()
                
        elif id == 26:
            if n == 1:
                Quirky += 2
            elif n == 2:
                Hardy += 2
            else:
                quit()
                
        elif id == 27:
            if n == 1:
                Docile += 1
                Naive += 2
            elif n == 2:
                Quirky += 2
            else:
                quit()
                
        elif id == 28:
            if n == 1:
                Sassy += 2
            elif n == 2:
                Relaxed += 2
            else:
                quit()
                
        elif id == 29:
            if n == 1:
                Timid += 2
            elif n == 2:
                Hasty += 2
            elif n == 3:
                Jolly += 2
            elif n == 4:
                Sassy += 2
            else:
                quit()
                
        elif id == 30:
            if n == 1:
                Lonely += 1
                Impish += 2
            elif n == 2:
                Calm += 2
            else:
                quit()
                
        elif id == 31:
            if n == 1:
                Hardy += 1
                Hasty += 1
            elif n == 2:
                Quirky += 2
            elif n == 3:
                Sassy += 2
            else:
                quit()
                
        elif id == 32:
            if n == 1:
                Jolly += 2 
            elif n == 2:
                Relaxed += 2
            elif n == 3:
                Hasty += 2
            else:
                quit()
                
        elif id == 33:
            if n == 1:
                Lonely += 1
                Jolly += 1
            elif n == 2:
                Calm += 1
                Relaxed += 2
            elif n == 3:
                Timid += 1
                Lonely += 3
            else:
                quit()
                
        elif id == 34:
            if n == 1:
                Jolly += 2
            elif n == 2:
                Quirky += 1
                Sassy += 1
            else:
                quit()
                
        elif id == 35:
            if n == 1:
                Jolly += 2
            elif n == 2:
                Calm += 2
            elif n == 3:
                Quirky += 2
            else:
                quit()
                
        elif id == 36:
            if n == 1:
                Quirky += 1
                Hasty += 1
            elif n == 2:
                Lonely += 1
                Jolly += 1
            else:
                quit()
                
        elif id == 37:
            if n == 1:
                Lonely += 1
                Naive += 1
            elif n == 2:
                Hasty += 1
                Sassy += 1
            else:
                quit()
                
        elif id == 38:
            if n == 1:
                Docile += 2
            elif n == 2:
                Sassy += 2
            elif n == 3:
                Quirky += 2
            else:
                quit()
                
        elif id == 39:
            if n == 1:
                Hardy += 2
            elif n == 2:
                Calm += 2
            elif n == 3:
                Quirky += 2
            else:
                quit()
                
        elif id == 40:
            if n == 1:
                Hardy += 1
                Brave += 3
            elif n == 2:
                Quirky += 2
            elif n == 3:
                Impish += 2
            elif n == 4:
                Timid += 2
            else:
                quit()
                
        elif id == 41:
            if n == 1:
                Hardy += 1
                Brave += 3
            elif n == 2:
                Naive += 2
            else:
                quit()
                
        elif id == 42:
            if n == 1:
                Docile += 2
            elif n == 2:
                Naive += 2
            elif n == 3:
                Impish += 2
            else:
                quit()
                
        elif id == 43:
            if n == 1:
                Brave += 2
            elif n == 2:
                Timid += 2
            elif n == 3:
                Relaxed += 2
            else:
                quit()
                
        elif id == 44:
            if n == 1:
                Timid += 1
                Lonely += 2
            elif n == 2:
                Calm += 2
            else:
                quit()
                
        elif id == 45:
            if n == 1:
                Hardy += 2
                Brave += 2
            elif n == 2:
                Quirky += 2
                Sassy += 2
            else:
                quit()
                
        elif id == 46:
            if n == 1:
                Docile += 2
                Naive += 1
            elif n == 2:
                Timid += 2
                Calm += 1
            else:
                quit()
                
        elif id == 47:
            if n == 1:
                Timid += 2
            elif n == 2:
                Lonely += 2
            elif n == 3:
                Quirky += 1
                Impish += 2
            else:
                quit()
                
        elif id == 48:
            if n == 1:
                Docile += 2
                Hasty += 1
            elif n == 2:
                Relaxed += 1
                Naive += 2
            else:
                quit()
                
        elif id == 49:
            if n == 1:
                Hasty += 2
            elif n == 2:
                Timid += 2
            elif n == 3:
                Sassy += 2
            else:
                quit()
                
        elif id == 50:
            if n == 1:
                Hasty += 1
                Jolly += 2
            elif n == 2:
                Hardy += 1
                Quirky += 1
            elif n == 3:
                Quirky += 2
                Brave += 1
            else:
                quit()
                
        elif id == 51:
            if n == 1:
                Hasty += 2
            elif n == 2:
                Calm += 2
            elif n == 3:
                Timid += 2
            else:
                quit()
                
        elif id == 52:
            if n == 1:
                Calm += 2
            elif n == 2:
                Docile += 2
            elif n == 3:
                Sassy += 2
            else:
                quit()
                
        elif id == 53:
            if n == 1:
                Docile += 1
                Hasty += 2
            elif n == 2:
                Relaxed += 2
            elif n == 3:
                Hasty += 3
            else:
                quit()
                
        elif id == 54:
            if n == 1:
                Brave += 3
            elif n == 2:
                Timid += 2
            elif n == 3:
                Brave += 3
                Impish += 1
            else:
                quit()
                
        elif id == 55:
            if n == 1:
                Brave += 3
                Impish += 1
            elif n == 2:
                Timid += 1
                Docile += 2
            else:
                quit()

        i += 1
        
    natures = [Brave, Calm, Docile, Hardy, Hasty, Impish, Jolly, Lonely, Naive, Quirky, Relaxed, Sassy, Timid]
    fnn = max(natures)
    fna = natures.index(fnn)
    natures = {Brave: "Brave", Calm: "Calm", Docile: "Docile", Hardy: "Hardy", Hasty: "Hasty", Impish: "Impish", Jolly: "Jolly", Lonely: "Lonely", Naive: "Naive", Quirky: "Quirky", Relaxed: "Relaxed", Sassy: "Sassy", Timid: "Timid"}
    print(natures[fna])
    if natures[fna] == "Brave":
        print("Congratulations, you're a Machop!")
    elif natures[fna] == "Calm":
        print("Congratulations, you're a Mudkip!")
    elif natures[fna] == "Docile":
        print("Congratulations, you're a Bulbasaur!")
    elif natures[fna] == "Hardy":
        print("Congratulations, you're a Charmander!")
    elif natures[fna] == "Hasty":
        print("Congratulations, you're a Torchic!") 
    elif natures[fna] == "Impish":
        print("Congratulations, you're a Pikachu!")
    elif natures[fna] == "Jolly":
        print("Congratulations, you're a Squirtle!")
    elif natures[fna] == "Lonely":
        print("Congratulations, you're a Cubone!")
    elif natures[fna] == "Naive":
        print("Congratulations, you're a Totodile!")
    elif natures[fna] == "Quirky":
        print("Congratulations, you're a Meowth!")
    elif natures[fna] == "Relaxed":
        print("Congratulations, you're a Psyduck!")
    elif natures[fna] == "Sassy":
        print("Congratulations, you're a Treecko!")
    elif natures[fna] == "Timid":
        print("Congratulations, you're a Cyndaquil!")

                
        
db = mysql.connector.connect(
    host = "localhost",
    username = "marian",
    password = "password1",
    database = "redandblue"
)

cursor = db.cursor()

print('Welcome to my Quiz!')
name = input("What is your name? ")

n = 1 #i forgot how do this repetition with just the answer
while n == 1:    
    ans = input("Do you want to play(yes/no): ").lower()
    if ans == "yes":
        break
    elif ans == "no":
        quit()
    else:
        print("The answer need to be yes or no") 

Questionary()






