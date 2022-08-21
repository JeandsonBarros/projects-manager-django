
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

function deleteProject(id, name) {
    if (confirm(`Realmente deseja deletar o projeto ${name}?`)) {
        window.location.href = `${location.origin}/projetos/delete/${id}`
    }
}


async function editProject(e) {
    e.preventDefault()

    let form = document.querySelector('#form')

    let data = new FormData(form);
    let token = document.querySelectorAll('input')[0].value;

    let fetchData = {
        method: 'POST',
        headers: {
            'X-CSRF-TOKEN': token
        },
        body: data
    }

    var htmlAlert = '<div class="alert alert-success alert-dismissible fade show " role="alert">' +
        '<span> message-here </span>' +
        '<button type="button" class="btn-close" onclick="hidenAlert()"</button>' +
        '</div>';
    const alert = document.querySelector('#alert')

    try {

        const response = await fetch(form.action, fetchData)

        if (response.status === 200) {

            window.scroll({
                top: 0,
                behavior: 'smooth'
            })

            document.getElementById("alert").style.display = "block"
            alert.innerHTML = htmlAlert.replace('message-here', 'Projeto editado com sucesso!')

        } else {
            htmlAlert = htmlAlert.replace('success', 'danger')
            alert.innerHTML = htmlAlert.replace('message-here', 'Erro ao editar projeto!')

            window.scroll({
                top: 0,
                behavior: 'smooth'
            })
        }

    } catch (error) {
        console.log(error)

        htmlAlert = htmlAlert.replace('success', 'danger')
        alert.innerHTML = htmlAlert.replace('message-here', 'Erro ao editar projeto!')
     
        window.scroll({
            top: 0,
            behavior: 'smooth'
        })
    }

}

function hidenAlert() {
    document.getElementById("alert").style.display = "none";
}

function menu() {
    const menuButton = document.getElementById("menu")
    menuButton.style.display = menuButton.style.display == "block" ? 'none' : 'block';
}