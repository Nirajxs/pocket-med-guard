const API_URL = "http://127.0.0.1:8000/message";

const sendBtn = document.getElementById("send");
const textBox = document.getElementById("text");
const messages = document.getElementById("messages");

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.classList.add("msg", sender);

    // 🔥 FIX: Render emojis + bold + newlines properly
    div.innerHTML = text.replace(/\n/g, "<br>");

    messages.appendChild(div);
    messages.scrollTop = messages.scrollHeight;
}

sendBtn.onclick = async () => {
    const text = textBox.value.trim();
    if (text === "") return;

    addMessage(text, "user");
    textBox.value = "";

    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ message: text })
        });

        const data = await response.json();

        // 🌟 HUMAN STYLE RESPONSE SHOW
        addMessage(data.reply, "bot");

    } catch (error) {
        addMessage("<b>⚠ Backend se connection me error aaya!</b>", "bot");
    }
};

textBox.addEventListener("keypress", (e) => {
    if (e.key === "Enter") sendBtn.onclick();
});
