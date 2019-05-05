# se selecteaza un cuvant random dintr-o lista
# de 400 de cuvinte
import random

def rand_word_gen(lang):
    myline = 0
    myline2 = 0
    #myline1 = cuvant1
    #myline2 = cuvant2
    if lang=="1":
        file1=open("wordsENG.txt","r")
        file2=open("wordsENG2.txt","r")
    elif lang=="2":
        file1=open("wordsRO.txt","r")
        file2=open("wordsRO2.txt","r")
    lines = file1.read().splitlines()
    myline =random.choice(lines)

    lines2 = file2.read().splitlines()

    if rand_num_gen()%2 == 0:
        myline = myline.upper()

    if rand_num_gen()%3 == 0:
        myline2 = myline + random.choice(lines2)
    elif rand_num_gen()%3 == 2:
        myline2 = myline
    else:
        myline2 = random.choice(lines2) + myline
    return myline2

def rand_symb_gen():
	lines = open('symbols.txt').read().splitlines()
	myline = random.choice(lines)
	return str(myline)

# se genereaza un numar random de maxim 4 cifre
def rand_num_gen():
	return random.randint(1,1000)

###########################
def gen_word_and_number(lang):
	rw=str(rand_word_gen(lang))
	rn=str(rand_num_gen())
	return rw,rn

# functii principale #######################################
def easy_pass_gen(lang):
	randomWord, randomNumber = gen_word_and_number(lang)
	if rand_num_gen()%2 == 0:
		easypass = randomWord + str(randomNumber)
	else:
		easypass = str(randomNumber) + randomWord
	return easypass

def strong_pass_gen(lang):
    temppass = rand_symb_gen()
    for i in range(rand_num_gen()%4):
        symbol = rand_symb_gen()
        temppass = temppass + symbol

    epg=easy_pass_gen(lang)
    #print(epg)
    #de aici rezulta ca problema de acum e cu easy_pass_gen, nu returneaza un cuvant for some reason
    #problema e rezolvata (?), acum mai e doar problema ca uneori se genereaza doar numere random, inca nu stiu unde. somn usor
    l = list(temppass)
    random.shuffle(l)
    temppass = ''.join(l)

    l = list(epg)
    random.shuffle(l)
    if rand_num_gen()%2 == 0:
        temppass =  temppass + ''.join(l)
    else:
        temppass = ''.join(l) + temppass
    return temppass
############################################################



def passcheck(passd):
    if len(passd)>4 and len(passd)<20:
        return 1
    else: return 0

def genpass(answer,lang):
    while True:
        if answer == "1":
            passd=easy_pass_gen(lang)
        else:
            passd=strong_pass_gen(lang)
        return passd
        if passcheck(passd)==1:
            return passd
        else:
            print("problema cu recursion!")
            genpass(answer,lang)

#def main():
#    file = open("wordsENG2.txt", "r")
#    file5 = open("parole.txt", "a")
#    file5.write(easy_pass_gen(file,2))
#    file5.write("\n")

#if __name__== "__main__":
#   i=501
#   while i>0:
#        main()
#        i-=1

def main():
    lang = input("EN/RO?")
    answer = input("Do you want a weak or strong password ? (1=weak, 2=strong) : ")
    print(genpass(answer,lang))


if __name__== "__main__":
    main()
