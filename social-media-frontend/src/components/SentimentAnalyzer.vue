<html lang="en">
	<head>
		<meta charset="UTF-8" />
		<title>Social Media Sentiment Analyzer</title>
		<link rel="stylesheet" href="styles.css" />
	</head>
	<body>
		<div id="app" class="container">
			<div class="sentiment-analyzer">
				<h1>Social Media Sentiment Analyzer</h1>

				<div class="input-section">
					<textarea
						id="sentiment-text"
						placeholder="Enter your text here..."
						rows="4"
					></textarea>
					<button id="analyze-btn">Analyze Sentiment</button>
				</div>

				<div id="result-section" class="result-section hidden">
					<div class="result-card">
						<h2>Analysis Results</h2>
						<div class="result-grid">
							<div class="result-item">
								<label>Sentiment</label>
								<div id="sentiment-result" class="result-value"></div>
							</div>
							<div class="result-item">
								<label>Polarity Score</label>
								<div id="polarity-result" class="result-value"></div>
							</div>
						</div>
						<div class="result-details">
							<label>Subjectivity</label>
							<div id="subjectivity-result" class="result-value"></div>
						</div>
					</div>
				</div>
			</div>
		</div>

		<script src="app.js"></script>
	</body>
</html>

<style>
body {
	font-family: Arial, sans-serif;
	background-color: #f4f4f4;
	margin: 0;
	padding: 20px;
	display: flex;
	justify-content: center;
}

.container {
	width: 100%;
	max-width: 600px;
}

.sentiment-analyzer {
	background-color: white;
	border-radius: 8px;
	box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
	padding: 30px;
}

h1 {
	text-align: center;
	color: #333;
	margin-bottom: 20px;
}

.input-section textarea {
	width: 100%;
	padding: 10px;
	border: 1px solid #ddd;
	border-radius: 4px;
	margin-bottom: 15px;
	resize: vertical;
}

.input-section button {
	width: 100%;
	padding: 10px;
	background-color: #007bff;
	color: white;
	border: none;
	border-radius: 4px;
	cursor: pointer;
	transition: background-color 0.3s;
}

.input-section button:hover {
	background-color: #0056b3;
}

.result-section {
	margin-top: 20px;
}

.result-card {
	background-color: #f8f9fa;
	border-radius: 8px;
	padding: 20px;
}

.result-grid {
	display: grid;
	grid-template-columns: 1fr 1fr;
	gap: 15px;
}

.result-item {
	background-color: white;
	border: 1px solid #e9ecef;
	border-radius: 4px;
	padding: 10px;
}

.result-item label,
.result-details label {
	font-weight: bold;
	color: #6c757d;
}

.result-value {
	margin-top: 5px;
	font-size: 18px;
}

.hidden {
	display: none;
}

.positive {
	color: green;
}
.negative {
	color: red;
}
.neutral {
	color: gray;
}
</style>

<!-- app.js -->
<script>
document.addEventListener("DOMContentLoaded", () => {
	const textArea = document.getElementById("sentiment-text");
	const analyzeBtn = document.getElementById("analyze-btn");
	const resultSection = document.getElementById("result-section");
	const sentimentResult = document.getElementById("sentiment-result");
	const polarityResult = document.getElementById("polarity-result");
	const subjectivityResult = document.getElementById("subjectivity-result");

	analyzeBtn.addEventListener("click", async () => {
		const text = textArea.value.trim();

		if (!text) {
			alert("Please enter some text");
			return;
		}

		try {
			const response = await fetch("http://localhost:5000/analyze", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify({ text }),
			});

			const result = await response.json();

			// Update result section
			sentimentResult.textContent =
				result.sentiment.charAt(0).toUpperCase() + result.sentiment.slice(1);
			sentimentResult.className = `result-value ${result.sentiment}`;

			polarityResult.textContent = `${(result.polarity * 100).toFixed(1)}%`;
			subjectivityResult.textContent = `${(result.subjectivity * 100).toFixed(
				1
			)}%`;

			resultSection.classList.remove("hidden");
		} catch (error) {
			console.error("Error:", error);
			alert("Failed to analyze sentiment");
		}
	});
});
</script>
