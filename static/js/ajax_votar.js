
function votar(id_usuario, id_video) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            'id_usuario': id_usuario,
            'id_video': id_video},
        url: "{% url 'votar_ajax %}",
        type: 'POST',

        success: function(x) {
            console.log(x.estado);
            if (x.console == 'ok'){
                console.log('Hola')
                console.log(x.id)
                document.getElementById(x.id), classList.toggle('btn-primary');
                document.getElementById(x.id), classList.toggle('btn-success');
                console.log('Bye')
            }
        }
    });
}