"""
CSE 111
Author: Tim Illguth
Instructor: Christian Eisingers
Filename: Prep_07.py
"""

def modify_args(n, alist):
    """Demonstrate that the computer passes a value
    for integers and passes a reference for lists.
    Parameters
        n: A number
        alist: A list
    Return: nothing
    """
    print("    modify_args(n, alist)")
    print(f"        Before changing n and alist: n {n}  alist {alist}")

    # Change the values of both parameters.
    n += 1  # Increment the value of n by 1
    alist.append(4)  # Append the number 4 to the list alist

    print(f"        After changing n and alist:  n {n}  alist {alist}")

def main():
    print("main()")
    x = 5  # Assign a number to variable x
    lx = [7, -2]  # Assign a list to variable lx
    print(f"    Before calling modify_args(): x {x}  lx {lx}")

    # Pass one integer and one list
    # to the modify_args function.
    modify_args(x, lx)

    print(f"    After calling modify_args():  x {x}  lx {lx}")

# Call the main function
if __name__ == "__main__":
    main()
