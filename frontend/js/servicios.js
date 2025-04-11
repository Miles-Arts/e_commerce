document.addEventListener('DOMContentLoaded', function () {

    const servicios = [
        {
            id: 1,
            nombre: "Tienda Online de Productos Agroindustriales",
            descripcion: "Compra frutas, vegetales, lácteos y productos transformados directamente de productores locales a través de nuestra plataforma web.",
            imagen: "tienda01.jpg"
        },
    
        {
            id: 2,
            nombre: "Pedidos Personalizados y Envío a Domicilio",
            descripcion: "Selecciona tus productos favoritos y recíbelos en casa. Ofrecemos opciones personalizadas para pedidos semanales o por suscripción.",
            imagen: "tienda02.jpg"
        },
        {
            id: 3,
            nombre: "Promoción del Comercio Local",
            descripcion: "Apoya a los campesinos y productores agroindustriales de tu región comprando productos frescos y de calidad, directamente desde nuestra tienda virtual.",
            imagen: "tienda03.jpg"
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