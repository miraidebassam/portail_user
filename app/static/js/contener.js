$(document).ready(function () {
        $(".nav_link").click(function (e) {
            e.preventDefault();
            var target = $(this).data("target");
            
            // Exemple : si le lien "Invoices" est cliqué, effectuer une requête AJAX
            if (target === "invoices-content") {
                $.ajax({
                    url: "{{ url_for('main.invoice_content') }}",
                    type: "GET",
                    success: function (data) {
                        $("#content-container").html(data);
                    }
                });
            }
        });
    });
