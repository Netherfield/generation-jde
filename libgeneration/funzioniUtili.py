class FunzioniUtili:
    @staticmethod
    def valida_numero(valore, minimo, massimo):
        if valore.isdigit() == False:
            return False
        else:
            valore = int(valore)
        if valore not in range(minimo, massimo):
            return False
        return True

    @staticmethod
    def numero_intero_positivo_input(minimo, massimo):
        n = (input("Inserisci numero positivo"))
        while FunzioniUtili.valida_numero(n, minimo, massimo) == False:
            n = (input("Inserisci numero positivo"))
        n = int(n)
        return n
    
    
    @staticmethod
    def calcola_primo(numero):
        '''
        questa funziona calcola se un numero è primo
        solleva un'eccezione typeerror se il numero non è intero
        '''
        primo = True
        
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True