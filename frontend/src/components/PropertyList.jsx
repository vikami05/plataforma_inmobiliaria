import { useEffect, useState } from "react";
import api from "../services/api";

function PropertyList() {
  const [properties, setProperties] = useState([]);

  useEffect(() => {
    api
      .get("properties/")
      .then((res) => setProperties(res.data))
      .catch((err) => console.error("Error al cargar propiedades:", err));
  }, []);

  return (
    <div style={{ marginTop: "2rem" }}>
      <h2>🏠 Propiedades disponibles</h2>
      {properties.length === 0 ? (
        <p>No hay propiedades cargadas aún.</p>
      ) : (
        <ul>
          {properties.map((p) => (
            <li key={p.id}>
              <strong>{p.title}</strong> — {p.city} — ${p.price}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default PropertyList;
