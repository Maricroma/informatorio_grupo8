function cambiar(categoria){
    $(document).ready(function(categoria) {


        if (categoria == "madera"){
            alert("hola")

            $("#imagenCabecera").attr("src","/static/imagenes/madera2.jpeg");
        }
        else if (categoria == "concreto"){
            $("#imagenCabecera").attr("src","/static/imagenes/concreto.jpeg");
        }
        else if (categoria == "metal"){
            document.getElementById("imagenCabecera").src="metal.jpeg";
        }
        else if (categoria == "artesania"){
            document.getElementById("imagenCabecera").src="artesanias.jpeg";
        }
        else if (categoria == "pintura"){
            document.getElementById("imagenCabecera").src="pinturas.jpeg";
        }
        else if (categoria == "marmol"){
            document.getElementById("imagenCabecera").src="piedra2.jpeg";
        }
        else if (categoria == "arena"){
            document.getElementById("imagenCabecera").src="arena.jpeg";
        }
        else {
            document.getElementById("imagenCabecera").src="bienaldigital.jpg";
        }
    
      
    });
}