# 📌 AI ETF Investment Advisor

🔍 A simple AI-powered tool to recommend the best ETF based on your risk level.
*Note: While it’s called “AI,” the tool uses historical performance metrics to guide its suggestions*

---

## 🚀 Live App  
👉 **Try it here:** [AI ETF Investment Advisor](https://ai-investing-etf.streamlit.app/)  

---

## 💡 How It Works
1️⃣ **Select your risk level** (Low, Medium, High).  
2️⃣ **Get the best ETF recommendation** based on the **Sharpe Ratio** (a measure of risk-adjusted return).  
3️⃣ **Want another ETF?** Click **"Check Another ETF"** to see a different option.  
4️⃣ **Reset anytime** with **"Reset Selection"**.

---

## 📊 ETF Selection Criteria
The tool evaluates ETFs on:
- **Sharpe Ratio** – A higher ratio indicates better risk-adjusted returns.
- **Volatility** – Measures the risk or variability in ETF returns.
- **Annual Return** – Gives an idea of potential earnings over the year.

---

## 🔍 What is the Sharpe Ratio?
📌 **Formula:**  
\[
\text{Sharpe Ratio} = \frac{\text{Annual Return} - \text{Risk-Free Rate}}{\text{Volatility}}
\]

📈 **Higher Sharpe Ratio → Better risk-adjusted return.**  
A high Sharpe Ratio means the investment provides better returns for the amount of risk taken.

---

## 📬 Contact
💬 Have feedback or questions? Feel free to reach out on **GitHub**!

🚀 **Happy Investing! 🎯**

---

## 🔧 Setup & Run Locally

### 1️⃣ Clone the Repository
git clone https://github.com/aoifegaughan5/ai-investing-etf.git
cd ai-investing-etf

---
### 2️⃣ Install Dependencies
pip install -r requirements.txt

---
### 3️⃣ Fetch ETF Data
python grab_data.py

---
### 4️⃣ Run the Streamlit App
streamlit run streamlit_app.py
