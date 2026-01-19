"""This Program similarr with the reverse counting song "100 bottles of beer on the wall", you'll need to do a little research to familiarize yourself with it.

Ask the user how many bottles of beer are on the wall.
Pass that input to a function that manages the countdown.
The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
Once the count is down to 1, change lyrics to show "1 bottle of beer...".
At the end of the countdown, get back to the main program and remind the user to buy more beer.
"""
# Assigment Module 1.3
# Girma Dingeto

def countdown_bottles(count):
    # Manages the countdown logic for the song.

    while count>0:
        if count>1:
            # Display the count of bottles of beer on the wall
            print(f"{count} bottles of beer on the wall,{count} bottles of beer.")
            next_count =count-1
            suffix="bottle" if next_count==1 else "bottles"
            print(f"Take one down and pass it arround,{next_count} {suffix} of beer on the wall.\n")
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer.")
            print(f"Take one down and pass it arround, 0 bottles of beer on the wall.\n")
            print ("please buy more Bottles of beer.")

            
        count-=1
        
def main():
 

    print("_______________________________________________________________\n")
    # Main program entry point.
    try:

        #Ask the user for starting number
        start_num =int(input("How many bottles of beer are on the wall?"))

        if start_num <1:
            print("Please enter a number greater than 0.")
        
            
        else:
           # print("0 bottles of beer on the wall. Please buy more beer.")
            # Pass input to the count down function
            countdown_bottles(start_num)
            # Final reminder after retuning from the function
    except ValueError:
        print("Invalid input. Please enter a whole number.")
if __name__=="__main__":
    main()

 