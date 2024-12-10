
def fis():
    a=str(input())
    summ=0
    for i in range(len(a)):
        summ=int(a[0])+summ
        a=a[1:]
    print(summ)

def multiply_matrices(A, B):        
    # Проверка совместимости матриц
    if len(A[0]) != len(B):
        raise ValueError("Число столбцов матрицы A должно быть равно числу строк матрицы B.")

    M = len(A)         # Количество строк в A
    N = len(A[0])      # Количество столбцов в A
    P = len(B)         # Количество строк в B
    Q = len(B[0])      # Количество столбцов в B

    # Инициализация результирующей матрицы C размером MxQ нулями
    C = [[0 for _ in range(Q)] for _ in range(M)]

    # Умножение матриц
    for i in range(M):
        for j in range(Q):
            for k in range(N):
                C[i][j] += A[i][k] * B[k][j]
              # Печать промежуточного результата

    return C

# Пример использования:
if __name__ == "__main__":
    # Матрица A размерности 2x3
    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    # Матрица B размерности 3x2
    B = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    print("Матрица A:")
    for row in A:
        print(row)

    print("\nМатрица B:")
    for row in B:
        print(row)

    try:
        C = multiply_matrices(A, B)
        print("\nМатрица C (A x B):")
        for row in C:
            print(row)
    except ValueError as e:        print(f"Ошибка: {e}") 
