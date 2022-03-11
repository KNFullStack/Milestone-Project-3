// Method to check that the two passwords entered into the boxes are the same
let passwordOne = document.getElementById("password")
let passwordTwo = document.getElementById("password_check")
let registerButton = document.getElementById("register_button")

passwordOne.addEventListener("input", confirmPassword)
passwordTwo.addEventListener("input", confirmPassword)

function confirmPassword() {
    if (passwordOne.value != passwordTwo.value) {
        registerButton.classList.add("unclickable")
    } else {
        registerButton.classList.remove("unclickable")
    }
}

// Deletion Confirmation Popup