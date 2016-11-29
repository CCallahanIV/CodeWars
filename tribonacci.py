def tribonacci(signature,n):
    while n > 3:
        signature.append(sum(signature[-3:]))
        return tribonacci(signature, n-1)
    else:
        if n==3:
            return signature
        else:
            return signature[:n]
