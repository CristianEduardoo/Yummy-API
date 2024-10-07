document.addEventListener("DOMContentLoaded", function () {
  // Selecciona el botón "Agregar"
  let addButton = document.querySelector(".addlink");

  // Define el límite máximo desde una variable global
  const maxItems = 5;

  // Asegúrate de que el botón existe antes de proceder
  if (!addButton) {
    console.warn("El botón de agregar no se encuentra en la página.");
    return;
  }

  // Realiza una solicitud AJAX para obtener el número actual de elementos (por ejemplo, de Entrantes)
  fetch("/api/v1/entrantes/")
    .then((response) => response.json())
    .then((data) => {
      let currentItems = data.length;

      if (currentItems >= maxItems) {
        // Cambia el estilo del botón
        addButton.classList.add("disabled");
        addButton.style.backgroundColor = "#FF6347"; // Cambia el color del botón
        addButton.style.pointerEvents = "none"; // Evita que sea clickeable

        // Usa SweetAlert para mostrar un mensaje cuando el usuario intente hacer clic
        addButton.addEventListener("click", function (event) {
          event.preventDefault(); // Evita que el enlace funcione
          Swal.fire({
            icon: "warning",
            title: "Límite alcanzado",
            text:
              "No puedes agregar más elementos, has alcanzado el límite máximo de " +
              maxItems +
              ".",
          });
        });
      }
    })
    .catch((error) => {
      console.error("Error al obtener el número de elementos:", error);
    });
});
