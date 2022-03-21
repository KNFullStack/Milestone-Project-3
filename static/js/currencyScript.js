// Currency Selector
let currency = document.getElementById('currency')
let currencySpan = document.getElementsByClassName("currencyPlacement")
const storedCurrency = JSON.parse(localStorage.getItem('currency'));
window.addEventListener("load", () => {
    currency.value = storedCurrency;
    loadCurrency();
})


// Function to check if storedCurrency exists, then uses Switch to set currency.
function loadCurrency() {
    switch (storedCurrency) {
        case "GBP":
            for (let i = 0; i < currencySpan.length; i++) {
                currencySpan[i].innerText = "£";
            }
            break;
        case "USD":
            for (let i = 0; i < currencySpan.length; i++) {
                currencySpan[i].innerText = "$"
            }
            break;
        case "Euro":
            for (let i = 0; i < currencySpan.length; i++) {
                currencySpan[i].innerText = "€"
            }
            break;
    }
}

// Function to change the localStorage currency item based on a selection, then alter currency accordingly.
currency.addEventListener("change", () => {
    if (currency.value == "GBP") {
        window.localStorage.setItem("currency", JSON.stringify(currency.value));
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = "£"
        }
    } else if (currency.value == "USD") {
        window.localStorage.setItem("currency", JSON.stringify(currency.value));
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = "$"
        }
    } else if (currency.value == "Euro") {
        window.localStorage.setItem("currency", JSON.stringify(currency.value));
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = "€"
        }
    } else {
        window.localStorage.setItem("currency", JSON.stringify(currency.value));
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = ""
        }
    }
})