
function confirmarVoto(user_id, video_id) {

    Swal.fire({
        title: '¿Estás seguro?',
        text: "No podrás volver a votar en esta categoría.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, estoy seguro',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            votar(user_id, video_id)
          )
        }
      })
}

function enviar() {
  formulario = document.getElementById("mensajeForm");
    formulario.submit();
    return true;

}


function confirmarMensaje() {

  Swal.fire({
    position: 'top-end',
    icon: 'success',
    title: 'Tu mensaje ha sido enviado.',
    showConfirmButton: false,
    timerProgressBar: true,
    timer: 1500,
    
  })
  .then((result) =>{
    setTimeout(() => {
      enviar()
    }, 0);
  });

}

function confrimarRegistro(mensaje){
  Swal.fire({
    position: 'top',
    icon: 'success',
    title: mensaje,
    showConfirmButton: false,
    timer: 1500
  })
}