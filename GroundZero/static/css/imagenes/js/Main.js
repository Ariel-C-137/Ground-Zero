$(document).ready(function () {
  $("#form").submit(function (event) {
    var isValid = true;

    // Validar el campo Nombre
    if ($("#nombre").val().trim() == "") {
      alert("El campo Nombre está vacío");
      isValid = false;
    }

    // Validar el campo Teléfono
    if ($("#telefono").val().trim() == "") {
      alert("El campo Teléfono está vacío");
      isValid = false;
    }

    // Validar el campo Correo
    if ($("#correo").val().trim() == "") {
      alert("El campo Correo está vacío");
      isValid = false;
    }

    // Validar el campo Mensaje
    if ($("#mensaje").val().trim() == "") {
      alert("El campo Mensaje está vacío");
      isValid = false;
    }

    // Si no es válido, prevenir el envío del formulario
    if (!isValid) {
      event.preventDefault();
    }
  });
  if (document.getElementById("btn-facebook")) {
    var modalFacebook = document.getElementById("modal-facebook");
    var buttonFacebook = document.getElementById("btn-facebook");
    var spanFacebook = document.getElementById("close-facebook");
    var bodyFacebook = document.getElementById("body");

    buttonFacebook.onclick = function () {
      modalFacebook.style.display = "block";
      bodyFacebook.style.position = "static";
      bodyFacebook.style.height = "100%";
      bodyFacebook.style.overflow = "hidden";
    };
    spanFacebook.onclick = function () {
      modalFacebook.style.display = "none";
    };
  }
  if (document.getElementById("btn-instagram")) {
    var modalInstagram = document.getElementById("modal-instagram");
    var buttonInstagram = document.getElementById("btn-instagram");
    var spanInstagram = document.getElementById("close-instagram");
    var bodyInstagram = document.getElementById("body");

    buttonInstagram.onclick = function () {
      modalInstagram.style.display = "block";
      bodyInstagram.style.position = "static";
      bodyInstagram.style.height = "100%";
      bodyInstagram.style.overflow = "hidden";
    };
    spanInstagram.onclick = function () {
      modalInstagram.style.display = "none";
    };
  }
  if (document.getElementById("btn-twitter")) {
    var modalTwitter = document.getElementById("modal-twitter");
    var buttonTwitter = document.getElementById("btn-twitter");
    var spanTwitter = document.getElementById("close-twitter");
    var bodyTwitter = document.getElementById("body");

    buttonTwitter.onclick = function () {
      modalTwitter.style.display = "block";
      bodyTwitter.style.position = "static";
      bodyTwitter.style.height = "100%";
      bodyTwitter.style.overflow = "hidden";
    };
    spanTwitter.onclick = function () {
      modalTwitter.style.display = "none";
    };
  }
  if (document.getElementById("btn-youtube")) {
    var modalYoutube = document.getElementById("modal-youtube");
    var buttonYoutube = document.getElementById("btn-youtube");
    var spanYoutube = document.getElementById("close-youtube");
    var bodyYoutube = document.getElementById("body");

    buttonYoutube.onclick = function () {
      modalYoutube.style.display = "block";
      bodyYoutube.style.position = "static";
      bodyYoutube.style.height = "100%";
      bodyYoutube.style.overflow = "hidden";
    };
    spanYoutube.onclick = function () {
      modalYoutube.style.display = "none";
    };
  }
});
