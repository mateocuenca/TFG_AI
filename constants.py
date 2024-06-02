system_instructions = """Tenés que devolver los datos en el siguiente formato JSON:

Algunas aclaraciones:

1. En caso de no encontrar el dato, completar con "none";
2. "experiencia" contiene un arreglo de 1 a n experiencias (experiencia-1, experiencia-2, experiencia-n)
3. "tecnologias" contiene un arreglo de strings con nombres de las tecnologías
4. "educacion" contiene un arreglo de 1 a n educaciones (educacion-1, educacion-2, educacion-n)
5. "idioma" contiene un arreglo de 1 a n idiomas (idioma-1, idioma-2, idioma-n)
6. "tecnologias-extra" contiene un arreglo de strings con nombres de las tecnologías que no estan mencionadas dentro de una experiencia o educacion

{
"datos-personales":
{
"nombre-completo":,
"fecha-nacimiento":,
"ubicacion":,
"telefono":,
"email":
},
"experiencia":
[
"experiencia-1":{
"puesto":,
"empresa":,
"fecha-comienzo":,
"fecha-fin":
"tecnologías":[]
}
],
"educacion":
[
"educacion-1":{
"nombre-curso":,
"institucion":,
"fecha-comienzo":,
"fecha-fin",
"tecnologias":[]
}
],
"idioma":
[
"nombre-idioma":,
"nivel":
],
tecnologias-extra:[]
}
"""
