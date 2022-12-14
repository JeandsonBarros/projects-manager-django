/* ----------- Start script modal ---------*/

function modalService(action, display) {

    if (display == 'none') {
        document.querySelector('#formService').reset();
        document.querySelector('#quantityCararacters').value = 0
    }

    let divModal = document.querySelector('#divModal')
    let formService = document.querySelector('#formService')

    divModal.style.display = display
    formService.style.display = display
    formService.action = action

}

function setValuesService(name, price, description, action) {

    document.querySelector('#id_name').value = name
    document.querySelector('#id_price').value = price
    document.querySelector('#id_description').value = description

    document.querySelector('#quantityCararacters').value = description.length

    modalService(action, 'block')

}

/* async function editService(event) {

    event.preventDefault();
   
    const form = document.querySelector('#formService')

    let data = new FormData(form);
    let token = document.querySelectorAll('input')[0].value;

    let fetchData = {
        method: 'POST',
        headers: {
            'X-CSRF-TOKEN': token
        },
        body: data
    }

    try {
        
        const response = await fetch(form.action, fetchData)

        if (response.status = 200){

            if (form.action.includes('editar'))
                alert('Serviço editado!')

            else if (form.action.includes('salvar')){
                alert('Serviço salvo!')
                modalService(form.action, 'none')
            }

            document.location.reload(true)

        }
        else
            alert('Erro ao execultar ação!')

    } catch (error) {
        console.log(error);
    }

} */

/* ----------- end script modal ---------*/

async function searchService(event, all = false) {
    event.preventDefault()

    const form = document.querySelector('#searchService')
    const search = form.querySelector('#search')

    try {

        if (all) {
            const response = await fetch(form.action)
            const data = await response.text()
            search.value = ''
            return document.querySelector('#listServices').innerHTML = data
        }

        const response = await fetch(form.action + "?search=" + search.value)
        const data = await response.text()
        document.querySelector('#listServices').innerHTML = data

    } catch (error) {
        console.log(error);
        alert('Erro ao buscar serviço.')
    }

}

async function paginatorServices(path) {

    try {
        const response = await fetch(path)
        const data = await response.text()
        document.querySelector('#listServices').innerHTML = data
    } catch (error) {
        alert("Erro ao listar serviços")
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

    var htmlAlert = '<div class="alert success alert-dismissible fade show " role="alert">' +
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
            htmlAlert = htmlAlert.replace('success', 'error')
            alert.innerHTML = htmlAlert.replace('message-here', 'Erro ao editar projeto!')

            window.scroll({
                top: 0,
                behavior: 'smooth'
            })
        }

    } catch (error) {
        console.log(error)

        htmlAlert = htmlAlert.replace('success', 'error')
        alert.innerHTML = htmlAlert.replace('message-here', 'Erro ao editar projeto!')

        window.scroll({
            top: 0,
            behavior: 'smooth'
        })
    }

}

