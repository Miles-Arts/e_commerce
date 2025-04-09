document.addEventListener('DOMContentLoaded', function () {

    const mostrarGranja = () => {

        const cardSection = document.getElementById("i-card-section")

        const granjas = [
            { nombre: "Granja Fresas Colombia", producto: "Fresa", img: "fresas.jpg", ubicacion: "Tuta", fecha: new Date(2024, 10, 14) },
            { nombre: "Granja Avi Boyacá", producto: "Huevos", img: "huevos.jpg", ubicacion: "Paipa", fecha: new Date(2024, 10, 17) },
            { nombre: "Maiz S.A", producto: "Maiz", img: "maiz.jpg", ubicacion: "Chocontá", fecha: new Date(2024, 10, 22) },
            { nombre: "Papa del campo", producto: "Papa", img: "papa.jpg", ubicacion: "Sogamoso", fecha: new Date(2024, 10, 15) },
            { nombre: "Granja Cristal", producto: "Durazno", img: "durazno.jpg", ubicacion: "Toca", fecha: new Date(2024, 10, 4) },
            { nombre: "Granja del Norte", producto: "Carne", img: "carne.jpg", ubicacion: "Sotaquirá", fecha: new Date(2024, 10, 1) }
        ]

        granjas.forEach(granja => {
            const verGranja = document.createElement("div")
            verGranja.className = "col-lg-4 col-md-6 col-sm-6 "
            verGranja.innerHTML = `  
                    <div class="card" style="width: 18rem;">
                        <img src="./img/${granja.img}" class="card-img-top" alt="Productos de Granja ${granja.nombre}">
                        <div class="card-body">
                            <h5 class="card-title">${granja.nombre}</h5>
                            <p class="card-text">${granja.producto}</p>
                            <p class="card-text">${granja.ubicacion}</p>
                            <p class="card-text">${granja.fecha.toLocaleDateString()}</p>
                            <a href="#" class="btn btn-primary">Ver más</a>
                        </div>
                    </div>
            `

            cardSection.appendChild(verGranja)

        })

    }

    mostrarGranja()

})