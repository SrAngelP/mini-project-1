import random
import pandas as pd
from PIL import Image
class Bulbasaur(object):
    
    #https://pokemondb.net/pokedex/bulbasaur
    
    def __init__(self):
        
        #rand= random.random();
        
        self.name = 'Bulbasaur';
        self.hp = random.randrange(200, 295, 1) ;
        self.attack = random.randrange(92, 217, 1);
        self.defense =  random.randrange(92, 217, 1);
        self.sp_attack = random.randrange(121, 252, 1);
        self.sp_defense = random.randrange(121, 252, 1);
        self.speed = random.randrange(85, 208, 1);
        self.image = Image.open("bulbasaur.jpg");
        
    def cambiar_nombre(self, nombre):
        self.name =  nombre;
        return;
        

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            resultado = (f"¡{self.name} fue vencido!");
        elif self.hp > 0:
            resultado = (f"¡{self.name} ha recibido {damage} de daño pero sigue en pie!");
        return resultado;
    
    
    def corte(self):
        general_attack = self.attack;
        power = 50;
        return general_attack, power;
    
    
    def hoja_navaja(self):
        general_attack = self.sp_attack;
        power = 55;
        return general_attack, power;
    
    
    def elegir_ataque(self, cpu=False):
        
        if cpu == False:
            
            elec1 = input('Elige un ataque: Presiona 1 para corte. Presiona 2 para hojas navaja ');
            if elec1 =='1':
                return self.corte(), int(elec1);
            elif elec1=='2':
                return self.hoja_navaja(), int(elec1);
            else:
                print('Opción equivocada');
                return self.elegir_ataque(); #Preguntar qué onda al maestro, ¿por qué al ponerlo en el return sí se hace el bucle y porque si sólo lo llamo no se hace?
        
        elif cpu == True:
            lista_ataques = [self.corte(), self.hoja_navaja()]
            elec3 = random.randrange(1,3)
            
            return lista_ataques[(elec3 - 1)], elec3;


    

class Charmander(object):
    
    
    #https://pokemondb.net/pokedex/charmander
    
    def __init__(self):
        
        
        self.name = 'Charmander';
        self.hp = random.randrange(188, 283, 1) ;
        self.attack = random.randrange(98, 224, 1);
        self.defense =  random.randrange(81, 204, 1);
        self.sp_attack = random.randrange(112, 242, 1);
        self.sp_defense = random.randrange(94, 219, 1);
        self.speed = random.randrange(121, 252, 1);
        self.image = Image.open("charmander.jpg");


    def cambiar_nombre(self, nombre):
        self.name =  nombre;
        return;

    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            resultado = (f"¡{self.name} fue vencido!");
        elif self.hp > 0:
            resultado = (f"¡{self.name} ha recibido {damage} de daño pero sigue en pie!");
        return resultado;
    
    
    def cuchillada(self):
        general_attack = self.attack;
        power = 70;
        return general_attack, power;
    
    
    def ascuas(self):
        general_attack = self.sp_attack;
        power = 40;
        return general_attack, power;
    
    
    def elegir_ataque(self, cpu = False):
        
        if cpu == False:
            
            elec2 = input('Elige un ataque: Presiona 1 para cuchillada. Presiona 2 para ascuas ');
            if elec2 =='1':
                return self.cuchillada(), int(elec2);
            elif elec2=='2':
                return self.ascuas(), int(elec2);
            else:
                print('Opción equivocada');
                return self.elegir_ataque();

        elif cpu == True:
            lista_ataques = [self.cuchillada(), self.ascuas()]
            elec3 = random.randrange(1,3)
            
            return lista_ataques[(elec3 - 1)], elec3;   


                
        
class Squirtle(object):
    
    #https://pokemondb.net/pokedex/squirtle
    
    def __init__(self):
        

        self.name = 'Squirtle';
        self.hp = random.randrange(198, 293, 1) ;
        self.attack = random.randrange(90, 215, 1);
        self.defense =  random.randrange(121, 252, 1);
        self.sp_attack = random.randrange(94, 219, 1);
        self.sp_defense = random.randrange(119, 250, 1);
        self.speed = random.randrange(81, 204, 1);
        self.image = Image.open("squirtle.jpg");
        
    def cambiar_nombre(self, nombre):
        self.name =  nombre;
        return;
        
    def receive_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            resultado = (f"¡{self.name} fue vencido!");
        elif self.hp > 0:
            resultado = (f"¡{self.name} ha recibido {damage} de daño pero sigue en pie!");
        return resultado;
    
    def mordida(self):
        general_attack = self.attack;
        power = 60;
        return general_attack, power;
    
    def pistola_agua(self):
        general_attack = self.sp_attack;
        power = 40;
        return general_attack, power;
    
    
    def elegir_ataque(self, cpu = False):
        
        if cpu == False:
            
            elec3 = input('Elige un ataque: Presiona 1 para mordida. Presiona 2 para pistola de agua ');
            if elec3 =='1':
                return self.mordida(), int(elec3);
            elif elec3=='2':
                return self.pistola_agua(), int(elec3);
            else:
                print('Opción equivocada');
                return self.elegir_ataque();
        
        elif cpu == True:
            lista_ataques = [self.mordida(), self.pistola_agua()]
            elec3 = random.randrange(1,3)
            
            return lista_ataques[(elec3 - 1)], elec3;





def select_pk():
    pokemon_list = [Bulbasaur(), Charmander(), Squirtle()];
    choice = random.choice(pokemon_list);
    return choice;        
        
                

def select_pokemon():
    
    poke = select_pk();
    
    print(f"¡Es un {poke.name}!");
    print('')
    name = input('¡Ponle un nombre! ');
    poke.cambiar_nombre(name);
    
    datos = [poke.name, poke.attack, poke.defense, poke.sp_attack, poke.sp_defense, poke.speed];
    name_datos = ['Nombre', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad'];
    
    
    display(poke.image.resize((200,200)))
    print(pd.DataFrame(datos, index = name_datos, columns = ['Datos']));
    
    
    return poke;
  


def damage(ataque_pokemon1, power, defensa_pokemon2):
    
    a_d =ataque_pokemon1/defensa_pokemon2;
    
    
    damage_pk = round(0.84*power*a_d)+2;
        
    
    return damage_pk;



def batalla_pokemon_prueba(poke1, poke2 = select_pk(), cpu = False):
    return poke1, poke2;

    

def batalla_pokemon(poke1, se_inv, poke2 = select_pk(), first_time=True, cpu = False):
    


    if first_time == True:
        
        #Evaluación de quién va primero
        
        if poke1.speed >= poke2.speed:
            print(f"{poke1.name} es más rápido. Ataca primero");
            pokemon1 = poke1;
            pokemon2 = poke2;
            se_inv = False;
        
        elif poke1.speed < poke2.speed:
            print(f"{poke2.name} es más rápido. Ataca primero");
            pokemon1 = poke2;
            pokemon2 = poke1;
            se_inv = True;
        
        ### Evaluación de si luchas contra la compu    
        if cpu == True:
            
            if poke1.speed >= poke2.speed:
                cpu3 = True;
                cpu1 = False;
                cpu2 = True;
    
            elif poke1.speed < poke2.speed:
                cpu3 = True;
                cpu1 = True;
                cpu2 = False;
                
        elif cpu == False:
            cpu3 = False;
            cpu1 = False;
            cpu2 = False;
            
            
    elif first_time == False:
        
        pokemon1 = poke1;
        pokemon2 = poke2;
        
        if cpu == True:
            if se_inv == False:
                cpu3 = True;
                cpu1 = False;
                cpu2 = True;
                
            elif se_inv == True:
                cpu3 = True;
                cpu1 = True;
                cpu2 = False;
                
        elif cpu == False:                
            cpu3 = False;
            cpu1 = False;
            cpu2 = False;

        
    
        
        ### Evaluación de si luchas contra la compu:
        

            
            

            
        
            
        
    
        
    

        
        
        

    
    
    
    damage1 = ataque_pk(pokemon1, pokemon2, cpu1);
    
    print('');
    print(F"¡{pokemon1.name} ataca!");
    print('');
    print(pokemon2.receive_damage(damage1));
    print('');
    print(f"{pokemon2.name} tiene {pokemon2.hp} puntos de vida");
    print('');
    print('');
    
    if pokemon2.hp<=0:
        print(f"¡{pokemon1.name} ha ganado la batalla!")
        return pokemon1.hp;
    
    elif pokemon2.hp>0:
                

        damage2 = ataque_pk(pokemon2, pokemon1, cpu2);
        
        print('');
        print(F"¡{pokemon2.name} ataca!");
        print('');
        print(pokemon1.receive_damage(damage2));
        print('');
        print(f"{pokemon1.name} tiene {pokemon1.hp} puntos de vida");
        print('');
        print('');
        
        if pokemon1.hp<=0:
            print(f"¡{pokemon2.name} ha ganado la batalla!");
            return pokemon2.hp;
        
        elif pokemon1.hp>0 and pokemon2.hp>0:
            print('¡La lucha sigue, siguiente ataque!');
            return batalla_pokemon(pokemon1, se_inv, pokemon2, first_time = False, cpu = cpu3);    
    


def ataque_pk(pokemon1, pokemon2, cpu_a):
    
    ataque_pk1 = pokemon1.elegir_ataque(cpu = cpu_a);
    if ataque_pk1[1] == 1:
        defe_2 = pokemon2.defense;
        #print(f"defensa = {pokemon2.defense}");
    elif ataque_pk1[1] == 2:
        defe_2 = pokemon2.sp_defense;
        #print(f"defensa especial = {pokemon2.sp_defense}");
    
    damage1 = damage(ataque_pk1[0][0], ataque_pk1[0][1], defe_2);
    
    return damage1;

    
    
def user_or_pc():
    u_o_p = input('¿Cuantós jugadores serán? ¿1 o 2?: ')
    
    
    if u_o_p =='1':
        return u_o_p;
    elif u_o_p =='2':
        return u_o_p;
    else:
        print('Opción equivocada');
        return user_or_pc();
    
    
    
def juego():
    
    u_o_p = user_or_pc();
    
    if u_o_p =='1':
        
        
        print('Tu pokemon: ')
        pk1 = select_pokemon();
        print('');
        print('');
        print('¡Ahora, a pelear!');
        
        batalla_pokemon(pk1, False, cpu = True);
        
        
        
        
        
    
    elif u_o_p == '2':
        
        print('El primer pokemon: ')
        pk1 = select_pokemon();
        
        print('')
        print('El segundo pokemon: ')
        pk2 = select_pokemon();
        
        batalla_pokemon(pk1, False, pk2);
    
    
        
        
        
        
        
        
    return;
    
    
    
