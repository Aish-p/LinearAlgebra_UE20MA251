import numpy as np
def print_mat(matrix , row , col):
    for i in range ( row ) :
        for j in range ( col ) :
            print(matrix [ i ] [ j ] , end = '\t')
        print()
    print()

def main () :
    n = int(input("Enter the number of pages :"))
    adj_mat = np . zeros ([ n , n ])

    print()
    for i in range (n) :
        print ("For page" , i , " : " )
        num_conn = int (input("Enter the number of links in the page :" ) )
        weight_pages = round ( 1 / num_conn , 4 )
        for q in range( num_conn ) :
            y = int (input( "Page referenced :"))
            adj_mat [y][i] = weight_pages
        print()
    vec = np . zeros([n , 1])
    for i in range(n) :
        vec [i][0] = round ( 1/n,4)
    print( "Vector : " )
    print_mat( vec , n , 1 )
    print("Transition  Matrix :")
    print_mat(adj_mat,n,n)

    for i in range(100):
        vec1 = np.dot(adj_mat,vec)
        for j in range(n-1):
            if ( vec [ j ] == vec1 [ j ] ) :
                break
            vec = vec1
    print("Final weights of the pages:")
    print(vec)

if __name__ =="__main__":
    main()
