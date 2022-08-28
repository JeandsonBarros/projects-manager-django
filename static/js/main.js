/* ---------- Start script dark theme ------------ */

var check = document.querySelector('#trigger')
var html = document.querySelector('html')

if (!localStorage.getItem('dark')) {
    const prefersColorScheme = window.matchMedia('(prefers-color-scheme: dark)');

    localStorage.setItem('dark', prefersColorScheme.matches)
    check.checked = prefersColorScheme.matches
}

var isDark = JSON.parse(localStorage.getItem('dark'))

if (isDark) {
    html.classList.toggle('dark')
    check.checked = true
}

check.addEventListener('change', () => {
    let booleanTpggle = html.classList.toggle('dark')
    localStorage.setItem('dark', booleanTpggle)
})

/* ---------- End script dark theme ------------ */

function hidenAlert() {
    document.getElementById("alert").style.display = "none";
}

function genericModal(id){
    const element = document.getElementById(id)
    element.style.display = element.style.display == "flex" ? 'none' : 'flex';
}

function deleteConfirm(message, path) {
    if (confirm(message)) {
        window.location.href = `${location.origin}${path}`
    }
}