def maior_primo(n):
    while n != 1:
        i = 2
        primo = True

        while i < n and primo == True:

            if n % i == 0:

                primo = False

            i = i + 1

        if primo == True:

            return n

        n = n - 1
