document.addEventListener("DOMContentLoaded", () => {
  // Añadir eventos de escucha a los campos del formulario
  addFieldListeners();

  // Enlazar la función submitForm al evento de clic del botón de envío
  const submitButton = document.querySelector(".enviar");
  submitButton.addEventListener("click", submitForm); /* valida el envio */
});

// Función para añadir eventos de escucha a los campos del formulario
function addFieldListeners() {
  const form = document.querySelector(".form");
  form.querySelectorAll("input").forEach((input) => {
    const fieldName = input.name;

    input.addEventListener("input", () => {
      const fieldValue = input.value.trim();
      validateField(fieldName, fieldValue);
    });
  });
}

// Función para limpiar los mensajes de error de un campo específico
function clearFieldError(fieldName) {
  const field = document.querySelector(`input[name="${fieldName}"]`);
  const groupDiv = field.closest(".group"); // Encuentra el div padre con la clase 'group'
  const errorContainer = groupDiv.querySelector(".error-message");
  if (errorContainer) {
    errorContainer.remove();
    field.classList.remove("is-invalid");
  }

  // Elimina la clase extraError del div correspondiente si existe
  const extraDiv = document.querySelector(".extraError");
  if (extraDiv) {
    extraDiv.classList.remove("extraError");
  }
}

function validateField(fieldName, fieldValue) {
  clearFieldError(fieldName);

  if (fieldName === "email") {
    if (!fieldValue) {
      showFieldError(fieldName, "El campo email es obligatorio");
    } else if (!isValidEmail(fieldValue)) {
      showFieldError(fieldName, "Formato de correo electrónico inválido");
    }
  }

  if (fieldName === "password") {
    if (!fieldValue) {
      showFieldError(fieldName, "El campo contraseña es obligatorio");
    } else if (!isValidPassword(fieldValue)) {
      const extraDiv = document.querySelector(".div-enviar");
      extraDiv.classList.add("extraError");
      showFieldError(
        fieldName,
        "La contraseña debe tener al menos 8 caracteres y contener letras, números y símbolos"
      );
    }
  }
}

// Función para validar el formato de correo electrónico
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

// Función para validar el formato de contraseña
function isValidPassword(password) {
  const passwordRegex =
    /^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&.-])[A-Za-z\d@$!%*#?&.-]{8,}$/;
  return passwordRegex.test(password);
}

// Función para mostrar mensajes de error debajo de cada campo
function showFieldError(fieldName, errorMessage) {
  const field = document.querySelector(`input[name="${fieldName}"]`);
  const groupDiv = field.closest(".group"); // Encuentra el div padre con la clase 'group'
  let errorContainer = groupDiv.querySelector(".error-message");

  if (!errorContainer) {
    // Si no existe un div de error, créalo
    errorContainer = document.createElement("div");
    errorContainer.className = "error-message";
    groupDiv.appendChild(errorContainer); // Inserta el div de error dentro del div 'group'
  }

  // Actualiza el contenido del div de error con el mensaje de error
  errorContainer.innerHTML = errorMessage;

  // Agrega la clase 'is-invalid' al campo para resaltar el error
  field.classList.add("is-invalid");
  groupDiv.classList.add("is-invalid");
}

// Función para limpiar mensajes de error y clases inválidas
function clearErrors() {
  const errorMessages = document.querySelectorAll(".error-message");
  errorMessages.forEach((errorMessage) => errorMessage.remove());

  const fields = document.querySelectorAll("input");
  fields.forEach((field) => field.classList.remove("is-invalid"));

  // Elimina la clase extraError del div correspondiente si existe
  const extraDiv = document.querySelector(".extraError");
  if (extraDiv) {
    extraDiv.classList.remove("extraError");
  }
}

// Función para validar el formulario
function validateForm() {
  clearErrors();

  const userField = document.getElementById("email");
  const passwordField = document.getElementById("password");

  let isValid = true;

  // Validar campo de usuario
  const userValue = userField.value.trim();
  const userName = userField.name;
  if (!userValue) {
    isValid = false;
    showFieldError(userName, "El campo email es obligatorio");
  } else if (!isValidEmail(userValue)) {
    isValid = false;
    showFieldError(userName, "Formato de correo electrónico inválido");
  }

  // Validar campo de contraseña
  const passwordValue = passwordField.value.trim();
  const passwordName = passwordField.name;
  if (!passwordValue) {
    isValid = false;
    showFieldError(passwordName, "El campo contraseña es obligatorio");
  } else if (!isValidPassword(passwordValue)) {
    isValid = false;
    const extraDiv = document.querySelector(".div-enviars");
    extraDiv.classList.add("extraError");
    showFieldError(passwordName, "La contraseña debe tener al menos 8 caracteres y contener letras, números y símbolos");
  }

  return isValid;
}

/*=============== ENVIO DE FORMULARIO ===============*/
function submitForm(event) {
  event.preventDefault(); // Evitar que el formulario se envíe automáticamente

  if (validateForm()) {
    const form = document.querySelector(".form");
    const formData = new FormData(form);

    // Realizar la solicitud con fetch
    fetch(form.action, {
      method: form.method,
      body: formData,
      headers: {
        "X-Requested-With": "XMLHttpRequest", // Cabecera para indicar que es una petición AJAX
      },
    })
      .then((response) => {
        // Verificar si la respuesta es exitosa
        if (response.ok) {
          return response.json();
        } else {
          return response.json().then((data) => {
            // Devolver un error con los detalles
            throw new Error(data.error || "Error desconocido");
          });
        }
      })
      .then((data) => {
        // Manejar la respuesta exitosa del servidor
        Swal.fire({
          icon: "success",
          title: "¡Inicio de sesión exitoso!",
          customClass: {
            popup: "swal2-custom-popup", // Clase personalizada para la alerta
          },
          showConfirmButton: false,
          timer: 1500, // Cerrar automáticamente después de 1.5 segundos
        }).then(() => {
          // Redirigir al usuario según la respuesta del servidor
          if (data.redirect) {
            window.location.href = data.redirect;
          }
        });
      })
      .catch((error) => {
        // Manejar el error del servidor
        Swal.fire({
          icon: "error",
          title: "Error",
          text: error.message,
        });
      });
  } else {
    // Si el formulario no es válido, mostrar un mensaje de error
    Swal.fire({
      icon: "error",
      title: "Error",
      text: "Por favor, corrige los errores en el formulario antes de enviarlo.",
    });
    console.log("Formulario inválido. No se puede enviar.");
  }
}

/*=============== SHOW HIDDEN - PASSWORD ===============*/
function showHiddenPass(password, loginEye) {
  const input = document.getElementById(password),
    iconEye = document.getElementById(loginEye);

  iconEye.addEventListener("click", () => {
    // Change password to text
    if (input.type === "password") {
      // Switch to text
      input.type = "text";

      // Icon change
      iconEye.classList.add("fa-eye");
      iconEye.classList.remove("fa-eye-slash");
    } else {
      // Change to password
      input.type = "password";

      // Icon change
      iconEye.classList.remove("fa-eye");
      iconEye.classList.add("fa-eye-slash");
    }
  });
}

showHiddenPass("password", "login-eye");
