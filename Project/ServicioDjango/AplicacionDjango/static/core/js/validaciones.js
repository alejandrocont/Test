// Tabbed Menu
function openMenu(evt, menuName) {
  var i, x, tablinks;
  x = document.getElementsByClassName("menu");
  for (i = 0; i < x.length; i++) {
     x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
     tablinks[i].className = tablinks[i].className.replace(" w3-red", "");
  }
  document.getElementById(menuName).style.display = "block";
  evt.currentTarget.firstElementChild.className += " w3-red";
}
//validacion formulario 
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("registro").addEventListener('submit', validarFormulario); 
});

function validarFormulario(evento) {
  evento.preventDefault();//prevenir envio
  var nombre = document.getElementById("nombre").value;
  var email = document.getElementById("email").value;
  var password1 = document.getElementById("password1").value;
  var password2 = document.getElementById("password2").value;
  let warnings = ''
  let entrar = false;
  let regexEmail = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
  let regexPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}/
  parrafo.innerHTML = ''

  if (nombre.value.length < 6 ){
    warnings += '<p>El nombre debe tener al menos 6 caracteres</p>'
    entrar = true;
  }
  if (nombre.value.length > 15 ){
    warnings += '<p>El nombre debe tener menos de 15 caracteres</p>'
    entrar = true;
  }
  if (!regexEmail.test(email)){
    warnings += '<p>El email no es valido</p>'
    entrar = true;
  }
  if(password1.value != password2.value){
    warnings += '<p>Las contraseñas no coinciden</p>'
    entrar = true;
  if(!regexPassword.test(password1)){
    warnings += '<p>La contraseña debe tener al menos 8 caracteres, una mayuscula, una minuscula, un numero y un caracter especial</p>'
    entrar = true;
  }
}
if(entrar){
  parrafo.innerHTML = warnings;
}else{
  parrafo.innerHTML = '<p>Formulario enviado</p>';
} }

var modal = document.getElementById('id01');
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//validacion formulario 
document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("sesion").addEventListener('submit', validarFormulario); 
});

function validarFormulario(evento) {
  evento.preventDefault();//prevenir envio
  var nombre = document.getElementById("nombre").value;
  var contraseña = document.getElementById("contraseña").value;
  let warnings = ''
  let entrar = false;
  let regexPassword = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$@$!%*?&])[A-Za-z\d$@$!%*?&]{8,15}/
  parrafo.innerHTML = ''

  if (nombre.value.length < 6 ){
    warnings += '<p>El nombre debe tener al menos 6 caracteres</p>'
    entrar = true;
  }
  if (nombre.value.length > 15 ){
    warnings += '<p>El nombre debe tener menos de 15 caracteres</p>'
    entrar = true;
  }
  if(!regexPassword.test(contraseña)){
    warnings += '<p>La contraseña debe tener al menos 8 caracteres, una mayuscula, una minuscula, un numero y un caracter especial</p>'
    entrar = true;
  }
if(entrar){
  parrafo.innerHTML = warnings;
}
else{
  parrafo.innerHTML = '<p>Formulario enviado</p>';
} 
}







/*API REST

src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAB2fLqEcxJFE1bkTPKiXlKIj-6nBH8zts&callback=initMap"

if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(iniciarMapa);
}
function iniciarMapa(){
  var latitud = navigator.geolocation.getCurrentPosition.latitud
  var longitud = 70.6789547

  coordenadas = {
    lng: longitud,
    lat: latitud
  }
  generarMapa(coordenadas);
}
function generarMapa(coordenadas){
  var mapa = new google.maps.Map(document.getElementById('Map'),{
    zoom: 12,
    center: new google.maps.latLng(coordenadas.lat, coordenadas.lng)
  });
}*/
