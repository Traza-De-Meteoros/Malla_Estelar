import json

class PuntosImagen:
    """
    Puntos Imagen sería las estrellas de referencia que se llegan a encontrar en la imagen
    X y Y son las coordenadas de imagen, en Y es el valor que resulta de restar el valor del ancho total de la imagen
    Ejemplo: Tamaño de imagen(720x560) Se localiza la estrella en 650,300 en puntos imagen sería (650,560-300)
    """
    def __init__(self, nombre:str, ascencion:int, declinacion:int, coordsX:int, coordsY:int):
        self.nombre=nombre
        self.ascencion=ascencion
        self.declinacion=declinacion
        self.x=coordsX
        self.y=coordsY
        self.xi=0
        self.psi=0
    
    def __str__(self):
        return "Nombre:{} , Ascencion:{}, Descencion:{}, X:{}, Y:{}".format(self.nombre, self.ascencion, self.declinacion, self.x, self.y)

class EstRef(PuntosImagen):
    """
    EstRef es las Estrellas con las que se desea generar la malla.
    Normalmente se tomarían de un catálogo que es un archivo cvs
    en el cual solo se tendría nombre y coordenadas estelares.
    En estos ejemplos se tiene X y Y para poder calcula el error que tiene el
    software al generar la malla.
    """
    def __init__(self, nombre, ascencion, declinacion, coordsX, coordsY):
        PuntosImagen.__init__(nombre, ascencion, declinacion, coordsX,coordsY)


def transform_from_json_to_list(file:str, pts_img:bool=True):
    """
    Esta funcion convierte el contenido Json a listas de instancias de la clase PuntosImagen o EstRef
    PARAMS:
     file : archivo a ser leído
     pts_img : true= PuntosImagen , false=EstRef
    """
    list_to_be_returned=[]
    with open(file) as f:
        data = json.load(f)
    for json_str in data:
        if pts_img:
            ptsImg= PuntosImagen(json_str["Nombre"], json_str["Ascension"], json_str["Declinacion"], int(json_str["X"]),int(json_str["Y"]))
            list_to_be_returned.append(ptsImg)
        else:
            est_ref= EstRef(json_str["Nombre"], json_str["Ascension"], json_str["Declinacion"], int(json_str["X"]),int(json_str["Y"]))
            list_to_be_returned.append(est_ref)
    return list_to_be_returned
