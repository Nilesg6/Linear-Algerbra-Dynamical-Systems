import ast
import math
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt


print("\nPlease enter your preferred 2 by 2 matrix. Remember, this must be a real matrix, with complex eigenvalues a +/- ib.\nAlso, a + ib should have a corresponding eigenvector v + iw. Finally, remember that b cannot equal 0.\n")
print("When inputting data, input in this form: [x, y].\n")

our_row_1 = np.array(ast.literal_eval((input("What's in row 1? "))))
our_row_2 = np.array(ast.literal_eval((input("What's in row 2? "))))
our_matrix = np.matrix([our_row_1, our_row_2])

our_initial_vector = np.array(ast.literal_eval(input("What do you want the initial vector to be? ")))





def find_values_to_plot (matrix, initial_vector):


    print("\nSo your matrix is:\n{}\n".format(matrix))
    print("And your initial vector is:\n{}\n".format(initial_vector))


    eigenvalues, eigenvectors = LA.eig(matrix)
    print("Your eigenvalues are:\n{}\n".format(eigenvalues))
    print("Your eigenvectors are:\n{}\n".format(eigenvectors))

    input("Calculating...\n")


    r = math.sqrt(np.real(eigenvalues[0] * eigenvalues[1]))
    print("r is: {}\n".format(r))


    first_eigenvector = np.matrix(eigenvectors[:,0])
    if (np.imag(first_eigenvector[0,0]) < 0 or np.imag(first_eigenvector[1,0]) < 0):
        s_matrix = np.multiply(-1, np.matrix([[np.imag(first_eigenvector[0,0]), np.real(first_eigenvector[0,0])],[np.imag(first_eigenvector[1,0]), np.real(first_eigenvector[1,0])]]))
        s_matrix = remove_negative_zeros(s_matrix)
        print("Our S-matrix is:\n{}\n".format(s_matrix))
    else:
        s_matrix = np.matrix([[np.imag(first_eigenvector[0,0]), np.real(first_eigenvector[0,0])],[np.imag(first_eigenvector[1,0]), np.real(first_eigenvector[1,0])]])
        s_matrix = remove_negative_zeros(s_matrix)
        print("Our S-matrix is:\n{}\n".format(s_matrix))


    s_inverse_matrix = (s_matrix).I
    s_inverse_matrix = remove_negative_zeros(s_inverse_matrix)
    print("Our S-inverse matrix is:\n{}\n".format(s_inverse_matrix))


    theta = math.atan2(np.imag(eigenvalues[0]), np.real(eigenvalues[0]))
    print("The angle theta is: {}\n".format(theta))


    no_of_values = int(input("How many values of t do you want to calculate the system for? "))


    circle_x = np.zeros(no_of_values); circle_y = np.zeros(no_of_values); ellipse_x = np.zeros(no_of_values); ellipse_y = np.zeros(no_of_values); final_x = np.zeros(no_of_values); final_y = np.zeros(no_of_values)


    for t in range (no_of_values):


        theta_matrix = np.matrix([[math.cos(theta*(t)), -1*math.sin(theta*(t))], [math.sin(theta*(t)), math.cos(theta*(t))]])


        first = np.reshape(np.matmul(s_inverse_matrix, initial_vector), (2,1))
        second = np.reshape(np.matmul(theta_matrix, first), (2,1))
        circle_x[t] = second[0,0]
        circle_y[t] = second[1,0]


        third = np.reshape(np.matmul(s_matrix, second), (2,1))
        ellipse_x[t] = third[0,0]
        ellipse_y[t] = third[1,0]


        final = np.multiply(r**(t), third)
        final_x[t] = final[0,0]
        final_y[t] = final[1,0]


    input("\nValues have been calculated, ready to graph!\n")


    if (r >= 1):
        result = "the zero state is not asympotically stable"
    else:
        result = "the zero state is asymptotically stable"


    input("Based on our modulus of both of our eigenvalues, we can say that {} for this system.\n".format(result))


    return circle_x, circle_y, ellipse_x, ellipse_y, final_x, final_y





def make_subplots (circle1, circle2, ellipse1, ellipse2, final1, final2):


    size = int(input("What size window do you want? Enter \'n\' (n*n window). "))

    fig = plt.figure(figsize = (size,size))


    ax1 = fig.add_axes([.05, .55, .425, .425])
    ax1.set_title("Circle", fontsize='large')
    ax1.plot(circle1, circle2)


    ax2 = fig.add_axes([.05, .05, .425, .425])
    ax2.set_title("Ellipse", fontsize='large')
    ax2.plot(ellipse1, ellipse2)


    ax3 = fig.add_axes([.55, .33, .425, .2])
    ax3.set_title("Dynamical System", fontsize='large')
    ax3.plot(final1, final2)


    plt.show()





def remove_negative_zeros (negative_matrix):


    for i in range(2):
        for j in range(2):
            if (negative_matrix[i,j] == -0.0 or negative_matrix[i, j] == -0.):
                negative_matrix[i,j] = 0


    return negative_matrix





make_subplots(*find_values_to_plot(our_matrix, our_initial_vector))
