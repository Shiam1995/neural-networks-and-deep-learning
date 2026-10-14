"""
Sigmoid neurons simulating perceptrons, part I
Suppose we take all the weights and biases in a network of perceptrons,
 and multiply them by a positive constant, c>0
. Show that the behaviour of the network doesn't change
"""

def Nand_Gate(input1,input2,weight1,weight2, bias, threshold):
    print("input1:",input1)
    print("input2:",input2)
    print("weight1:",weight1)
    print("weight2:",weight2)
    print("bias:",bias)
    print("threshold:",threshold)
    sum = 0

    if (input1*weight1 + input2*weight2 + bias > threshold):

        print("output greater than : thresehold " + str(threshold))
        sum = (input1 * weight1 + input2 * weight2 + bias)
        print(f"{input1} * {weight1} + {input2} * {weight2} + {bias} = {sum}")
        print(input1 * weight1 + input2 * weight2)
    else:
        print("output less than : thresehold " + str(threshold))
        sum = (input1 * weight1 + input2 * weight2 + bias)
        print(f"{input1} * {weight1} + {input2} * {weight2} + {bias} = {sum}")
        print(input1 * weight1 + input2 * weight2 + bias)



Nand_Gate(-1,1,-2,-2,3,5)
