// Fungsi untuk memvalidasi password
function validatePassword() {
    var passwordInput = document.getElementById('password');
    var password = passwordInput.value;

    // Pattern untuk memeriksa apakah password memiliki setidaknya 8 karakter, satu simbol atau angka,
    // dan tidak terlalu mudah (Anda dapat menyesuaikan pola sesuai kebutuhan)
    var pattern = /^(?=.*[0-9!@#$%^&*])(?=.{8,})/;

    if (!pattern.test(password)) {
        document.getElementById('password-validation-message').textContent = "Password harus memiliki setidaknya 8 karakter, satu simbol atau angka, dan tidak terlalu mudah.";
        passwordInput.setCustomValidity("Password tidak valid");
    } else {
        document.getElementById('password-validation-message').textContent = "";
        passwordInput.setCustomValidity("");
    }
}

// Tambahkan event listener untuk memvalidasi password saat input berubah
var passwordInput = document.getElementById('password');
if (passwordInput) {
    passwordInput.addEventListener('input', validatePassword);
}
