document.addEventListener("DOMContentLoaded", function () {
    var map = L.map('map').setView([5.690338844121654, -73.22773931589995], 9);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">Colombia - Boyacá</a> - Municipio Tuta'
}).addTo(map);

L.marker([5.690338844121654, -73.22773931589995 ]).addTo(map)
    .bindPopup("<b>Tuta - Boyacá</b> <br> Bosque de Tuta")
    .openPopup();


});