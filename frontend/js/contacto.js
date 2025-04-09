document.addEventListener('DOMContentLoaded', function () {

    const manejoFormulario= ()=>{

        const form= document.getElementById("i-contacto-form")

        form.addEventListener("submit", function(event){
            event.preventDefault()

            const nombre= document.getElementById("nombre").value
            const email= document.getElementById("email").value
            const mensaje= document.getElementById("mensaje").value
            const terminos= document.getElementById("terminos").checked

            if(!nombre || !email || !mensaje || !terminos){
                alert("Por favor, completa los campos vacios.")
                return
            }

            console.log(`Formulario enviado con nombre ${nombre}, email ${email}, mensaje ${mensaje}, terminos ${terminos}`)
            alert("¡Formulario enviado con éxito!")

            form.reset()

        })
    }

    manejoFormulario()

})