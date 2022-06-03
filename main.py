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
  print("Major Site Plan review is required for this.")
land_disturbance = int(input("How many square feet of land area will be stripped, graded, grubbed,\n filled, or excavated to facilitate this project, in square feet? "))
if land_disturbance > 1000 or land_disturbance < 130680:
  print("Minor Site Plan review is required for this.")
elif land_disturbance > 1000:
  print("OK - let's check a few more things.")
elif land_disturbance > 130680:
  print("Major Site Plan review is required for this.")
change_of_use = int(input("Are you changing the use of your site? If so, how many square feet is this use?" ))
if change_of_use > 10000:
  print("This change of use can be reviewed by Permitting - Planning review is not required.")
elif change_of_use < 10000 and change_of_use > 20000:
  print("This change of use requires Minor Site Plan review.")
elif change_of_use > 20000:
  print("This change of use requires Major Site Plan review.")