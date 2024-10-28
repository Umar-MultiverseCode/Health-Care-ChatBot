

# 💬🤖 **Aetmaad Health Chatbot** 🩺💊 


Welcome to the **Aetmaad Health Chatbot**—your friendly assistant for personalized health recommendations and advice. This project provides users with a health-focused chatbot that interacts with users, collects essential health information, and suggests remedies available on the **Aetmaad** platform. It's built using Python and Flask, integrated with HTML, CSS, JavaScript, and SQLite for an interactive and seamless user experience.

## 🚀 **Features**

1. **User Information Form** 📋:
   - Collects basic user details like name, counselor's name, mobile number, age, height, weight, marital status, address, etc.
   - Redirects the user to the chatbot interface upon submission.

2. **Interactive Health Chatbot** 🤖:
   - Asks users about their symptoms, allergies, lifestyle, and current medications.
   - Suggests remedies and products based on the user’s responses and symptoms, such as:
     - Cough, Malaria, Constipation, Blood Pressure, Joint Pain, Ulcers, etc.
   - Recommends products only from the **Aetmaad** site, ensuring trusted and verified options.

3. **Product Recommendation System** 💊:
   - Provides detailed information on recommended products, including:
     - Product name, price, and a link to purchase.
     - Usage instructions and health benefits.

4. **Dynamic Conversation Management** 💬:
   - Stores each user conversation in a **SQLite** database for reference and analysis.
   - Tracks symptoms and responses to personalize future interactions.

5. **User-Friendly Interface** 🖥️:
   - Built using **Flask** with front-end support from HTML, CSS, and JavaScript for a smooth user experience.
   - Designed to be simple, interactive, and accessible.

## 🛠️ **Tech Stack**

- **Frontend**: HTML, CSS, JavaScript 🌐
- **Backend**: Python (Flask) 🐍
- **Database**: SQLite 🗃️

## 📂 **Project Setup**

Follow these steps to set up and run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Health-Care-ChatBot.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Health-Care-ChatBot.git
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS/Linux
   source venv/bin/activate
   ```

5. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

6. Run the application:
   ```bash
   python app.py
   ```

7. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

## 🧠 **How It Works**

1. **Form Submission** 📝:
   - The user fills out a form with their details, which are processed and stored.
   
2. **Chat Interaction** 💬:
   - The chatbot initiates a conversation based on the user’s symptoms and lifestyle.
   - The chatbot asks about allergies, current medication, and eating habits to provide accurate advice.

3. **Recommendation** 🔎:
   - Based on the user's symptoms, the bot suggests specific products with a link and price from the **Aetmaad** platform.
   - Example:
     - *"For joint pain, try Rumabil, available for ₹300 [here](https://aetmaad.co.in/product/rumabil)."*

4. **Database Management** 🗄️:
   - All conversations are saved in an SQLite database for future reference and insights.

## 📋 **Future Improvements**

- Adding more health conditions and expanding the product catalog.
- Integrating machine learning for improved diagnosis and personalized recommendations.
- Enhancing the user interface for a more engaging experience.

## 🎉 **Contributing**

We welcome contributions! Feel free to fork the repository, make enhancements, and submit a pull request. Let’s build a healthier future together! 🌱

## 📧 **Contact Us**

For queries or support, please reach out to [umarmulla7700@gmail.com](mailto:umarmulla7700@gmail.com).

---

