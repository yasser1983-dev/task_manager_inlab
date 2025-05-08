function validateFormLogin() {
  $('#loginForm').on('submit', function (e) {
    let valid = true;
    $(this).find('input').each(function () {
      if (!$(this).val().trim()) {
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
