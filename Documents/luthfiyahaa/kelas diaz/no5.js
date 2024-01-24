document.querySelector('form').addEventListener('submit', function (event) {
    event.preventDefault()

    const nama = document.getElementById('nama').value
    const email = document.getElementById('email').value
    const jam = document.getElementById('jam').value
    const tiket = document.getElementById('tiket').value
    const tujuan = document.getElementById('tujuan').value
})