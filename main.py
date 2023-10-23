################### Scope ####################
enemies = 1
def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


#Local Scope
def drink_portion():
    portion_strength = 2
    print(portion_strength)

drink_portion
#print(portion_stregnth) 
#This will throw an error since you are trying to access it outside the function.


#Global Scope
player_health = 10 
def drink_portion():
    portion_strength = 2
    print(player_health) 
#player_health has global scope since it was defined at the top level (no indentation)


#There is no block scope in python
if 3 >2:
    a_variable = 10 

print(a_variable) #This will print it properly - if statements have no fence even though it is indented. 


game_level = 3
enemies = ['skeleton', 'zombie', 'alien']
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)


#Modifying a global scope
enemies = 2

def increase_enemies():
    global enemies   #there is a global scope somewhere in the code 
    enemies += 1
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

#Alternative to modifying global scope 
def increase_enemies(): 
    print(f"enemies inside function: {enemies}")
    return enemies +1 
# Use return statements to edit global variables and change it outude the indentation

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")


#Global Constants > variables you never want to change 
PI = 3.14159

def pi_value():
    PI  #As a rule, use UPPER CASE for global constants, so you know never to modify them

