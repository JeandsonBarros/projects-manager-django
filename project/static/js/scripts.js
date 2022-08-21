/* ((doc, win) => {

    const prefersColorScheme = window.matchMedia('(prefers-color-scheme: dark)');

    if (prefersColorScheme.matches) {
        
        doc.body.style.backgroundColor = "rgb(50,50,50)";
        doc.body.style.color = "#fff";
        doc.getElementsByTagName('header')[0].style.background = '#5a5a5a'
        doc.getElementsByTagName('footer')[0].style.background = '#5a5a5a'
        doc.getElementsByTagName('nav')[0].style.background = '#3a3a3a'

        let inputs = doc.querySelectorAll('.form-control')
        inputs.forEach(input => {
            input.style.backgroundColor = '#3a3a3a'
            input.style.color = '#fff'
        })

        let cards = doc.querySelectorAll(".cardProject")
        cards.forEach(card => {
            card.style.background = '#323232';
            card.style.boxShadow = '20px 20px 60px #2b2b2b, -20px -20px 60px #3a3a3a';

        })
    }

})(document, window)
 */

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
        '<strong> message-here </strong>' +
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
        }

    } catch (error) {
        console.log(error)
        htmlAlert = htmlAlert.replace('success', 'danger')
        alert.innerHTML = htmlAlert.replace('message-here', 'Erro ao editar projeto!')
    }

}

function hidenAlert() {
    document.getElementById("alert").style.display = "none";
}

function menu() {
    const menuButton = document.getElementById("menu")
    menuButton.style.display = menuButton.style.display == "block" ? 'none' : 'block';
}