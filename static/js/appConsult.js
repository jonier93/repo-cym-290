function consult_user() {
    let id = document.getElementById("id").value
    fetch("/consult_user", {
        "method":"post",
        "headers":{"Content-Type":"application/json"},
        "body":JSON.stringify(id)
    })
    .then(resp => resp.json())
    .then(data => document.getElementById("txt-data").value = data.name + " " + data.lastname)
    .catch(error => alert("Error"))
}
