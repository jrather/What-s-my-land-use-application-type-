def input_repl(text = ''):
  print(text, end = '')
  return input()

print("Welcome! Please answer the questions below to determine what type of project you have.")
sf_of_development = int(input("How many square feet of new floor area will your project include? "))
if sf_of_development > 500 and sf_of_development < 10000:
  print ("OK - lets check a few more things.")
elif sf_of_development < 500:
  print("Too small for Planning review - straight to Permitting.")
elif sf_of_development > 10000:
  print("Major Site Plan review is required.")
land_disturbance = int(input("How many square feet of land area will be stripped, graded, grubbed,\n filled, or excavated to facilitate this project? "))