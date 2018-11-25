#!/usr/bin/python3.6 
#Auteur : Clélia BURLE 
#Khôlle 



#IMPORT
import  argparse 
import csv 

#VARIABLES 
li = []
minNbr, maxNbr = [],[]

#ARGUMENTS
parser = argparse.ArgumentParser() 
parser.add_argument("-l", action="store_true", help="Affiche le contenu de la liste")
parser.add_argument("-a", type=int, nargs='+', help="Ajoute les items dans la liste") 
parser.add_argument("-c", action="store_true", help="Supprime tous les éléments de la liste")
parser.add_argument("-s", "--max", action="store_true", help="Affiche la valeur maximum contenu dans la liste") 

args = parser.parse_args()
 

#FUNCTIONS 


#CODE

if args.l: 
   
    with open('list.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader: 
            print(line) 

elif args.a: 

    with open('list.csv', 'w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",") 
        csv_writer.writerow(args.a)

elif args.c: 
    
    with open('list.csv', 'r') as csv_file: 
        csv_reader = csv.reader(csv_file) 
        
        csv_file.close() 
        
elif args.max: 

    with open('list.csv', 'rt') as csv_file: 
        csv_reader = csv.reader(csv_file) 

        for line in csv_reader: 
            maxNbr.append('list.csv') 

        print("max value is : ", max(maxNbr)) 




 
