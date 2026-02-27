import { MapContainer, TileLayer, Marker, Polyline } from "react-leaflet";
import { useEffect, useState } from "react";
import "leaflet/dist/leaflet.css";

function App() {

  const [position, setPosition] = useState([0, 0]);
  const [trail, setTrail] = useState([]);

  useEffect(() => {

    const socket = new WebSocket("ws://127.0.0.1:8000/ws/iss/");

    socket.onmessage = (event) => {

      const data = JSON.parse(event.data);

      const newPosition = [data.latitude, data.longitude];

      setPosition(newPosition);

      setTrail(prev => [...prev, newPosition]);
    };

  }, []);

  return (
    <MapContainer center={[0, 0]} zoom={2} style={{ height: "100vh" }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
      />
      <Marker position={position} />
      <Polyline positions={trail} />
    </MapContainer>
  );
}

export default App;
