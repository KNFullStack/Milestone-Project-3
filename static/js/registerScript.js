// Method to check that the two passwords entered into the boxes are the same
let passwordOne = document.getElementById("password")
let passwordTwo = document.getElementById("password_check")
let form = document.getElementById("registerForm")
let passwordWarning = document.getElementById("passwordsIncorrect")

form.addEventListener("submit", confirmPassword)

function confirmPassword(event) {
    event.preventDefault();
    if (passwordOne.value != passwordTwo.value) {
        passwordWarning.classList.remove("hidden")
    } else {
        passwordWarning.classList.add("hidden")
        form.submit();
    }
    return
}