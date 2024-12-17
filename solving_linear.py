import numpy as np 



def creating_matrix(n):
    A = []  # Coefficient matrix
    B = []  # Constants vector

    print("\nEnter the coefficients for each equation:")
    for i in range(n): 
        while True:  # Ensures input validity
            try:
                row = list(map(float, input(f"Equation {i+1} coefficients (separated by spaces): ").split()))
                if len(row) != n:
                    raise ValueError(f"Each equation must have exactly {n} coefficients.")
                A.append(row)
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

    print("\nEnter the right-hand side values:")
    for i in range(n): 
        while True:
            try:
                b = float(input(f"Constant for equation {i+1}: "))
                B.append(b)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    A = np.array(A)  # Convert list of lists to a NumPy array
    B = np.array(B)  # Convert list to a NumPy array

    return A, B 




def solver(A , B ):
    try: 
        X=np.linalg.solve(A,B)
        print(" Solution")
        for i in range(n): 
            print(f"x{i+1}= {X[i]}")
    except np.linalg.LinAlgError:
        print('No unique solution')

n=int(input("Enter the number of variables: "))
a,b= creating_matrix(4)
solver(a,b)