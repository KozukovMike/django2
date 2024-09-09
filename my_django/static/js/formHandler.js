$(document).ready(function() {
    $('#registrationForm').on('submit', function(event) {
        event.preventDefault();  // Отключаем стандартное поведение формы

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $(this).serialize(),
            success: function(response) {
                $('#responseMessage').text(response.message).css('color', 'green').show();
            },
            error: function(xhr) {
                // Обработка ошибки
                let responseText = xhr.responseText;
                try {
                    let errors = JSON.parse(responseText).errors;
                    let errorMessage = "Ошибка: ";
                    for (let field in errors) {
                        errorMessage += errors[field].join(", ") + " ";
                    }
                    $('#responseMessage').text(errorMessage).css('color', 'red').show();
                } catch (e) {
                    $('#responseMessage').text("Ошибка сервера").css('color', 'red').show();
                }
            }
        });
    });
});
