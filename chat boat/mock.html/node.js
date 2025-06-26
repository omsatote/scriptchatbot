import React, { useState } from "react";

function App() {
  const [chat, setChat] = useState([]);
  const [input, setInput] = useState("");

  const sendMessage = async () => {
    if (!input.trim()) return;

    setChat([...chat, { role: "user", text: input }]);
    const res = await fetch("http://localhost:3000/interview", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });

    const data = await res.json();
    setChat((prev) => [...prev, { role: "bot", text: data.reply }]);
    setInput("");
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>🎤 AI Interview</h1>
      <div style={{ marginBottom: "1rem", height: "300px", overflowY: "scroll", border: "1px solid #ccc", padding: "1rem" }}>
        {chat.map((msg, i) => (
          <div key={i} style={{ marginBottom: "10px", textAlign: msg.role === "user" ? "right" : "left" }}>
            <strong>{msg.role === "user" ? "You" : "Bot"}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <input
        type="text"
        value={input}
        placeholder="Type your answer..."
        onChange={(e) => setInput(e.target.value)}
        onKeyDown={(e) => e.key === "Enter" && sendMessage()}
        style={{ padding: "0.5rem", width: "70%" }}
      />
      <button onClick={sendMessage} style={{ padding: "0.5rem", marginLeft: "1rem" }}>
        Send
      </button>
    </div>
  );
}

export default App;
