import random
print('Welcome to Alien NPC Generator')
print('\n')
name = ''
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
vowels = ['a','e','i','o','u','y']
consonants = ['b','c', 'd','f','g','h','j','k','l','m','n','p', 'q', 'r', 's', 't','v', 'w','x','z']
first_letter = input('Enter the first letter of the names of your aliens here (Leave blank for a random starting letter): ')
last_letter = input('Enter the last letter of the names of your aliens here: ')
min_age = input('Enter a minimum age in years here (leave blank for a random minimum age): ')
max_age = input('Enter a maximum age in years here (leave blank for a random maximum age): ')
age = 0
min_stamina = input('Enter a minimum stamina level here (leave blank for a random minimum stamina level): ')
max_stamina = input('Enter a maximum stamina level here (leave blank for a random maximum stamina level): ')
stamina = 0
min_health = input('Enter a minimum health here (leave blank for a random minimum health): ')
max_health = input('Enter a maximum health here (leave blank for a random maximum health): ')
health = 0
min_power = input('Enter a minimum power level here (leave blank for a random minimum power level): ')
max_power = input('Enter a maximum power level here (leave blank for a random maximum power level): ')
power = 0

for i in range(1,11):
    # This is the code for the name
    name = ''
    if first_letter is not ' ' and last_letter is not ' ':
        name += first_letter
        for i in range(1,11):
            name += random.choice(vowels)
            name += random.choice(consonants)
        name += last_letter
            
    elif first_letter is not ' ' and last_letter is ' ':
        name += first_letter
        for i in range(1,11):
            name += random.choice(vowels)
            name += random.choice(consonants)
        name += random.choice(alphabet)
    
    elif first_letter is ' ' and last_letter is not ' ':
        name += random.choice(alphabet)
        for i in range(1,11):
            name += random.choice(vowels)
            name += random.choice(consonants)
        name += last_letter
        
    else:
        for i in range(1,12):
            random.choice(vowels)
            random.choice(consonants)
    print(f'Name: {name.capitalize()}')
    # This is the code for the age
    
    if min_age is not '' and max_age is not '':
        min_age = float(min_age)
        max_age = float(max_age)
        if min_age <= max_age:
            age = random.uniform(min_age,max_age)
        else:
            print('Invalid age range. Setting age to random value.')
            age = random.random()
    elif min_age is not '' and max_age is '':
        min_age = float(min_age)
        age = random.uniform(min_age, )
    elif min_age is '' and max_age is not '':
        max_age = float(max_age)
        age = random.uniform(0,max_age)
    else:
        age = random.random()
    print(f'Age (years): {age}')
    
    # This is the code for the stamina
    
    if min_stamina is not '' and max_stamina is not '':
        min_stamina = int(min_stamina)
        max_stamina = int(max_stamina)
        if min_stamina <= max_stamina:
            stamina = random.randint(min_stamina,max_stamina)
        else:
            print('Invalid stamina level range. Setting stamina level to random value.')
            stamina = random.randint()
    elif min_stamina is not '' and max_stamina is '':
        min_stamina = int(min_stamina)
        stamina = random.randint(min_stamina, )
    elif min_stamina is '' and max_stamina is not '':
        max_stamina = int(max_stamina)
        stamina = random.randint(0,max_stamina)
    else:
        stamina = random.randint(1,10000000001)
    print(f'Stamina Level: {stamina}')
    
    #This is the code for the health
    if min_health is not '' and max_health is not '':
        min_health = int(min_health)
        max_health = int(max_health)
        if min_health <= max_health:
            health = random.randint(min_health,max_health)
        else:
            print('Invalid health range. Setting health to random value.')
            health = random.randint()
    elif min_health is not '' and max_health is '':
        min_health = int(min_health)
        health = random.randint(min_health, )
    elif max_health is '' and max_health is not '':
        max_health = int(max_health)
        health = random.randint(0,max_health)
    else:
        health = random.randint(1,10000000001)
    print(f'Health: {health}')
    
        #This is the code for the power
    if min_power is not '' and max_power is not '':
        min_power = int(min_power)
        max_power = int(max_power)
        if min_power <= max_power:
            power = random.randint(min_power,max_power)
        else:
            print('Invalid power level range. Setting power level to random value.')
            power = random.randint()
    elif min_power is not '' and power is '':
        min_power = int(min_power)
        power = random.randint(min_power, )
    elif max_power is '' and max_power is not '':
        max_power = int(max_power)
        power = random.randint(0,max_power)
    else:
        power = random.randint(1,10000000001)
    print(f'Power: {power}')
    print('\n')
    
