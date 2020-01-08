def generate(k, A):
    if k == 1:
        print(A)
    else:
        for i in range(0, k):
            generate(k - 1, A)
            if k % 2 == 0:
                A[i], A[k-1] = A[k-1], A[i]
            else:
                A[0], A[k-1] = A[k-1], A[0]


generate(3, [2, 4, 8])
