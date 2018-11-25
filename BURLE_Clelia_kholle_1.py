#!/usr/bin/python3.6 
#Auteur : Clélia BURLE 
#Khôlle 



#IMPORT
import  argparse 
import csv 

#VARIABLES 
li = []
mini=0
maxi=0
summ=0
#ARGUMENTS
parser = argparse.ArgumentParser() 
parser.add_argument("-l", action="store_true", help="Affiche le contenu de la liste")
parser.add_argument("-a", type=int, nargs='+', help="Ajoute les items dans la liste") 
parser.add_argument("-c", action="store_true", help="Supprime tous les éléments de la liste")
parser.add_argument("-max", action="store_true", help="Affiche la valeur maximum contenu dans la liste") 
parser.add_argument("-min", action="store_true", help="Affiche la valeur minimal contenu dans la liste") 
#parser.add_argument("-moy", action="store_true", help="Affiche la moyenne de tous les éléments dans la liste") 
parser.add_argument("-sum", action="store_true", help="Affiche la somme de tous les éléments dans la liste") 

args = parser.parse_args()
 

#FUNCTIONS 


#CODE

if args.l: 
   
    with open('list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader: 
            print(line) 

elif args.a: 

    with open('list.csv', 'a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",") 
        csv_writer.writerow(args.a)

elif args.c: 
    
    with open('list.csv', 'w') as csv_file: 
        csv_reader = csv.reader(csv_file) 
        
        csv_file.close() 
        
elif args.max: 

    with open('list.csv', 'rt') as csv_file: 
        csv_reader = csv.reader(csv_file) 

        for line in csv_reader: 
            maxi=max(line) 

        print("la valeur maximal est : ", maxi ) 

   
elif args.min: 

    with open('list.csv', 'rt') as csv_file: 
        csv_reader = csv.reader(csv_file) 

        for line in csv_reader: 
            mini=min(line) 

        print("la valeur minimal est : ", mini)
       
#elif args.moy


elif args.sum:

    with open ('list.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file) 

        for line in csv_reader: 
            summ=sum(line) 

        print("la somme est de : ", summ)  


