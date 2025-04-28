async function predictSegment() {
    const recency = document.getElementById('recency').value;
    const frequency = document.getElementById('frequency').value;
    const monetary = document.getElementById('monetary').value;

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({
            Recency: parseFloat(recency),
            Frequency: parseFloat(frequency),
            Monetary: parseFloat(monetary)
        })
    });

    const result = await response.json();
    document.getElementById('result').innerText = 
        `Tahmin Edilen Segment: ${result.Segment}`;
}
