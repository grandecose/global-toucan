on = 1;
a = -9.800000000000
print("Welcome to the physics calculator\n");
valid = "Please choose a valid option\n";
while(on == 1):
	a = -9.800000000000000000000000
	choice = int(input("What equation would like to find?\n1. Final Velocity\n2. Distance\n3. Time\n4. Help\n5. Quit\n"))
	if(choice == 1):
		z = int(input("What do you want to find?\n1. Final Velocity\n2. Initial Velocity\n3. Acceleration\n4. Time\n"));
		if(z == 1):
			vi = int(input("What is the initial velocity?\n"))
			
			time = int(input("What is the time?\n"))

			vf = vi + (a * time)

			print("Your final velocity is: ")

			print vf

		elif(z == 2):
			vf = int(input("What is the final velocity (m/s)?"))
			
			time = int(input("For how long is the object travelling (seconds)?"))

			vi = vf - (a * time)
			
			print("The initial velocity is: ")

			print vi			
		elif(z == 3):
			vf = int(input("What is the final velocity?\n"))
			
			vi = int(input("What is your initial velocity?\n"))

			time = int(input("What is the time?\n"))	
			
			a = 1.000000000000000 * ((vf - vi) / time)

			print("The acceleration is: ");
			
			print a
		elif(z == 4):
			print valid
		else:
			print valid

	elif(choice == 2):
		print valid
	elif(choice == 3):
		print valid

	elif(choice == 4):
		print("Physics calculator is a simple program written in python in order to physics problems.\n The calculator will only take numbers, so please no units.\n Everything will be done in seconds for time, m/s for velocity, and m/s/s for acceleration.\n");
		raw_input("Press enter to return to the main page.\n");
	elif(choice == 5):
		jdfhks = raw_input("Physics Calculator will now exit, please press enter.")
		on = 0;

	else:
		print valid
