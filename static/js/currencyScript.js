// Currency Selector
let currency = document.getElementById('currency')
let currencySpan = document.getElementsByClassName("currencyPlacement")

currency.addEventListener("change", () => {
    if (currency.value == "GBP") {
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = "£"
        }
    } else if (currency.value == "USD") {
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = "$"
        }
    } else if (currency.value == "Euro") {
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = "€"
        }
    } else {
        for (let i = 0; i < currencySpan.length; i++) {
            currencySpan[i].innerText = ""
        }
    }
})