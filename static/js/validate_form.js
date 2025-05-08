function validateFormById(formId) {
  $('#' + formId).on('submit', function (e) {
    let valid = true;

    $(this).find('input, select, textarea').each(function () {
      if ($(this).prop('required') && !$(this).val()) {
        $(this).addClass('is-invalid');
        valid = false;
      } else {
        $(this).removeClass('is-invalid');
      }
    });

    if (!valid) {
      e.preventDefault();
    }
  });
}

