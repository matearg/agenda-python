import re
patron1 = re.compile(r'((?P<name>[a-zA-Z 0-9]*)(?(name)-Administrador|))')

nombre = 'Pedro-Administrador ap>-Administrador Juan-Administrador rp4 w'
print(patron1.search(nombre))

patron2 = re.compile(r'(<)?(\w+@\w+(?i:\.[a-z]+)+)(?(1)>|$)')
mail1 = "<user@host.com>"
mail2 = "user@host.com"
mail3 = "<user@Host.Com"
mail4 = "user@host.com>"
print(patron2.search(mail1))
print(patron2.search(mail2))
print(patron2.search(mail3))
print(patron2.search(mail4))





class Persona:

    def __init__(self, usuario):
        self._usuario = usuario
        
    def getUsuario(self):
        self._usuario
        return 
        """
        if not valid():
            raise TypeError('cannot fetch name')
        else:
            return self.name.transform()"""
    def setUsuario(self, valor):
        pass
        """if not valid(value):
            raise TypeError('cannot change name')
        else:
            self.name = transform(value)"""

persona = Persona('Juan-Administrador')
persona.getUsuario()
persona.setUsuario('Juan-Administrador')