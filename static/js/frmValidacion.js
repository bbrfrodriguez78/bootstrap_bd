// Archivo: frmValidacion.js

$(document).ready(function () {
    // Agrega efecto Blur al evento para los campos requeridos obligatorios
    $('.required').on('blur', function () {
        if ($(this).val() === '') {
            $(this).addClass('error');
        } else {
            $(this).removeClass('error');
        }
    });

    $('#registerButton').click(function () {
        var isValid = true;

        // Revisa todos los campos requeridos
        $('.required').each(function () {
            if ($(this).val() === '') {
                isValid = false;
            }
        });

        if (!isValid) {
            alert('Ingresa todos los campos requeridos.');
            return;
        }

    });
});