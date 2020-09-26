
function votar(id_usuario, id_video) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: '{{ csrf_token }}',
            'id_usuario': id_usuario,
            'id_video': id_video},
        url: "{% url 'votar_ajax %}",
        type: 'post',

        success: function(x) {
            if (x.console == 'ok'){
                document.getElementById(x.id), classList.toggle('btn-primary');
                document.getElementById(x.id), classList.toggle('btn-success');
            }
        }
    });
}