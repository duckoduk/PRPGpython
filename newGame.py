import json
import time #invt 는 인벤토리안의 툴 invw는 인벤토리안의 무기 invf 는 인벤토리안의 음식
from random import seed
from random import randint
import math
invt = "nothing"
bread = 0
carrot = 0
seed = 0
Carrotstr = 'Carrots:'+str(carrot)
Breadstr = 'Bread:'+str(bread)
Seedstr = 'Seeds:'+str(seed)
invf = Carrotstr, Breadstr
invw = "nothing"
Pickaxe = "nothing"
Axe = "nothing"
Hoe = "nothing"
Weapon = "nothing"
Opponent = "None"
strength = 1
OpponentHealth = 0
Damage = 0
turn = 0
UserHealth = 100
Prize = 0
cash = 100
played = 1
print("Hello! What's your name?")
User = input(">>> ")
print ("???: Oh hello, nice to meet you "+User+"!")
print ("???: My name is Elizabeth.")
print ("Elizabeth: Do you wish to start your game?")
answer = input("[yes or no?] ")
if answer == "yes":
    print ("Ok, wait a sec...")
    time.sleep(0.5)
    print ("[Creating world...]")
    time.sleep(0.5)
    print ("[Entering.....]")
    time.sleep(0.5)
    print ("[System: "+User+" has entered.]")
    print ("[System: welcome "+User+"!")
    time.sleep(0.5)
    print ("???: Oh hello, "+User+"!","I'm Hehg")
    print ("Welcome to the Herba Village!")
    print ("I'll show you what you can do in this place.")
    print ("Ok!", "Controls:", "A: Hunt","C: Chop Trees","M: Mine","B: Open Bazaar","S: Show Stats","I: Inventory","X: Exit","T: Show Tutorial", sep='\n')
    time.sleep(3)
    print(" ")
    print("This is what you can do in the village.")
    time.sleep(1)
    print("If you want to read this again, open the tutorial book with 't'!")
    while True:
        control = input(">>> ")
        if control == "b":
            print ("1. Tools", "2.Weapons", "3. Foods", "Your Current Cash:",cash, "[Press C to cancel]")
            bcon = input("[Press C to cancel]")
            if bcon == "1":
                print ("Tools","1. Axes","2. Pickaxes","3. Hoes","Your Current Cash: ",cash)
                tc = input (">>> ")
                if tc == "1":
                    print ("Axes","1. Wood Axe : 100 cash","2. Stone Axe : 500 cash","3. Iron Axe : 2000 cash","4. Diamond Axe : 6000 cash")
                    ac = input (">>> ")
                    if ac == "1":
                        if cash >= 100:
                            print ("You have purchased Wood Axe!")
                            invt = invt + ",Wood Axe"
                            Axe = "Wood Axe"
                            cash = cash - 100
                        elif cash < 100:
                            print ("You don't have enough cash to buy")
                    if ac == "2":
                        if cash >= 500:
                            print ("You have purchased Stone Axe!")
                            invt = invt + ",Stone Axe"
                            Axe = "nothing"
                            Axe = "Stone Axe"
                            cash = cash - 500
                        elif cash < 500:
                            print ("You don't have enough cash to buy")
                    if ac == "3":
                        if cash >= 2000:
                            print ("You have purchased Iron Axe!")
                            invt = invt + ",Iron Axe"
                            Axe = "nothing"
                            Axe = "Iron Axe"
                            cash = cash - 2000
                        elif cash < 2000:
                            print ("You don't have enough cash to buy")
                    if ac == "4":
                        if cash >= 6000:
                            print ("You have purchased Diamond Axe!")
                            invt = invt + ",Diamond Axe"
                            Axe = "nothing"
                            Axe = "Diamond Axe"
                            cash = cash - 6000
                        elif cash < 6000:
                            print ("You don't have enough cash to buy")
                    
                if tc == "2": #여기서부터
                    print ("Axes","1. Wood Pickaxe : 300 cash","2. Stone pickaxe : 800 cash","3. Iron pickaxe : 2400 cash","4. Diamond Pickaxe : 6400 cash")
                    pc = input (">>> ")
                    if pc == "1":
                        if cash >= 300:
                            print ("You have purchased Wood Pickaxe!")
                            invt = invt + ",Wood Pickaxe"
                            Pickaxe = "Wood Pickaxe"
                            cash = cash - 300
                        elif cash < 300:
                            print ("You don't have enough cash to buy")
                    if pc == "2":
                        if cash >= 800:
                            print ("You have purchased Stone Pickaxe!")
                            invt = invt + ",Stone Pickaxe"
                            Pickaxe = "nothing"
                            Pickaxe = "Stone Pickaxe"
                            cash = cash - 800
                        elif cash < 800:
                            print ("You don't have enough cash to buy")
                    if pc == "3":
                        if cash >= 2400:
                            print ("You have purchased Iron Pickaxe!")
                            invt = invt + ",Iron Pickaxe"
                            Pickaxe = "nothing"
                            Pickaxe = "Iron Pickaxe"
                            cash = cash - 2400
                        elif cash < 2400:
                            print ("You don't have enough cash to buy")
                    if pc == "4":
                        if cash >= 6400:
                            print ("You have purchased Diamond Pickaxe!")
                            invt = invt + ",Diamond Pickaxe"
                            Pickaxe = "nothing"
                            Pickaxe = "Diamond Pickaxe"
                            cash = cash - 6400
                        elif cash < 6400:
                            print ("You don't have enough cash to buy") 
                    
                if tc == "3":
                    print ("Hoes","1. Wood Hoe : 500 cash","2. Stone Hoe : 1500 cash","3. Iron Hoe : 3500 cash","4. Diamond Hoe : 7000 cash")
                    hc = input (">>> ")
                    if hc == "1":
                        if cash >= 500:
                            print ("You have purchased Wood Hoe!")
                            invt = "Wood Hoe"
                            Hoe = "Wood Hoe"
                            cash = cash - 500
                        elif cash < 500:
                            print ("You don't have enough cash to buy")
                    if hc == "2":
                        if cash >= 1500:
                            print ("You have purchased Stone Hoe!")
                            invt = invt + ",Stone Hoe"
                            Hoe = "nothing"
                            Hoe = "Stone Hoe"
                            cash = cash - 1500
                        elif cash < 1500:
                            print ("You don't have enough cash to buy")
                    if hc == "3":
                        if cash >= 3500:
                            print ("You have purchased Iron Hoe!")
                            invt = invt + ",Iron Hoe"
                            Hoe = "nothing"
                            Hoe = "Iron Hoe"
                            cash = cash - 3500
                        elif cash < 3500:
                            print ("You don't have enough cash to buy")
                    if hc == "4":
                        if cash >= 7000:
                            print ("You have purchased Diamond Hoe!")
                            invt = invt + ",Diamond Hoe"
                            Hoe = "nothing"
                            Hoe = "Diamond Hoe"
                            cash = cash - 7000
                        elif cash < 7000:
                            print ("You don't have enough cash to buy")
                

                            


                
            

            if bcon == "2":
                print ("Weapons","1. Swords")
                wc = input (">>> ")
                if wc == "1":
                    print ("Swords","1. Wood Sword : 100 cash","2. Stone Sword : 500 cash","3. Iron Sword : 3000 cash","4. Diamond Sword : 6000 cash",sep='\n')
                    sc = input("[What Sword Do You Want?]")
                    if sc == "1":
                        if cash >= 100:
                            print ("You have purchased Wood Sword!")
                            invw = "Wood Sword"
                            Weapon = "nothing"
                            Weapon = "Wood Sword"
                            cash = cash - 100
                        elif cash < 100:
                            print ("You don't have enough cash to buy")
                    if sc == "2":
                        if cash >= 500:
                            print ("You have purchased Stone Sword!")
                            invw = invw + ",Stone Sword"
                            Weapon = "nothing"
                            Weapon = "Stone Sword"
                            cash = cash - 500
                        elif cash < 500:
                            print ("You don't have enough cash to buy")
                    if sc == "3":
                        if cash >= 3000:
                            print ("You have purchased Iron Sword!")
                            invw = invw + ",Iron Sword"
                            Weapon = "nothing"
                            Weapon = "Iron Sword"
                            cash = cash - 3000
                        elif cash < 3000:
                            print ("You don't have enough cash to buy")
                    if sc == "4":
                        if cash >= 6000:
                            print ("You have purchased Diamond Sword!")
                            invw = invw + ",Diamond Sword"
                            Weapon = "nothing"
                            Weapon = "Diamond Sword"
                            cash = cash - 6000
                        elif cash < 6000:
                            print ("You don't have enough cash to buy")
                        
    
            if bcon == "3":
                print ("Foods","1. Carrot : 10 cash","2. Bread : 25 cash", "Current Cash: " + str(cash) ,sep='\n') 
                fc = input (">>> ")
                if fc == "1":
                    if cash >= 10:
                        print ("You have purchased a Carrot!")
                        carrot = carrot + 1     
                        Carrotstr = 'Carrots:'+str(carrot)   
                        cash = cash - 10
                    elif cash < 10:
                        print ("You don't have enough cash to buy")
                if fc == "2":
                    if cash >= 25:
                        print ("You have purchased a Bread!")
                        bread = bread + 1
                        Breadstr = 'Bread:'+str(bread)
                        cash = cash - 25
                    elif cash < 25:
                        print ("You don't have enough cash to buy")
                
            if bcon == "c":
                    print ("Ok Canceled")

            else:
                    print ("Shop Closed")
                
        if control == "c":   #여기부터 c 버튼에 대한것 
            while True:
                if Axe == "nothing": #도구가 없을때
                    print ("You have no tool, go to Bazaar and buy some")
                    break
                if Axe == "Wood Axe": #나무 망치일떄
                    gain = randint(5, 15)
                    cash = cash + gain
                    print ("You went to the forest with a Wood Axe...")
                    time.sleep(0.5)
                    print ("And sold the gains.")
                    time.sleep(0.5)
                    print ("Your current cash: "+str(cash))
                    mcon = input('C to cancel')
                    if mcon =='c':
                        break
                    else:
                        continue
                if Axe == "Stone Axe": #철 망치
                    gain = randint(10, 20)
                    cash = cash + gain
                    print ("You went to the forest with a Stone Axe...")
                    time.sleep(0.5)
                    print ("And sold the gains.")
                    time.sleep(0.5)
                    print ("Your current cash: "+str(cash))
                    mcon = input('C to cancel')
                    if mcon =='c':
                        break
                    else:
                        continue
                if Axe == "Iron Axe":
                    gain = randint(30, 40)
                    cash = cash + gain
                    print ("You went to the forest with a Iron Axe...")
                    time.sleep(0.5)
                    print ("And sold the gains.")
                    time.sleep(0.5)
                    print ("Your current cash: "+str(cash))
                    mcon = input('C to cancel')
                    if mcon =='c':
                        break
                    else:
                        continue
                if Axe == "Diamond Axe":
                    gain = randint(70, 100)
                    cash = cash + gain
                    print ("You went to the forest with a Diamond Axe...")
                    time.sleep(0.5)
                    print ("And sold the gains.")
                    time.sleep(0.5)
                    print ("Your current cash: "+str(cash))
                    mcon = input('C to cancel')
                    if mcon =='c':
                        break
                    else:
                        continue
        
        if control == "m":
            if Pickaxe == "nothing":
                print("You have no pickaxe! Go to Bazaar and buy one!")
            if Axe == "Wood Axe": #나무 망치일떄
                gain = randint(5, 15)
                cash = cash + gain
                print ("You went to the mine with a Wood Pickaxe...")
                time.sleep(0.5)
                print ("And sold the gains.")
                time.sleep(0.5)
                print ("Your current cash: "+str(cash))
                mcon = input('C to cancel')
                if mcon =='c':
                    break
                else:
                    continue
            if Axe == "Stone Axe": #나무 망치일떄
                gain = randint(20, 30)
                cash = cash + gain
                print ("You went to the mine with a Stone Pickaxe...")
                time.sleep(0.5)
                print ("And sold the gains.")
                time.sleep(0.5)
                print ("Your current cash: "+str(cash))
                mcon = input('C to cancel')
                if mcon =='c':
                    break
                else:
                    continue
            if Axe == "Iron Axe": #나무 망치일떄
                gain = randint(30, 40)
                cash = cash + gain
                print ("You went to the mine with a Iron Pickaxe...")
                time.sleep(0.5)
                print ("And sold the gains.")
                time.sleep(0.5)
                print ("Your current cash: "+str(cash))
                mcon = input('C to cancel')
                if mcon =='c':
                    break
                else:
                    continue
            if Axe == "Diamond Axe": #나무 망치일떄
                gain = randint(70, 100)
                cash = cash + gain
                print ("You went to the mine with a Diamond Pickaxe...")
                time.sleep(0.5)
                print ("And sold the gains.")
                time.sleep(0.5)
                print ("Your current cash: "+str(cash))
                mcon = input('C to cancel')
                if mcon =='c':
                    break
                else:
                    continue
        
        if control == "x":
            break

        if control == "i":
            print ("1. Weapons, 2. Tools, 3: Foods")
            ic = input ("C to cancel")
            if ic == "1":
                print ("Weapons",invw,sep='\n')
            if ic == "2":
                print ("Tools",invt,sep='\n')
            if ic == "3":
                print ("Foods")
                print(str(Carrotstr)+' '+str(Breadstr))
                econ= input("What do you want to eat?>>>")
                if econ == "carrot":
                    if carrot > 0:
                        carrot = carrot - 1
                        Carrotstr = 'Carrots:'+str(carrot)  
                        strength = strength + 0.1
                        print("You have ate your Carrot!")
                        print("Now Your strength is",strength)
                    else:
                        print("You don't have any Carrots left")
                if econ == "bread":
                    if bread > 0:
                        bread = bread - 1
                        Breadstr = 'Breads:'+str(Breadstr)
                        strength = strength + 0.2
                        print("You have ate your Bread!")
                        print("Now Your strength is",strength)
                    else:
                        print("You don't have any Bread left")

                
                        

        if control == "s":
            print ("Your Current Cash: ",cash)

        if control == "t":
            print('1. controls','2. guide', sep='\n')
            tcon = input('C to Cancel>>>')
            while True:
                if tcon == '1':
                    print('CONTROLS')
                    print ("A: Hunt","C: Chop Trees","M: Mine","B: Open Bazaar","S: Show Stats","I: Inventory","X: Exit","T: Show Tutorial","H: Save the Game", sep='\n')
                    break
                if tcon == '2':
                    print('GUIDE')
                    print('You can earn cash by hunting, mining, and chopping woods!','You can do it by buying matching weapons or tools','You can buy them at bazaar.', 'Hunting: Swords', 'Mining: Pickaexes', 'Chopping woods: Axes', 'If your are newbie I recommend you to try hunting', 'You can grow you stats by eating foods(Carrot: 0.1 or bread: 0.2)','You can get seed by eating carrots','You can farm them',sep='\n')
                    break
                if tcon == 'c':
                    print('You closed the tutorial book from this realm.')
                    break


        

        if control == "a":
            animal = randint(1, 2)
            if Weapon == "nothing":
                print("You have no Weapon, go to bazaar and buy some")
            elif Weapon != "nothing":
                if animal == 1:
                    print("You found a Pig!")
                    OpponentHealth = 100
                    print("1. Attack  2. Run away")
                    while True:
                        acon = input (">>> ")
                        if acon == "1":
                            if Weapon == "Wood Sword":
                                Damage = randint(10, 15)
                                OpponentHealth = OpponentHealth - math.floor(math.floor(Damage*strength))
                                print("Now Pig's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your pig!")
                                    cash = cash + 150
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(0.6)
                                    continue
                            if Weapon == "Stone Sword":
                                Damage = randint(15, 20)
                                OpponentHealth = OpponentHealth - math.floor(math.floor(Damage*strength))
                                print("Now Pig's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your pig!")
                                    cash = cash + 150
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(0.6)
                                    continue
                            if Weapon == "Iron Sword":
                                Damage = randint(20, 25)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Pig's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your pig!")
                                    cash = cash + 150
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(0.6)
                                    continue
                            if Weapon == "Gold Sword":
                                Damage = randint(25, 30)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Pig's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your pig!")
                                    cash = cash + 150
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(0.6)
                                    continue
                            if Weapon == "Diamond Sword":
                                Damage = randint(30, 35)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Pig's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your pig!")
                                    cash = cash + 150
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(0.6)
                                    continue
                    
                        else:
                            break
                        
                if animal == 2:
                    print("You found a Cow!")
                    OpponentHealth = 200
                    print("1. Attack  2. Run away")
                    while OpponentHealth >= 0:
                        acon = input (">>> ")
                        if acon == "1":
                            if Weapon == "Wood Sword":
                                Damage = randint(10, 15)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Cow's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your pig!")
                                    cash = cash + 400
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(1)
                                    continue
                            if Weapon == "Stone Sword":
                                Damage = randint(15, 20)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Cow's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your cow!")
                                    cash = cash + 400
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(1)
                                    continue
                            if Weapon == "Iron Sword":
                                Damage = randint(20, 25)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Cow's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your cow!")
                                    cash = cash + 400
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(1)
                                    continue
                            if Weapon == "Gold Sword":
                                Damage = randint(25, 30)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Cow's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your cow!")
                                    cash = cash + 400
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(1)
                                    continue
                            if Weapon == "Diamond Sword":
                                Damage = randint(30, 35)
                                OpponentHealth = OpponentHealth - math.floor(Damage*strength)
                                print("Now Cow's health is ",OpponentHealth,"!")
                                if OpponentHealth <= 0:
                                    print("You have hunt your cow!")
                                    cash = cash + 400
                                    print("Your cash:",cash)
                                    break
                                else:
                                    time.sleep(1)
                                    continue
                        else:
                            print("You succesfully ran away from",animal,"!")
                            break
        
        
        
        
        
        if control == "f":
            print("Do you want to plant your carrot?")
            print("You need to wait [1 min] to grow you carrot")
            fanswer = input("Yes or NO \n>>>")
            if fanswer == "yes":
                if Hoe == "nothing":
                    print("You don't have a hoe, go to the bazaar and buy one")
                if Hoe == "Wood Hoe":
                    if seed >= 5:
                        seed = seed - 5
                        Seedstr = 'Seeds:'+str(seed)
                        print("You planted 10 carrots")
                        time.sleep(60)
                        print("You harvest 10 carrots!")
                        carrot = carrot + 10
                        Carrotstr = 'Carrots:'+str(carrot)
                    else:
                        print('You do not have enough seeds to farm')
                        print('You need 5 seeds to farm')
                        print(Seedstr)

                if Hoe == "Stone Hoe":
                    if seed >= 5:
                        seed = seed - 5
                        Seedstr = 'Seeds:'+str(seed)
                        print("You planted 15 carrots")
                        time.sleep(60)
                        print("You harvest 15 carrots!")
                        carrot = carrot + 15
                        Carrotstr = 'Carrots:'+str(carrot)
                    else:
                        print('You do not have enough seeds to farm')
                        print('You need 5 seeds to farm')
                        print(Seedstr)
                if Hoe == "Iron Hoe":
                    if seed >= 5:
                        seed = seed - 5
                        Seedstr = 'Seeds:'+str(seed)
                        print("You planted 20 carrots")
                        time.sleep(60)
                        print("You harvest 20 carrots!")
                        carrot = carrot + 20
                        Carrotstr = 'Carrots:'+str(carrot)
                    else:
                        print('You do not have enough seeds to farm')
                        print('You need 5 seeds to farm')
                        print(Seedstr)

                if Hoe == "Diamond Hoe":
                    if seed >= 5:
                        seed = seed - 5
                        Seedstr = 'Seeds:'+str(seed)
                        print("You planted 25 carrots")
                        time.sleep(60)
                        print("You harvest 25 carrots!")
                        carrot = carrot + 25
                        Carrotstr = 'Carrots:'+str(carrot)
                    else:
                        print('You do not have enough seeds to farm')
                        print('You need 5 seeds to farm')
                        print(Seedstr)

            else:
                print("Canceled")
        
        if control == "h":
            dictionary ={
                "User": User,
                "invt" : invt,
                "bread" : bread,
                "carrot" : carrot,
                "Carrotstr" : Carrotstr,
                "Breadstr" : Breadstr,
                "Seedstr" : Seedstr,
                "invf" : invf,
                "invw" : invw,
                "Pickaxe" : Pickaxe,
                "Axe" : Axe,
                "Hoe" : Hoe,
                "Weapon" : Weapon,
                "strength" : strength,
                "Userhealth" : UserHealth,
                "cash" : cash
            }
            with open('data.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)    
            print("Data saved.")
            print("Time has stopped.")
            break    

if answer == "no":
    print ("No? Ok then..")
    time.sleep(0.5)
    print ("Maybe you'll want to come to the realm next time.")
    print ("Then goodbye for now.")