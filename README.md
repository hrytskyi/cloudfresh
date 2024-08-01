## Part 3: Programming Skills

### 3.1. Simple Automation Script

#### Objective

Demonstrate basic programming skills.

#### Task

1.  **Write a script in Python or JavaScript that performs the following:**
       -   Fetch data from a public API (e.g., weather data).
       -   Process the data and store it in a file (e.g., JSON or CSV).
       -   Optionally, visualize the data in a simple chart (e.g., using a library like Matplotlib for Python or Chart.js for JavaScript).
#### Script
The script is written in Python and fetches exchange rate data from the Fixer API. It processes the data and saves it to both JSON and CSV files. The script also includes optional data visualization using the Matplotlib library.
#### How to Run the Script

1.  **Clone the Repository and Checkout the `task3` Branch:**
```
    git clone https://github.com/hrytskyi/cloudfresh.git
    cd cloudfresh
    git checkout task3 
 ```   
2.  **Install Dependencies:** Ensure you have `requests` and `matplotlib` libraries installed. You can install them using pip:
```
    pip install requests matplotlib
```    
3.  **Set Up the API Key:** Replace `"YOUR_ACCESS_KEY"` in the script with your actual Fixer API access key.
    
4.  **Run the Script:**
```
    python script.py
```
### Example Output Files

-   **exchange_rates.json:** Contains the raw exchange rate data fetched from the Fixer API.
-   **exchange_rates.csv:** Contains the processed exchange rate data in CSV format.

### Explanation of the Logic

1.  **Fetching Data:** The script sends a GET request to the Fixer API to fetch the latest exchange rates.
    
2.  **Processing Data:** The fetched data is processed and saved to `exchange_rates.json` and `exchange_rates.csv` files.
    
3.  **Visualizing Data:** The script uses Matplotlib to create a simple bar chart of the exchange rates for the first 10 currencies.
<img width="991" alt="image" src="https://github.com/user-attachments/assets/b8dbff74-f1fe-4a6f-8c51-29d07ebe0eba">
