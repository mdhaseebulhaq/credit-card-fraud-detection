async function analyzeTransaction() {

    const resultDiv = document.getElementById("result");

    // Get values from the form
    const transactionAmt =
        document.getElementById("TransactionAmt").value;

    const productCD =
        document.getElementById("ProductCD").value;

    const card4 =
        document.getElementById("card4").value;

    const card6 =
        document.getElementById("card6").value;

    const deviceType =
        document.getElementById("DeviceType").value;


    // Check transaction amount
    if (!transactionAmt) {
        resultDiv.innerHTML =
            "<p>Please enter a transaction amount.</p>";
        return;
    }


    // Show loading message
    resultDiv.innerHTML =
        "<p>🔍 AI is analyzing the transaction...</p>";


    // Create transaction data
    const transaction = {
        TransactionAmt: Number(transactionAmt),
        ProductCD: productCD,
        card4: card4,
        card6: card6,
        DeviceType: deviceType || null
    };


    try {

        // Send request to FastAPI
        const response = await fetch(
             "https://credit-card-fraud-detection-8-ayxm.onrender.com",
            {
                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify(transaction)
            }
        );


        const data = await response.json();


        // Handle API errors
        if (!response.ok) {
            resultDiv.innerHTML = `
                <p>
                    Error: ${JSON.stringify(data.detail)}
                </p>
            `;
            return;
        }


        // Determine CSS class
        let riskClass = data.risk_level.toLowerCase();


        // Display result
        resultDiv.innerHTML = `

            <div class="result-status ${riskClass}">
                ${data.result === "Fraud"
                    ? "⚠️ FRAUD DETECTED"
                    : "✅ TRANSACTION LOOKS SAFE"}
            </div>

            <div class="result-item">
                <strong>Prediction:</strong>
                ${data.result}
            </div>

            <div class="result-item">
                <strong>Fraud Probability:</strong>
                ${data.fraud_probability}%
            </div>

            <div class="result-item">
                <strong>Risk Level:</strong>
                <span class="${riskClass}">
                    ${data.risk_level}
                </span>
            </div>
        `;

    } catch (error) {

        console.error(error);

        resultDiv.innerHTML = `
            <p>
                ❌ Unable to connect to the Fraud Detection API.
            </p>
        `;
    }
}