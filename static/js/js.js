// ==== Activar Select2 ====
$(document).ready(function () {
    $('#select-cliente').select2({
        placeholder: "Buscar cliente...",
        width: '100%',
        allowClear: true
    });

    $('#select-servicio').select2({
        placeholder: "Buscar servicio...",
        width: '100%',
        allowClear: true
    });
});
