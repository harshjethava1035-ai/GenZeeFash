import streamlit as st
import pandas as pd
from PIL import Image
import base64

# Page configuration
st.set_page_config(
    page_title="GenZeeFash - Trendy Clothing for Gen Z",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #FF6B6B;
        text-align: center;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .category-header {
        font-size: 2rem;
        color: #4ECDC4;
        margin: 2rem 0 1rem 0;
    }
    .product-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .price-tag {
        font-size: 1.5rem;
        color: #FFE66D;
        font-weight: bold;
    }
    .sidebar .stSelectbox {
        background-color: #f0f2f6;
    }
    .stButton > button {
        background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.5rem 2rem;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Sample product data
products_data = {
    "Boys Jeans": {
        "Bell Bottom Jeans": [
            {"name": "Retro Bell Bottom - Blue", "price": "₹2,999", "description": "Classic 70s inspired bell bottom jeans with authentic vintage wash"},
            {"name": "Black Bell Bottom Denim", "price": "₹3,299", "description": "Sleek black bell bottom jeans perfect for parties and casual outings"},
            {"name": "Light Wash Bell Bottom", "price": "₹2,799", "description": "Light blue bell bottom jeans with distressed detailing"}
        ],
        "Cargo Jeans": [
            {"name": "Multi-Pocket Cargo Jeans", "price": "₹3,499", "description": "Functional cargo jeans with 8 pockets and utility straps"},
            {"name": "Olive Green Cargo Denim", "price": "₹3,799", "description": "Military-inspired olive green cargo jeans with reinforced knees"},
            {"name": "Black Tactical Cargo", "price": "₹4,199", "description": "Premium black cargo jeans with tactical styling"}
        ],
        "Loose Fit Jeans": [
            {"name": "Relaxed Fit Blue Jeans", "price": "₹2,499", "description": "Comfortable loose fit jeans perfect for everyday wear"},
            {"name": "Oversized Denim", "price": "₹2,899", "description": "Trendy oversized jeans with a relaxed streetwear vibe"},
            {"name": "Baggy Fit Vintage Wash", "price": "₹3,199", "description": "90s inspired baggy jeans with authentic vintage treatment"}
        ],
        "Straight Fit Jeans": [
            {"name": "Classic Straight Leg", "price": "₹2,299", "description": "Timeless straight fit jeans in classic indigo wash"},
            {"name": "Dark Wash Straight Jeans", "price": "₹2,699", "description": "Sophisticated dark wash straight jeans for smart casual looks"},
            {"name": "Raw Denim Straight", "price": "₹3,999", "description": "Premium raw denim straight jeans that age beautifully"}
        ]
    },
    "Boys Tops": [
        {"name": "GenZ Graphic Tee", "price": "₹999", "description": "Trendy graphic t-shirt with bold GenZ prints"},
        {"name": "Oversized Hoodie", "price": "₹2,499", "description": "Comfortable oversized hoodie perfect for layering"},
        {"name": "Vintage Band Tee", "price": "₹1,299", "description": "Authentic vintage band t-shirt with distressed finish"},
        {"name": "Striped Long Sleeve", "price": "₹1,599", "description": "Classic striped long sleeve shirt in multiple colors"}
    ],
    "Girls Jeans": {
        "Bell Bottom Jeans": [
            {"name": "Floral Bell Bottom", "price": "₹3,199", "description": "Feminine bell bottom jeans with subtle floral embroidery"},
            {"name": "High Waist Bell Bottom", "price": "₹3,499", "description": "Flattering high-waisted bell bottom jeans"},
            {"name": "Pastel Bell Bottom", "price": "₹2,999", "description": "Soft pastel colored bell bottom jeans"}
        ],
        "Cargo Jeans": [
            {"name": "Pink Cargo Jeans", "price": "₹3,299", "description": "Trendy pink cargo jeans with feminine touches"},
            {"name": "Slim Cargo Denim", "price": "₹3,699", "description": "Slim-fit cargo jeans that combine style with functionality"},
            {"name": "White Cargo Pants", "price": "₹3,899", "description": "Fresh white cargo jeans perfect for summer"}
        ],
        "Loose Fit Jeans": [
            {"name": "Boyfriend Jeans", "price": "₹2,799", "description": "Relaxed boyfriend jeans with rolled cuffs"},
            {"name": "Mom Jeans", "price": "₹2,599", "description": "Trendy high-waisted mom jeans with tapered legs"},
            {"name": "Distressed Loose Fit", "price": "₹3,099", "description": "Edgy distressed loose fit jeans"}
        ],
        "Straight Fit Jeans": [
            {"name": "Mid-Rise Straight", "price": "₹2,399", "description": "Versatile mid-rise straight jeans"},
            {"name": "Skinny Straight", "price": "₹2,699", "description": "Modern skinny straight jeans with stretch"},
            {"name": "High Waist Straight", "price": "₹2,899", "description": "Flattering high-waisted straight jeans"}
        ]
    },
    "Girls Tops": [
        {"name": "Crop Top Collection", "price": "₹899", "description": "Trendy crop tops in various colors and patterns"},
        {"name": "Oversized Tee", "price": "₹1,199", "description": "Comfortable oversized t-shirts perfect for casual wear"},
        {"name": "Floral Blouse", "price": "₹1,799", "description": "Elegant floral blouse for special occasions"},
        {"name": "Denim Jacket", "price": "₹2,999", "description": "Classic denim jacket that goes with everything"}
    ]
}

# Initialize session state for cart
if 'cart' not in st.session_state:
    st.session_state.cart = []

# Header
st.markdown('<h1 class="main-header">🛍️ GenZeeFash</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Trendy Clothing for the New Generation</p>', unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
category = st.sidebar.selectbox(
    "Choose Category",
    ["Home", "Boys Jeans", "Boys Tops", "Girls Jeans", "Girls Tops", "Cart", "About Us"]
)

# Sidebar filters
if category in ["Boys Jeans", "Girls Jeans"]:
    st.sidebar.subheader("Filters")
    price_range = st.sidebar.slider("Price Range (₹)", 1000, 5000, (2000, 4000))
    size = st.sidebar.multiselect("Size", ["S", "M", "L", "XL", "XXL"], default=["M", "L"])

# Function to add to cart
def add_to_cart(item_name, price):
    st.session_state.cart.append({"name": item_name, "price": price})
    st.success(f"Added {item_name} to cart!")

# Function to display products
def display_products(products, category_name):
    if isinstance(products, dict):
        for subcategory, items in products.items():
            st.markdown(f'<h3 class="category-header">{subcategory}</h3>', unsafe_allow_html=True)
            cols = st.columns(3)
            for idx, product in enumerate(items):
                with cols[idx % 3]:
                    st.markdown(f"""
                    <div class="product-card">
                        <h4>{product['name']}</h4>
                        <p class="price-tag">{product['price']}</p>
                        <p>{product['description']}</p>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button(f"Add to Cart", key=f"{category_name}_{subcategory}_{idx}"):
                        add_to_cart(product['name'], product['price'])
    else:
        cols = st.columns(3)
        for idx, product in enumerate(products):
            with cols[idx % 3]:
                st.markdown(f"""
                <div class="product-card">
                    <h4>{product['name']}</h4>
                    <p class="price-tag">{product['price']}</p>
                    <p>{product['description']}</p>
                </div>
                """, unsafe_allow_html=True)
                if st.button(f"Add to Cart", key=f"{category_name}_{idx}"):
                    add_to_cart(product['name'], product['price'])

# Main content based on category selection
if category == "Home":
    st.markdown("## Welcome to GenZeeFash! 🎉")
    st.write("Your one-stop destination for trendy clothing that speaks to the new generation.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 👦 For Boys")
        st.write("- Bell Bottom Jeans")
        st.write("- Cargo Jeans")
        st.write("- Loose Fit & Straight Fit")
        st.write("- Trendy Tops & T-shirts")
    
    with col2:
        st.markdown("### 👧 For Girls")
        st.write("- Stylish Bell Bottoms")
        st.write("- Fashion Cargo Jeans")
        st.write("- Comfortable Fits")
        st.write("- Chic Tops & Blouses")
    
    st.markdown("---")
    st.markdown("### Why Choose GenZeeFash?")
    st.write("✨ Latest fashion trends")
    st.write("🌟 High-quality materials")
    st.write("💰 Affordable prices")
    st.write("🚚 Fast delivery")

elif category == "Boys Jeans":
    st.markdown('<h2 class="category-header">Boys Jeans Collection</h2>', unsafe_allow_html=True)
    display_products(products_data["Boys Jeans"], "Boys Jeans")

elif category == "Boys Tops":
    st.markdown('<h2 class="category-header">Boys Tops Collection</h2>', unsafe_allow_html=True)
    display_products(products_data["Boys Tops"], "Boys Tops")

elif category == "Girls Jeans":
    st.markdown('<h2 class="category-header">Girls Jeans Collection</h2>', unsafe_allow_html=True)
    display_products(products_data["Girls Jeans"], "Girls Jeans")

elif category == "Girls Tops":
    st.markdown('<h2 class="category-header">Girls Tops Collection</h2>', unsafe_allow_html=True)
    display_products(products_data["Girls Tops"], "Girls Tops")

elif category == "Cart":
    st.markdown('<h2 class="category-header">Your Shopping Cart</h2>', unsafe_allow_html=True)
    
    if st.session_state.cart:
        for idx, item in enumerate(st.session_state.cart):
            col1, col2, col3 = st.columns([3, 2, 1])
            with col1:
                st.write(f"**{item['name']}**")
            with col2:
                st.write(f"**{item['price']}**")
            with col3:
                if st.button("Remove", key=f"remove_{idx}"):
                    st.session_state.cart.pop(idx)
                    st.rerun()
        
        st.markdown("---")
        total_items = len(st.session_state.cart)
        st.write(f"**Total Items: {total_items}**")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Clear Cart", type="secondary"):
                st.session_state.cart = []
                st.rerun()
        with col2:
            if st.button("Proceed to Checkout", type="primary"):
                st.success("Thank you for your order! We'll contact you soon for payment and delivery details.")
    else:
        st.write("Your cart is empty. Start shopping to add items!")

elif category == "About Us":
    st.markdown('<h2 class="category-header">About GenZeeFash</h2>', unsafe_allow_html=True)
    st.write("""
    GenZeeFash is a fashion-forward clothing brand designed specifically for Generation Z. 
    We understand the unique style preferences of today's youth and offer trendy, comfortable, 
    and affordable clothing options.
    
    **Our Mission:** To provide high-quality, stylish clothing that allows young people to 
    express their individuality and stay on-trend.
    
    **Contact Information:**
    - 📧 Email: contact@genzeefash.com
    - 📱 Phone: +91 12345 67890
    - 📍 Address: Fashion Street, Mumbai, India
    
    **Follow Us:**
    - Instagram: @genzeefash
    - Twitter: @genzeefash
    - Facebook: GenZeeFash Official
    """)

# Footer
st.markdown("---")
st.markdown(
    '<p style="text-align: center; color: #666; font-size: 0.9rem;">© 2024 GenZeeFash - All Rights Reserved</p>',
    unsafe_allow_html=True
)

