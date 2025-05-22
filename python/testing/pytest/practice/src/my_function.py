class calculadora:

    def add(n1, n2):
        return n1 + n2
    
    def mult(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        # no se puede dividir entre 0
        if n2 == 0:
            raise ValueError
        
        return n1 / n2