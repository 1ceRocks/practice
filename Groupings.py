import random

def select_random_names(BSCOE_2_6):
    n = int(input("Enter the desired number of group members: "))
    random.shuffle(BSCOE_2_6)
    grouped = []
    for i in range(0, len(BSCOE_2_6), n):
        grouped.append(BSCOE_2_6[i:i + n])
    print(grouped)



BSCOE_2_6 = ["Azarcon",							
"Baroto",							
"Bermundo",							
"Bugnon",						
"Cabanag",								
"Cando",									
"Chan",										
"Corpuz",									
"Daza",									
"De Vega",								
"Dela Rosa",								
"Domer",										
"Esguerra",								
"Estrella",						
"Floranda",							
"Ilagan",
"Javier",									
"Jubilo",									
"Lacson",																
"Lasco",																
"Lim",												
"Lopez",												
"Maglangit",												
"Mampusti",
"Merque",
"Nicanor",
"Ofiangga",
"Palahang",
"Pangaruy",	
"Piñero",
"Punzal",
"Ramirez",
"Relleve Jr.",	
"Robles",
"Rosales",
"Salazar",
"Santos",
"Susa",		
"Velasquez",
"Villariza",	
"Zoleta"]

select_random_names(BSCOE_2_6)
