// ==============================
// COPY RESPONSE
// ==============================

function copyResponse() {

    const text =
        document.getElementById(
            "responseText"
        ).innerText;

    navigator.clipboard.writeText(text);

    alert("✅ Response copied!");
}

// ==============================
// OPEN REDDIT
// ==============================

function openReddit() {

    window.open(
        "https://www.reddit.com",
        "_blank"
    );
}

// ==============================
// OPEN QUORA
// ==============================

function openQuora() {

    window.open(
        "https://www.quora.com",
        "_blank"
    );
}

// ==============================
// OPEN DEV.TO
// ==============================

function openDevto() {

    window.open(
        "https://dev.to",
        "_blank"
    );
}
