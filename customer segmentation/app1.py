import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# --- Page Configuration ---
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🎯",
    layout="wide"
)

# --- Custom CSS Styling & Visual Corrections ---
st.markdown("""
<style>
    /* Main Page Background (Darker Slate Gray for contrast) */
    .stApp {
        background-color: #cbd5e1;
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background-color: #0f172a;
    }
    [data-testid="stSidebar"] * {
        color: #f1f5f9 !important;
    }
    
    /* File Uploader Contrast Fix for Dark Sidebar */
    [data-testid="stFileUploader"] {
        background-color: #1e293b !important;
        border: 2px dashed #475569 !important;
        border-radius: 10px !important;
        padding: 12px !important;
    }
    [data-testid="stFileUploader"] section {
        background-color: #1e293b !important;
    }
    [data-testid="stFileUploader"] section * {
        color: #f8fafc !important;
    }
    [data-testid="stFileUploader"] button {
        background-color: #3b82f6 !important;
        color: #ffffff !important;
        border-radius: 6px !important;
        border: none !important;
    }
    [data-testid="stFileUploader"] button * {
        color: #ffffff !important;
    }

    /* Metric Card Custom Backgrounds */
    div[data-testid="stMetric"] {
        background: #ffffff;
        border: 1px solid #94a3b8;
        border-radius: 12px;
        padding: 16px 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.08);
    }
    
    /* Title Banners */
    .header-box {
        background: linear-gradient(135deg, #1d4ed8 0%, #1e40af 100%);
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 24px;
        box-shadow: 0 4px 12px rgba(30, 64, 175, 0.25);
    }
    .header-box h1 {
        color: white !important;
        margin: 0;
        font-size: 2rem;
    }
    .header-box p {
        color: #e0f2fe !important;
        margin: 6px 0 0 0;
    }
    
    /* Content Containers & Plotly Wrapper Styling */
    .table-container {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        border: 1px solid #94a3b8;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.06);
        margin-bottom: 20px;
    }
    
    /* Global Dataframe Container Styling */
    div[data-testid="stDataFrame"] {
        background-color: #ffffff;
        border-radius: 8px;
        padding: 8px;
        border: 1px solid #cbd5e1;
    }

    /* Plotly Chart Container Styling */
    div[data-testid="stPlotlyChart"] {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 12px;
        border: 1px solid #94a3b8;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.06);
    }
    
    /* Section Headers */
    h2, h3 {
        color: #0f172a;
    }
</style>
""", unsafe_allow_html=True)

# --- Feature Definitions for customer_segmentation_1000.csv ---
FEATURE_COLS = [
    'Age', 'AnnualIncome', 'SpendingScore', 'PurchaseFrequency',
    'AvgPurchaseAmount', 'TotalPurchaseValue', 'OnlinePurchasePercentage',
    'RecencyDays', 'DiscountUsagePercentage', 'SatisfactionScore'
]

CAT_COLS = ['Gender', 'PreferredCategory', 'Location', 'MembershipLevel']

# --- Helper Functions with Caching ---
@st.cache_data
def load_data(file):
    df = pd.read_csv(file)
    df = df.dropna().drop_duplicates()
    return df

@st.cache_data
def run_clustering(df, k=3):
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df[FEATURE_COLS])
    
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(scaled_data)
    
    silhouette = silhouette_score(scaled_data, cluster_labels)
    return scaled_data, cluster_labels, kmeans, scaler, silhouette

@st.cache_data
def compute_elbow_data(scaled_data, max_k=10):
    inertias = []
    silhouettes = []
    k_range = range(2, max_k + 1)
    for k in k_range:
        km = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = km.fit_predict(scaled_data)
        inertias.append(km.inertia_)
        silhouettes.append(silhouette_score(scaled_data, labels))
    return list(k_range), inertias, silhouettes

# --- Sidebar & Navigation ---
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard Home",
        "Customer Segmentation",
        "Visualizations",
        "Customer Analysis",
        "Business Insights",
        "Download & Predict"
    ]
)

st.sidebar.markdown("---")
st.sidebar.header("📂 Data Import")
uploaded_file = st.sidebar.file_uploader("Upload 'customer_segmentation_1000.csv'", type=["csv"])

if uploaded_file is None:
    st.info("👆 Please upload the `customer_segmentation_1000.csv` file in the sidebar to get started.")
    st.stop()

# --- Load & Process Data ---
df = load_data(uploaded_file)

st.sidebar.markdown("---")
st.sidebar.header("⚙️ Clustering Settings")
k_val = st.sidebar.slider("Number of Clusters (K)", min_value=2, max_value=8, value=3)

scaled_data, cluster_labels, kmeans, scaler, sil_score = run_clustering(df, k=k_val)

df_segmented = df.copy()
df_segmented['Cluster'] = [f"Cluster {c}" for c in cluster_labels]

# --- 1. Dashboard Home ---
if page == "Dashboard Home":
    st.markdown("""
        <div class="header-box">
            <h1>📊 Customer Segmentation Dashboard</h1>
            <p>High-level summary of customer groups based on behavioral and demographic patterns.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Customers", f"{len(df_segmented):,}")
    col2.metric("Active Clusters (K)", k_val)
    col3.metric("Silhouette Score", f"{sil_score:.3f}")
    
    st.markdown("---")
    st.subheader("Customer Distribution across Clusters")
    
    dist_df = df_segmented['Cluster'].value_counts().reset_index()
    dist_df.columns = ['Cluster', 'Count']
    dist_df['Percentage'] = (dist_df['Count'] / len(df_segmented) * 100).round(2)
    
    fig = px.bar(
        dist_df, 
        x='Cluster', 
        y='Count', 
        text=dist_df['Percentage'].apply(lambda x: f"{x}%"),
        color='Cluster', 
        title="Customer Count per Cluster",
        color_discrete_sequence=px.colors.qualitative.Bold,
        template="plotly_white"
    )
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

# --- 2. Customer Segmentation ---
elif page == "Customer Segmentation":
    st.markdown("""
        <div class="header-box">
            <h1>🎯 Customer Segmentation Overview</h1>
            <p>Detailed distribution counts, percentages, and feature averages across customer segments.</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.subheader("Cluster Proportions")
    dist_df = df_segmented['Cluster'].value_counts().reset_index()
    dist_df.columns = ['Cluster', 'Customer Count']
    dist_df['Percentage (%)'] = (dist_df['Customer Count'] / len(df_segmented) * 100).round(2)
    st.dataframe(dist_df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.subheader("Average Feature Values per Cluster")
    avg_stats = df_segmented.groupby('Cluster')[FEATURE_COLS].mean().round(2)
    st.dataframe(avg_stats, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 3. Visualizations ---
elif page == "Visualizations":
    st.markdown("""
        <div class="header-box">
            <h1>📈 Cluster Visualizations</h1>
            <p>Optimal K evaluation charts, 2D PCA projection, and cluster profile comparisons.</p>
        </div>
    """, unsafe_allow_html=True)
    
    k_range, inertias, silhouettes = compute_elbow_data(scaled_data)
    
    col1, col2 = st.columns(2)
    with col1:
        fig_elbow = px.line(
            x=k_range, 
            y=inertias, 
            markers=True, 
            title="Elbow Method (Inertia vs K)",
            labels={'x': 'Number of Clusters (K)', 'y': 'Inertia'},
            template="plotly_white"
        )
        st.plotly_chart(fig_elbow, use_container_width=True)
        
    with col2:
        fig_sil = px.line(
            x=k_range, 
            y=silhouettes, 
            markers=True, 
            title="Silhouette Score vs K",
            labels={'x': 'Number of Clusters (K)', 'y': 'Silhouette Score'},
            template="plotly_white"
        )
        st.plotly_chart(fig_sil, use_container_width=True)
        
    st.markdown("---")
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("2D PCA Cluster Projection")
        pca = PCA(n_components=2)
        pca_coords = pca.fit_transform(scaled_data)
        pca_df = pd.DataFrame(pca_coords, columns=['PCA1', 'PCA2'])
        pca_df['Cluster'] = df_segmented['Cluster'].values
        
        fig_pca = px.scatter(
            pca_df, 
            x='PCA1', 
            y='PCA2', 
            color='Cluster', 
            title="2D Principal Component Projection",
            color_discrete_sequence=px.colors.qualitative.Bold,
            template="plotly_white"
        )
        st.plotly_chart(fig_pca, use_container_width=True)
        
    with col4:
        st.subheader("Key Feature Profile Comparison")
        selected_feature = st.selectbox("Select Feature to Profile:", FEATURE_COLS, index=1)
        
        fig_profile = px.bar(
            df_segmented.groupby('Cluster')[selected_feature].mean().reset_index(),
            x='Cluster',
            y=selected_feature,
            color='Cluster',
            title=f"Average {selected_feature} by Cluster",
            color_discrete_sequence=px.colors.qualitative.Bold,
            template="plotly_white"
        )
        st.plotly_chart(fig_profile, use_container_width=True)

# --- 4. Customer Analysis ---
elif page == "Customer Analysis":
    st.markdown("""
        <div class="header-box">
            <h1>🔍 Customer Analysis & Filtering</h1>
            <p>Filter customer records by cluster, category, membership tier, location, or gender.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    cluster_filter = col1.multiselect(
        "Cluster:", 
        options=sorted(df_segmented['Cluster'].unique()), 
        default=sorted(df_segmented['Cluster'].unique())
    )
    
    cat_filter = col2.multiselect(
        "Category:", 
        options=sorted(df_segmented['PreferredCategory'].unique()), 
        default=sorted(df_segmented['PreferredCategory'].unique())
    )
    
    member_filter = col3.multiselect(
        "Membership:", 
        options=sorted(df_segmented['MembershipLevel'].unique()), 
        default=sorted(df_segmented['MembershipLevel'].unique())
    )
    
    location_filter = col4.multiselect(
        "Location:", 
        options=sorted(df_segmented['Location'].unique()), 
        default=sorted(df_segmented['Location'].unique())
    )
    
    filtered_df = df_segmented[
        (df_segmented['Cluster'].isin(cluster_filter)) &
        (df_segmented['PreferredCategory'].isin(cat_filter)) &
        (df_segmented['MembershipLevel'].isin(member_filter)) &
        (df_segmented['Location'].isin(location_filter))
    ]
    
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.write(f"Showing **{len(filtered_df)}** matching records out of **{len(df_segmented)}** total customers:")
    st.dataframe(filtered_df, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 5. Business Insights ---
elif page == "Business Insights":
    st.markdown("""
        <div class="header-box">
            <h1>💡 Business Insights & Marketing Strategy</h1>
            <p>Actionable segments and target recommendations based on customer traits.</p>
        </div>
    """, unsafe_allow_html=True)
    
    if k_val == 3:
        st.markdown("""
        <div class="table-container">
        <b>Cluster 0: High-Value VIP Shoppers</b>
        <ul>
            <li><b>Profile:</b> Highest annual income (~$78.6k), spending score (~81), total purchase value (~$22.7k), and frequent visits.</li>
            <li><b>Target:</b> High-earning premium buyers.</li>
            <li><b>Strategy:</b> Priority support, exclusive product launches, personalized concierge services, and high-tier loyalty perks.</li>
        </ul>
        <hr>
        <b>Cluster 1: Tech-Savvy Younger Online Shoppers</b>
        <ul>
            <li><b>Profile:</b> Youngest age (~31 yrs), moderate income (~$61.3k), highest online purchase ratio (~67%).</li>
            <li><b>Target:</b> Digital-first younger buyers.</li>
            <li><b>Strategy:</b> Social media ad campaigns, app-exclusive discounts, fast online checkout incentives, and influencer collaborations.</li>
        </ul>
        <hr>
        <b>Cluster 2: Price-Sensitive Mature In-Store Buyers</b>
        <ul>
            <li><b>Profile:</b> Older age (~50 yrs), lower average income (~$55.5k), lower spending score (~52), mostly in-store purchases.</li>
            <li><b>Target:</b> Traditional value-seeking customers.</li>
            <li><b>Strategy:</b> In-store promotional coupons, bundle pricing, discount alerts via SMS, and loyalty point multipliers.</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info(f"Insights above are tailored for $K=3$. With $K={k_val}$, explore feature metrics in the 'Visualizations' and 'Customer Segmentation' tabs to profile the clusters.")

# --- 6. Download & Predict ---
elif page == "Download & Predict":
    st.markdown("""
        <div class="header-box">
            <h1>📥 Predict Cluster & Download Data</h1>
            <p>Predict the cluster segment for a new customer or export the full segmented dataset.</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 1. New Customer Prediction Section (Top)
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.subheader("🔮 Predict Cluster for a New Customer")
    st.write("Enter the customer details below to predict their segment using the trained model.")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age_in = st.number_input("Age", min_value=18, max_value=100, value=35)
        income_in = st.number_input("Annual Income ($)", min_value=10000, max_value=200000, value=60000, step=1000)
        spend_score_in = st.number_input("Spending Score (1-100)", min_value=1, max_value=100, value=50)
        freq_in = st.number_input("Purchase Frequency", min_value=1, max_value=50, value=10)

    with col2:
        avg_amt_in = st.number_input("Avg Purchase Amount ($)", min_value=10.0, max_value=5000.0, value=1200.0, step=50.0)
        total_val_in = st.number_input("Total Purchase Value ($)", min_value=10.0, max_value=50000.0, value=12000.0, step=500.0)
        online_pct_in = st.number_input("Online Purchase %", min_value=0, max_value=100, value=50)

    with col3:
        recency_in = st.number_input("Recency (Days)", min_value=0, max_value=365, value=30)
        disc_pct_in = st.number_input("Discount Usage %", min_value=0, max_value=100, value=25)
        sat_score_in = st.number_input("Satisfaction Score (1-10)", min_value=1.0, max_value=10.0, value=7.0, step=0.1)

    if st.button("🔮 Predict Customer Cluster", use_container_width=True):
        new_customer = np.array([[
            age_in, income_in, spend_score_in, freq_in,
            avg_amt_in, total_val_in, online_pct_in,
            recency_in, disc_pct_in, sat_score_in
        ]])
        
        scaled_input = scaler.transform(new_customer)
        predicted_cluster = kmeans.predict(scaled_input)[0]
        
        st.success(f"🎯 **Predicted Segment: Cluster {predicted_cluster}**")
        
        if k_val == 3:
            descriptions = {
                0: "High-Value VIP Shopper (High income, spending score, and total purchase value).",
                1: "Tech-Savvy Younger Online Shopper (Younger age, high online purchase ratio).",
                2: "Price-Sensitive Mature In-Store Buyer (Older age, lower spending score, in-store preference)."
            }
            st.info(f"**Segment Summary:** {descriptions.get(predicted_cluster, 'Custom cluster segment.')}")
    
    st.markdown('</div>', unsafe_allow_html=True)

    # 2. Download Section (Bottom)
    st.markdown('<div class="table-container">', unsafe_allow_html=True)
    st.subheader("📥 Export Segmented Data")
    st.write("Download the processed dataset containing all original attributes along with predicted cluster labels.")
    
    csv_data = df_segmented.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Segmented CSV",
        data=csv_data,
        file_name="customer_segmentation_1000_processed.csv",
        mime="text/csv"
    )
    st.markdown('</div>', unsafe_allow_html=True)