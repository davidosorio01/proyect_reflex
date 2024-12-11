import reflex as rx

class Calculadora(rx.State):
    valor: list = ["",] 
    union_str: str 
    i: str 
    
    #NUMEROS [0,1,2,3,4,5,6,7,8,9]
    def valores(self, x):
        self.valor.append(x)
    
    #SIMBOLOS SIN LOGICA [+,-,*,/,.]
    def simbol(self, x):
        self.valor.append(x)
        
    #LOGICA DEL PORCENTAJE
    def valoresporc(self):
        self.valor = [self.i for self.i in self.valor]
        self.union_str = ""
        
        for self.i in self.valor: 
            if self.i == "=":
                pass
            else:
                self.union_str += str(self.i)
        self.valor = eval(self.union_str)/100
        self.valor = ["=", self.valor]
    
    #LOGICA DEL BORRAR UNO EN UNO
    def valoresdel(self):
        if isinstance(self.valor, list):
            self.valor.pop()
        else:
            self.valor = ["",]       
            
    #LOGICA DEL IGUAL
    def valoresiqual(self):
        self.valor = [str(self.i) for self.i in self.valor]
        self.union_str = ""
        
        for self.i in self.valor:
            if self.i != "=":
                self.union_str += str(self.i)
                
        print(f"{self.union_str} = {eval(self.union_str)}")

        try:
            self.valor = round(eval(self.union_str), 4)
            self.valor = ["=", self.valor]
        except Exception:
            self.valor = ["ERROR"]
        
    #LOGICA DEL BORRAR EN TOTAL
    def clear(self):
        self.valor = ["",]
        self.valor.clear()
        self.valor.append("",)