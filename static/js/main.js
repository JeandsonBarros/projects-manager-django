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