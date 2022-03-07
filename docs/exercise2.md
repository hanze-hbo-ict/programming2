# Exercise 2: Classes and instances

## Introduction

Photosynthesis is the process by which plants and certain animals convert light energy into chemical energy that can be stored and used to drive the organism's activities. Though different varieties of photosynthesis exist, the overall equation for the type that occurs in plants is as follows:

$6CO_2 + 6H_2O -> C_6H_{12}O_6 + 6O_2 + energy$

## Assignment 1: the `Atom` class

- **1a.** Create a class `Atom` that is a representation of any atom in the periodic table. Make sure that when a concrete atom is instantiated, it is given its symbol and its atomic number and the normal (default) number of neutrons in the core. 

- **1b.** Create a method `proton_number` that returns the number of protons in the nucleus; make another method `mass_number` that returns the sum of protons and neutrons in the nucleus.

Isotopes are types of atoms that have the same number of atomic number but a different number of neutrons in the core. So, e.g. 'normal' hydrogen has 1 proton and 1 neutron, but also comes in the form of deuterium (1 proton and 2 neutrons) or even tritium (1 proton and 3 neutrons).

- **1c.** Create a method `isotope` in the class `Atom`. When this method is called, the normal number of neutrons must be replaced by whatever number is provided to this method.

- **1d.** We define an atom A to be *less* than another atom B if their proton number is the same (i.e. it is the same element) but the mass number of A is less than the mass number of B. Implement the methods that check whether two isotopes of the same atom are equal to each other, or less than or greater than each other. 

You can use the code below to test your implementation.

```python
protium = Atom('H', 1, 1)
deuterium = Atom('H', 1, 2)
tritium = Atom('H', 1, 2)
tritium.isotope(3)

assert tritium.neutrons == 3
assert tritium.mass_number() == 4
assert protium < deuterium
assert deuterium <= tritium
assert tritium >= protium
```

## Assignment 2: the `Molecule` class

A molecule is a neutral group of two or more atoms.

- **2a.** Create the class `Molecule`. When creating an instance of this class, a list of tuples or two elements (a *pair*) is given. The first element of this pair is the Atom, the second element is the number of atoms of that type that is put into the molecuel. Thus, the following code snippet creates a water-molecule:

```python
hydrogen = Atom('H', 1, 1)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
```

- **2b.** Make sure that when we print individual molecules, we get somehing resembling the correct chemical formula (you don't *have* to take the exact protocol into account. So, e.g. `print (water)` would render `H2O`. Make sure that the number 1 is omitted in the representation.

- **2c** In our small implementation, molecules that are created can never change (they are *immutable*). However, we can *add* two molecules together in order to create a new molecule. Implement this method in the class `Molecule`. Creating molecules this way is, of course, not really possible. However, because of educational reasons we pretend that this is an ok way to work.

You can use the code below to test your implementation:

```python
hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
print (water) # H2O
print (co2) # CO2
print (water + co2) # H2OCO2
```

## Assignment 3: The `Chloroplast` class

As a final assignment, we are going to make a (very, very) simplified version of the photosynthesis process; basically, we are only going to implement the formula stated above.

- **3a.** Create the class `Chloroplast`. When creating objects of this type, make sure four fields `water` and `co2` are initialised at value `0`.

- **3b.** Implement the following functionality: make a methode `add_molecule` in which we can add water or carbondioxyde molecules to objects of this class. When we add either of them, the corresponding field is incrementend by one. When we add something else than water of carbondioxyde, a `ValueError` is raised, but the program continues to function. If nothing else happens, this method returns an empty list

- **3c.** When we have added a total of 6 CO2-molecules and 12 H2O-molecules, we start of the photosyntheses. We decrease the fields `water` and `co2` with 6 and 12 respectively and create three new molecules: `C6H12O6`, `O2` and `H2O`. In this case, the method returns a list of tuples: 1 molecule of sugar, 6 molecules of oxygen and 6 molecules of water (as per the general formula stated above).

- **3d.** Make sure thwat when we print this instance of chloroplast, we get an idea of how many molecules of water and co2 are already stored in it.

You can use the following script to check your implementation

```python
water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
demo = Chloroplast()
els = [water, co2]

while (True):
    print ('\nWhat molecule would you like to add?')
    print ('[1] Water')
    print ('[2] carbondioxyde')
    print ('Please enter your choice: ', end='')
    try:
        choice = int(input())
        res = demo.add_molecule(els[choice-1])
        if (len(res)==0):
            print (demo)
        else:
            print ('\n=== Photosynthesis!')
            print (res)
            print (demo)

    except Exception:
        print ('\n=== That is not a valid choice.')
```

## Wrap up

Make sure your code follows the SOLID principles. Do you see any refactoring-possibilities? Did you use constants where possible? Have you identified all the stuff that stayed the same and seperated that from all the stuff that changed...?
