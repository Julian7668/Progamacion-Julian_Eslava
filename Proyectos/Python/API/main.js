const API_BASE = "http://localhost:8000";

function showMessage(text, type = "success") {
  const messageDiv = document.getElementById("message");
  messageDiv.innerHTML = `<div class="message ${type}">${text}</div>`;
  setTimeout(() => {
    messageDiv.innerHTML = "";
  }, 3000);
}

async function createUser() {
  const name = document.getElementById("name").value;
  const age = parseInt(document.getElementById("age").value);

  if (!name || !age) {
    showMessage("Por favor completa todos los campos", "error");
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/users`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ name, age }),
    });

    const data = await response.json();

    if (response.ok) {
      showMessage(`Usuario ${name} creado exitosamente!`);
      document.getElementById("name").value = "";
      document.getElementById("age").value = "";
      loadUsers();
    } else {
      showMessage("Error al crear usuario", "error");
    }
  } catch (error) {
    showMessage("Error de conexión con la API", "error");
    console.error("Error:", error);
  }
}

async function loadUsers() {
  try {
    const response = await fetch(`${API_BASE}/users`);
    const data = await response.json();

    const usersList = document.getElementById("usersList");

    if (data.users && data.users.length > 0) {
      usersList.innerHTML = data.users
        .map(
          (user, index) => `
<div class="user-item">
    <div class="user-info">
        <strong>${user.name}</strong>
        <span>Edad: ${user.age}</span>
        <span>ID: ${user.id || index + 1}</span>
    </div>
    <div class="user-actions">
        <button class="delete-btn" onclick="deleteUser(${
          user.id || index + 1
        })">
            Eliminar
        </button>
    </div>
</div>
`
        )
        .join("");
    } else {
      usersList.innerHTML = "<p>No hay usuarios registrados</p>";
    }
  } catch (error) {
    showMessage("Error al cargar usuarios", "error");
    console.error("Error:", error);
  }
}

async function deleteUser(userId) {
  if (!confirm("¿Estás seguro de eliminar este usuario?")) {
    return;
  }

  try {
    const response = await fetch(`${API_BASE}/users/${userId}`, {
      method: "DELETE",
    });

    if (response.ok) {
      showMessage("Usuario eliminado exitosamente");
      loadUsers();
    } else {
      showMessage("Error al eliminar usuario", "error");
    }
  } catch (error) {
    showMessage("Error de conexión", "error");
  }
}

// Cargar usuarios al iniciar la página
window.onload = function () {
  loadUsers();
};
