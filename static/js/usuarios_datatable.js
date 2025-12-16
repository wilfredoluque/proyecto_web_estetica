$(document).ready(function () {
    $('#tablaUsuarios').DataTable({
        responsive: false,
        scrollX: true,
        autoWidth: false,
        pageLength: 10,
        lengthMenu: [5, 10, 20, 50, 100],

        language: {
            lengthMenu: "Mostrar _MENU_ registros",
            zeroRecords: "No se encontraron usuarios",
            info: "Mostrando _START_ a _END_ de _TOTAL_ usuarios",
            infoEmpty: "No hay datos disponibles",
            search: "Buscar:",
            paginate: {
                first: "Primero",
                last: "Último",
                next: "Siguiente",
                previous: "Anterior"
            }
        }
    });
});
