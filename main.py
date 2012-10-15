on = 1;
a = -9.800000000000
print("Welcome to Global Toucan, a physics calculator.\n");
valid = "Please choose a valid option\n";
#I've never been good at commenting, if you can't understand whats going on contact me and I will help.
while(on == 1):
	a = -9.800000000000000000000000
	choice = raw_input("What equation would like to use?\n1. Final Velocity\n2. Distance\n3. Help\n4. List Equations\n5. Quit\n")
	if(choice == "1"):
		z = raw_input("What do you want to find?\n1. Final Velocity\n2. Initial Velocity\n3. Acceleration\n4. Time\n");
		if(z == "1"):
			vi = int(input("What is the initial velocity?\n"));
			
			time = int(input("What is the time?\n"));

			vf = (vi * 1.000000000000000000000000000000000) + (a * time)

			print("Your final velocity is %s m/s" % vf);

		elif(z == "2"):
			vf = int(input("What is the final velocity?\n"));
			
			time = int(input("For how long is the object travelling?\n"));

			vi = (vf * 1.00000000000000000000000000) - (a * time)
			
			print("The initial velocity is %s m/s" % vi);
		
		elif(z == "3"):
			vf = int(input("What is the final velocity?\n"));
			
			vi = int(input("What is your initial velocity?\n"));

			time = int(input("What is the time?\n"));
			
			a = ((vf * 1.00000000000000000000 - vi) / time)

			print("The acceleration is %s m/s/s" % a);
		elif(z == "4"):
			vf = int(input("What is the final velocity?\n"));
			
			vi = int(input("What is the initial velocity?\n"));

			time = (vf - vi) / (a * 1.0000000000000000000000000)
 		
			print("The time is %s seconds" % time);	
		else:
			print valid

	elif(choice == "2"):
		choice = raw_input("What do you want to find?\n1. Distance\n2. Initial Velocity\n3. Acceleration\n4. Time\n");
		# d = vi * t + (.5 * a * (t ** 2)) 
		if(choice == "1"):
			vi = int(input("What is your initial velocity?\n"))
			
			t = int(input("What is the time?\n"))
			
			d = vi * 1.00000000000000000 * t + (.5 * a * (t ** 2))

			print("This object has travelled %s meters" % d);

		elif(choice == "2"):
			d = int(input("What is the distance (please remember to include a - sign if movement is negative)?\n"))
			
	
			t = int(input("What is the time?\n"))
			
			vi = (d * 1.000000000000000000 - (.5 * a * (t ** 2))) / t	
			
			print("The final velocity is %s m/s" % vi);			

		elif(choice == "3"):
			d = int(input("What is the distance (please remember to include a - sign if movement is negative)?\n"))
			
			vi = int(input("What is the initial velocity?\n"))			
				
			t = int(input("What is the time?\n"))

			a = (d * 1.000000000000000000000000 - (vi * t)) / (.5 * (t ** 2))

			print("The acceleration is %s m/s/s" % a);
		elif(choice == "4"):
			d = int(input("What is the distance (please remember to include a - sign if movement is negative)?\n"))
			
			vi = int(input("What is the initial velocity?\n"))

			vf = int(input("What is the final velocity?\n"))
			# currently using the distance formula python won't figure it out. I'll have to put in a function later. In the 
  			# meantime use vf and vi. vf = vi + at 
			t = (vf * 1.000000000000000 - vi) / a
			
			print("The time is %s seconds" % t);
			
		else:
			print valid

	elif(choice == "3"):
		print("Global Toucan is a simple program written in python made to solve physics problems concerning motion.\n The calculator will only take numbers, so please no units.\nWhen calculating for directions going down please remember to include '-'. For example if your calculation involves an apple falling 50 meters one would input -50 as the distance.\nEverything will be done in seconds for time, m/s for velocity, and m/s/s for acceleration.\nAs such, please do any conversions beforehand.\nGlobal Toucan is licensed under the GPLv3 a Free Software License.\n");
		raw_input("Press enter to return to the main menu.\n");
	
	elif(choice == "4"):
		print("The following are the equations used by this program:\nFinal Velocity: vf = vi + at, where vf is final velocity, a is acceleration and t is time.\nDistance: d = vi * t + .5 a * (t ^ 2), where d is distance, vi is initial velocity, t is time, a is acceleration, and t is time.\n");
		raw_input("Press enter when you are ready to return to the main menu.\n");
		
	elif(choice == "5"):
		raw_input("Global Toucan will now exit, please press enter.")
		on = 0;

	else:
		print valid
