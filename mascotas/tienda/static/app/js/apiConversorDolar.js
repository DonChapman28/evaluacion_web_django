$(function() {
    $.getJSON('https://mindicador.cl/api', function(data) {
        var dailyIndicators = data;
        var tipoCambioDolar = dailyIndicators.dolar.valor;

        $('[name="precioApi"]').each(function() {
            var precioOriginal = parseFloat($(this).data('precio-original'));
            var precioDolar = (precioOriginal / tipoCambioDolar).toFixed(2);
            $(this).text("$" + precioDolar);
        });
    });
});

