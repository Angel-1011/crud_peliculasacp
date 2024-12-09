const header = document.querySelector("header");

window.addEventListener("scroll", function (){
    header.classList.toggle("sticky", this.window.scrollY > 60)
})

/* agregrar un evento click al elemento de clase btn

document.querySelector('.btn').addEventListener("click", function(){
    alert('¡Contactando con desarrollador!')
})

// agregrar un evento click a cada uno de los elementos encontrados de clase .btn
document.querySelectorAll('.btn').forEach(function(button){
    button.addEventListener('click', function(){
        alert('¡Contactando con desarrollador!')
    })
})*/

// funcion para el boton 'Reserva'
document.getElementById('btn-Reserva').addEventListener('click', function(){
    alert('¡Contactando con el proveedor espere un momento!')
})

// funcion para el boton 'Oferta'
document.getElementById('btn-Oferta').addEventListener('click', function(){
    alert('¡Su registro a sido guardado!')
})


document.querySelectorAll('.navbar a[href^="#"]').forEach(function(enlace){
    enlace.addEventListener('click', function(e){
        e.preventDefault();
        //Desplazamiento suave
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        })

    })
})

// cambiar las imagenes de fondo de la sección home

const imagenesAcp = [
    
    '/static/peliculas/img/viajes1.jpg',
    '/static/peliculas/img/botes.jpg',
    '/static/peliculas/img/comida.jpg',
    '/static/peliculas/img/esqui.jpg',
    '/static/peliculas/img/hospedajes.jpg',
    '/static/peliculas/img/senderismo.jpg'
];

const homeSection = document.querySelector('.home');
const intervalo = 4000;  // 4000 ms = 4s

let indiceImagen = 0;

function cambiarFondo(){
    //alert('hola')
    homeSection.style.backgroundImage = `linear-gradient(45deg, rgb(115, 232, 223, 0.6), rgba(239, 240, 238, 0.3)),url(${imagenesAcp[indiceImagen]})`;
     indiceImagen = (indiceImagen + 1) % imagenesAcp.length;
} 

setInterval(cambiarFondo, intervalo)

// Menú para pantallas pequeñas
let menu = document.querySelector('#menu-icon');
let navbar = document.querySelector('.navbar'); 
let enlaces = document.querySelectorAll('.navbar a');

menu.onclick = () => {
    navbar.classList.toggle('open')
    menu.classList.toggle('bx-x')
}

enlaces.forEach(link => {
    link.onclick = () => {
        navbar.classList.remove('open')
        menu.classList.remove('bx-x')
    }
})


  var typed = new Typed('#typed', {
  strings: ['Hospedajes de lujo', 'Encuentra los lugares mas hermosos', 'No pierdas esta gran oportunidad'],
  typeSpeed: 50,
  loop: "true",
  backSpeed: 20,
  });
