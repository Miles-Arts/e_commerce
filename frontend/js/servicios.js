document.addEventListener('DOMContentLoaded', function () {

    const servicios = [
        {
            id: 1,
            nombre: "Tour de caminatas por los Bosques en Boyacá",
            descripcion: "Participa en nuestros tours guiados y experimenta la belleza y diversidad de los bosques.",
            imagen: "avistamiento.jpg" 
        },
    
        {
            id: 2,
            nombre: "Programas Educativos",
            descripcion: "Involúcrate en nuestros programas educativos diseñados para todas las edades y aprende sobre la importancia de la biodiversidad arborea.",
            imagen: "programas1.jpg"
        },
        {
            id: 3,
            nombre: "Conservación de árboles",
            descripcion: "Aprende sobre nuestras iniciativas de conservación para proteger y preservar las especies bosques locales.",
            imagen: "conservacion.jpg"
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