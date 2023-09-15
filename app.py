import streamlit as st
import pandas as pd
import base64
from io import BytesIO
# Import your scraping functions
from flipkart_scraper import scrape_flipkart
from bigbasket_scraper import scrape_bigbasket
from jiomart_scraper import scrape_jiomart

# Set the app's background color and text color
st.markdown(
    """
    <style>
    body {
        background-color: #f4f4f4;
        color: #333;
    }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])

# Center the logo image
with col2:
    st.image("logo1.png", width=400,)
    


# Define the Streamlit app layout
st.title("E-commerce Data Scraper (EC-DS)")
st.header("🌟Welcome to EC-DS 🌟")
st.write("Enter the details in the sidebar to scrape data from E-commerce sites.")

# Add colorful tips in a separate section
st.header("🌟 Tips & Information 🌟")
st.markdown("- Select an E-commerce site and enter a product name to start scraping.", unsafe_allow_html=True)
st.markdown("- Use 'All of the Above' to scrape data from all three sites.", unsafe_allow_html=True)
st.markdown("- Ensure that your search term is specific for better results.", unsafe_allow_html=True)
st.markdown("- Note that the app is in its development stage and so the accuracy might be low.", unsafe_allow_html=True)

# Sidebar for user input with a colorful header
st.sidebar.markdown(
    """
    <div style='background-color: #42b883; padding: 10px; color: white; font-size: 18px; border-radius: 5px;'>
    User Input
    </div>
    """,
    unsafe_allow_html=True
)

ecommerce_site = st.sidebar.radio("Select E-commerce Site", ("Flipkart", "BigBasket", "JioMart", "All of the Above"))
product_name = st.sidebar.text_input("Enter Product Name")

if st.button("Fetch Data"):
    if not product_name:
        st.warning("Please enter a product name.")
    elif(ecommerce_site != "All of the Above"):
        if ecommerce_site == "Flipkart":
            data = scrape_flipkart(product_name)
        elif ecommerce_site == "BigBasket":
            data = scrape_bigbasket(product_name)
        elif ecommerce_site == "JioMart":
            data = scrape_jiomart(product_name)
        if data:
            # Convert the scraped data to a DataFrame
            data_df = pd.DataFrame(data)

            # Display the scraped data as a table
            st.subheader("📊 Scraped Data 📊")
            st.write(data_df)
             # Allow users to download the data as an Excel file
            st.subheader("Download Data")
            excel_file = BytesIO()
            with pd.ExcelWriter(excel_file, engine='xlsxwriter', mode='xlsx', datetime_format='yyyy-mm-dd') as writer:
                data_df.to_excel(writer, index=False)
            excel_file.seek(0)
            b64 = base64.b64encode(excel_file.read()).decode()
            href = f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="scraped_data.xlsx">Download as Excel</a>'
            st.markdown(href, unsafe_allow_html=True)
            
        else:
            st.error("An error occurred while fetching data. Please try again later.")
    else:
        data1 = pd.DataFrame(scrape_flipkart(product_name))
        data2 = pd.DataFrame(scrape_bigbasket(product_name))
        data3 = pd.DataFrame(scrape_jiomart(product_name))
        st.subheader("📊 Flipkart Data 📊")
        st.write(data1)
        st.subheader("📊 BigBasket Data 📊")
        st.dataframe(data2, height=400)
        st.subheader("📊 JioMart Data 📊")
        st.dataframe(data3, height=400)

# Run the Streamlit app with 'streamlit run app.py'
