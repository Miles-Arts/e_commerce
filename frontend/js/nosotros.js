document.addEventListener('DOMContentLoaded', function () {

    const servicios = [
        {
            id: 1,
            nombre: "Comunidad",
            descripcion: "Líderes en el sector para fomentar el cambio.",
            imagen: "nosotros_01.jpg" 
        },
        {
            id: 2,
            nombre: "Colegios",
            descripcion: "Los saberes científicos en pro de la naturaleza.",
            imagen: "nosotros_02.jpg"
        },
        {
            id: 3,
            nombre: "Empresas",
            descripcion: "Apoyo privado para la preservación de los árboles.",
            imagen: "nosotros_03.jpg"
        }
    ];
 
    const mostrarServicios = () => {
        const listServicios = document.getElementById('i-list-servicios');

        servicios.forEach(servicio => {
            const div = document.createElement('div');
            div.className = 'col-md-4 mb-4';
            div.innerHTML = `
                <div class="card">
                    <img src="../img/${servicio.imagen}" class="card-img-top" alt="${servicio.nombre}">
                    <div class="card-body">
                        <h5 class="card-title">${servicio.nombre}</h5>
                        <p class="card-text">${servicio.descripcion}</p>
                    </div>
                </div>
            `;
            
            listServicios.appendChild(div);
        });
    };

    mostrarServicios();

});