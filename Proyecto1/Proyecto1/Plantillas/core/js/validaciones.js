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
  document.getElementById("id01").addEventListener('submit', validarFormulario); 
});

function validarFormulario(evento) {
  evento.preventDefault();//prevenir envio
  var letra = document.getElementById('nombre').value.charAt(0);
  var usuario = document.getElementById('nombre').value;
  let msj = "";
  let entrar = false
  if(usuario.length == 0) {//validacion usuario
    alert('No has escrito nada en el usuario');
    return;
  }
  if(usuario.trim().length <4 || usuario.trim().length >7){
    msj+="El nombre no tiene la longitud válida, 4-7 caracteres<br>";
    entrar = true;
  }
  if (entrar){
    $("mensajes").html(msj);
  }
  else{
    $("mensajes").html("Formulario Enviado")
  }
  function esMayuscula(letra){
    return letra == letra.toUpperCase();
}
  
  //validacion password 
  var clave = document.getElementById('psw1').value;
  var clave2 = document.getElementById('psw2').value;
  if (4>clave.length>12) {
    if(clave !== clave2)
      alert('La clave no es valida');
      return;
  }
  this.submit();
}
var modal = document.getElementById('id01');
// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
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
