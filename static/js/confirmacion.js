
function confirmarVoto(user_id, video_id, elemento) {

    Swal.fire({
        title: '¿Estás seguro?',
        text: "No podrás volver a votar en esta categoría.",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, votar',
        cancelButtonText: 'Cancelar'
      }).then((result) => {

        if (result.isConfirmed) {
          votar(user_id, video_id, elemento);
          Swal.fire(
            'Hecho!',
            'Tu voto ha sido registrado.',
            'success',
          );
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

function errorVotarCategoria(){
  const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener('mouseenter', Swal.stopTimer)
      toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
  })
  
  Toast.fire({
    icon: 'error',
    title: '¡¡No podes votar en la misma categoria!!'
  })
}

function noPodesVotarte(){
  const Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 3000,
    timerProgressBar: true,
    didOpen: (toast) => {
      toast.addEventListener('mouseenter', Swal.stopTimer)
      toast.addEventListener('mouseleave', Swal.resumeTimer)
    }
  })
  
  Toast.fire({
    icon: 'error',
    title: '¡¡No podes votarte a vos mismo!!!'
  })
}