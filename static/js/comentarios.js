// Archivo: comentarios.js

/*var main = function () {
    "use strict";

    var addCommentFromInputBox = function () {
        var $new_comment;

        if ($(".comment-input input").val() !== "") {
            $new_comment = $("<p>").text($(".comment-input input").val());
            $new_comment.hide();
            $(".comments").append($new_comment);
            $new_comment.fadeIn();
            $(".comment-input input").val("");
        }
    };

    $(".comment-input button").on("click", function (event) {
        addCommentFromInputBox();
    });

    $(".comment-input input").on("keypress", function (event) {
        if (event.keyCode === 13) {
            addCommentFromInputBox();
        }
    });
};

$(document).ready(main);
*/
var main = function () {
    "use strict";

    var addCommentFromInputBox = function () {
        var $new_comment;
        var comentario = $(".comment-input input").val();

        if (comentario !== "") {
            $.post("/add_comment", { comentario: comentario })
                .done(function (data) {
                    $new_comment = $("<p>").text(comentario);
                    $new_comment.hide();
                    $(".comments").append($new_comment);
                    $new_comment.fadeIn();
                    $(".comment-input input").val("");
                })
                .fail(function () {
                    alert("Error al agregar el comentario.");
                });
        }
    };

    $(".comment-input button").on("click", function (event) {
        addCommentFromInputBox();
    });

    $(".comment-input input").on("keypress", function (event) {
        if (event.keyCode === 13) {
            addCommentFromInputBox();
        }
    });
};

$(document).ready(main);
