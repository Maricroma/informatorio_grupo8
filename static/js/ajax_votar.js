
function votar(id_usuario, id_video, elemento) {
    $.ajax({
        data: {
            csrfmiddlewaretoken: $(elemento).siblings("input[name='csrfmiddlewaretoken']").val(),
            'id_usuario': id_usuario,
            'id_video': id_video},
        url:$(elemento).attr("data-url"),
        type: 'post',

        success: function(x) {
            if (x.estado == 'ok'){
                document.getElementById(x.id), classList.toggle('btn-primary');
                document.getElementById(x.id), classList.toggle('btn-success');
                elemento.setAttribute("value","Te gusta")
            }
            else if (x.estado == 'error'){
                errorVotarCategoria();
            }
            else {
                noPodesVotarte();
            }
        }
    });
}