<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

*Read this in other languages: [Spanish](README.sp.md).*

# Pokemon Battle Simulator!

## Content
- [Game Description](#Game-Description)
- [Game Mechanics](#Game-Mechanics)
- [Stats](#Stats)
- [Attacks](#Attacks)
- [Future Improvements](#Future-Improvements)
- [Links](#Links)

## Game Description

The game merges two mechanics. The classic battle rutine of the *gameboy*/*gameboy advance* versions and the randomness of the *gatcha* games. In summary, the user can choose between 1P mode or *PvP* mode. The battle starts and the winner is displayed in the screen.

## Game Mechanics

After the game starts the player choose the mode, then a pokemon of the game's pool (3 at this current version) with random stats will be given to the user, the stats of the pokemon are displayed so they can analize it. The pokemon with the higher speed is the one to attack first. For the battle the user can select one of the two attacks of each pokemon. Both players keep battling until one of the two pokemons' *HP* lowers to 0, the battle is over then.

### Stats

The pokemons' stats are based on the first generation and taken from the original source. **THE STATS ARE NOT THE ***BASE STATS*** ** but the ones of the range the pokemon can have in the level 100, so no pokemon is too powerfull.

### Attacks

The attacks were chosen so every pokemon has one *attack* and one *special attack*, the user would need to take into account the stats of *atk* and *sp. atk* to decide which attack to use; in accordance, the player will need to remember the defensive stats, to know which attack is more harmful for their pokemon.

The damage produced by each attack is calculated using a simplified first gen formula. The original ecuation is:

**Damage = ((((2 * Level / 5 + 2) * AttackStat * AttackPower / DefenseStat) / 50) + 2) * STAB * Weakness/Resistance * RandomNumber / 100**

In the ecuation the *boosters* of *type 1*, *type 2*, *STAB* and *random* are deprecated, and the level is assumed as 100 (the max level of the first gen), as mentioned earlier. The *A* and *D* are the attack and defense stats of each pokemon correspondingly, and the *power* refers to the attack's power individually.
 
## Future Improvements

In the programming process the problem of creating each pokemon (made with *python* objects) arised, but a method for sorting this problem using the existent databases was found in the meantime, its expected in the future to implement this update and have more pokemons and attacks to choose.
Similarly, there are plans to improve the *1P* mode difficulty by changing the CPU behavoiur at choosing the attacks, in this version attacks randomly.
Lastly, an upgrade in the user interface is needed, and maybe add more data for each pokemon.

## Links

https://pokemondb.net/

https://bulbapedia.bulbagarden.net/wiki/Damage
