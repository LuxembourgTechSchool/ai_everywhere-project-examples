"""
Streamlit Theming & Component Customization Demo

Shows how to use .streamlit/config.toml for global theming and
st.markdown + CSS for fine-grained per-component styling.
"""

import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(
    page_title="Customization Demo",
    page_icon="🎨",
    layout="wide",
)

# ---------------------------------------------------------------------------
# Custom CSS injected once — overrides individual components by class / data
# attribute selectors that Streamlit exposes.
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    /* ---- Matrix global overrides ---- */
    * { font-family: "Courier New", Courier, monospace !important; }

    /* Glowing green headings */
    h1, h2, h3, h4 {
        text-shadow: 0 0 8px #00FF41, 0 0 20px #00FF4180;
    }

    /* Rounded cards for metric containers */
    div[data-testid="stMetric"] {
        background: #0D0D0D;
        border: 1px solid #00FF41;
        border-radius: 8px;
        padding: 16px 20px;
        box-shadow: 0 0 12px #00FF4140, inset 0 0 8px #00FF4115;
    }
    div[data-testid="stMetric"] label,
    div[data-testid="stMetric"] [data-testid="stMetricValue"],
    div[data-testid="stMetric"] [data-testid="stMetricDelta"] {
        color: #00FF41 !important;
    }

    /* Expander headers — left accent bar */
    details[data-testid="stExpander"] summary {
        border-left: 4px solid #00FF41;
        padding-left: 12px;
    }

    /* Sidebar — dark with faint green glow at top */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1A1A2E 0%, #0D0D0D 100%);
        border-right: 1px solid #00FF4130;
    }

    /* Pill-style tab buttons */
    div[data-testid="stTabs"] button[data-baseweb="tab"] {
        border-radius: 20px;
        margin-right: 6px;
        padding: 6px 20px;
        border: 1px solid #00FF41;
        background: transparent;
        color: #00FF41;
        font-weight: 600;
        transition: all 0.2s ease;
    }
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background: #00FF41 !important;
        color: #0D0D0D !important;
        box-shadow: 0 0 10px #00FF4180;
    }

    /* Buttons — neon glow */
    button[data-testid="stBaseButton-primary"] {
        border: 1px solid #00FF41 !important;
        box-shadow: 0 0 8px #00FF4160;
    }
    button[data-testid="stBaseButton-primary"]:hover {
        box-shadow: 0 0 16px #00FF41A0;
    }

    /* Text inputs, selects, text areas — green caret & border */
    input, textarea, [data-baseweb="select"] {
        caret-color: #00FF41 !important;
    }
    input:focus, textarea:focus {
        border-color: #00FF41 !important;
        box-shadow: 0 0 6px #00FF4140 !important;
    }

    /* Progress bars — green fill */
    div[data-testid="stProgress"] > div > div > div {
        background-color: #00FF41 !important;
    }

    /* Dividers */
    hr {
        border-color: #00FF4130 !important;
    }

    /* Dataframe header row */
    div[data-testid="stDataFrame"] thead th {
        background: #1A1A2E !important;
        color: #00FF41 !important;
    }

    /* Alert boxes — keep type-specific colours but add border glow */
    div[data-testid="stAlert"] {
        border: 1px solid #00FF4130;
    }

    /* Scrollbar styling */
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #0D0D0D; }
    ::-webkit-scrollbar-thumb { background: #00FF4160; border-radius: 4px; }
    ::-webkit-scrollbar-thumb:hover { background: #00FF41; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar — theme reference
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("Theme Settings")
    st.markdown(
        """
        The global theme is defined in
        **`.streamlit/config.toml`**:

        ```toml
        [theme]
        primaryColor = "#00FF41"
        backgroundColor = "#0D0D0D"
        secondaryBackgroundColor = "#1A1A2E"
        textColor = "#00FF41"
        font = "monospace"
        ```

        Everything on this page inherits these
        values automatically. The CSS block at
        the top of `app.py` adds *per-component*
        overrides on top.
        """
    )

    st.divider()
    accent = st.color_picker("Pick an accent color", "#00FF41")
    st.caption(
        "This color picker is a themed component — "
        "its button inherits `primaryColor`."
    )

# ---------------------------------------------------------------------------
# Page header
# ---------------------------------------------------------------------------
st.title("🎨 Streamlit Theming & Customization")
st.caption(
    "A single-page app showcasing how `.streamlit/config.toml` and "
    "injected CSS work together to style every component."
)

# ---------------------------------------------------------------------------
# Metrics row — styled with gradient CSS above
# ---------------------------------------------------------------------------
st.subheader("Metrics")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Revenue", "$12,480", "+8.2 %")
m2.metric("Users", "3,241", "+124")
m3.metric("Bounce Rate", "34 %", "-2.1 %", delta_color="inverse")
m4.metric("Avg. Session", "4m 12s", "+0m 18s")

st.divider()

# ---------------------------------------------------------------------------
# Tabs — pill-style via CSS above
# ---------------------------------------------------------------------------
st.subheader("Tabs")
tab_inputs, tab_charts, tab_data, tab_feedback = st.tabs(
    ["Inputs", "Charts", "Data Table", "Feedback"]
)

# --- Inputs tab ----
with tab_inputs:
    col_left, col_right = st.columns(2)

    with col_left:
        st.text_input("Your name", placeholder="Jane Doe")
        st.number_input("Quantity", min_value=0, max_value=100, value=10)
        st.date_input("Start date")
        st.time_input("Meeting time")

    with col_right:
        st.selectbox("Favourite fruit", ["Apple", "Banana", "Cherry", "Dragonfruit"])
        st.multiselect("Skills", ["Python", "SQL", "JavaScript", "Rust", "Go"], default=["Python"])
        st.slider("Satisfaction", 0, 100, 75)
        st.select_slider("T-shirt size", options=["XS", "S", "M", "L", "XL"], value="M")

    st.divider()
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.checkbox("I agree to the terms")
    with col_b:
        st.toggle("Dark mode")
    with col_c:
        st.radio("Notification preference", ["Email", "SMS", "Push"], horizontal=True)

# --- Charts tab ---
with tab_charts:
    np.random.seed(42)
    dates = pd.date_range("2025-01-01", periods=60, freq="D")
    chart_df = pd.DataFrame(
        np.random.randn(60, 3).cumsum(axis=0),
        index=dates,
        columns=["Product A", "Product B", "Product C"],
    )

    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**Line chart** — uses `primaryColor` for the first series")
        st.line_chart(chart_df)
    with c2:
        st.markdown("**Area chart**")
        st.area_chart(chart_df)

    st.markdown("**Bar chart** — last 14 days")
    st.bar_chart(chart_df.tail(14))

# --- Data table tab ---
with tab_data:
    rows = 50
    table_df = pd.DataFrame(
        {
            "ID": range(1, rows + 1),
            "Name": [f"Item {i}" for i in range(1, rows + 1)],
            "Category": np.random.choice(["A", "B", "C"], size=rows),
            "Value": np.random.uniform(10, 500, size=rows).round(2),
            "Active": np.random.choice([True, False], size=rows),
        }
    )

    st.dataframe(
        table_df,
        use_container_width=True,
        column_config={
            "Value": st.column_config.NumberColumn(format="$ %.2f"),
            "Active": st.column_config.CheckboxColumn("Active?"),
        },
        hide_index=True,
    )

# --- Feedback tab ---
with tab_feedback:
    with st.form("feedback_form"):
        st.text_input("Email")
        rating = st.slider("Rating", 1, 5, 4)
        st.text_area("Comments", placeholder="Tell us what you think…")
        submitted = st.form_submit_button("Send Feedback", use_container_width=True)

    if submitted:
        st.success("Thank you for your feedback!")
        st.balloons()

st.divider()

# ---------------------------------------------------------------------------
# Expander — accent border via CSS above
# ---------------------------------------------------------------------------
st.subheader("Expanders")
with st.expander("How does global theming work?"):
    st.markdown(
        """
        Streamlit reads **`.streamlit/config.toml`** at startup. Any key
        under `[theme]` is applied to every widget automatically:

        | Key | Purpose |
        |---|---|
        | `primaryColor` | Accent for buttons, sliders, checkboxes |
        | `backgroundColor` | Main page background |
        | `secondaryBackgroundColor` | Sidebar, cards, inputs |
        | `textColor` | Default text |
        | `font` | `"sans serif"`, `"serif"`, or `"monospace"` |
        """
    )

with st.expander("How does per-component CSS work?"):
    st.markdown(
        """
        Inject a `<style>` block via `st.markdown(…, unsafe_allow_html=True)`.
        Target Streamlit's `data-testid` attributes for stability:

        ```css
        div[data-testid="stMetric"] {
            background: linear-gradient(…);
            border-radius: 12px;
        }
        ```

        This lets you override colours, spacing, borders, and animations
        on a per-component basis without touching the global theme.
        """
    )

# ---------------------------------------------------------------------------
# Progress & status
# ---------------------------------------------------------------------------
st.subheader("Progress & Status")
p1, p2 = st.columns(2)
with p1:
    st.progress(72, text="Model training — 72 %")
    st.progress(45, text="Data ingestion — 45 %")
with p2:
    st.info("ℹ️  This is an info alert — inherits `primaryColor`.")
    st.warning("⚠️  Warning alert — always amber.")
    st.error("🚨  Error alert — always red.")
    st.success("✅  Success alert — always green.")

# ---------------------------------------------------------------------------
# Buttons row
# ---------------------------------------------------------------------------
st.subheader("Buttons")
b1, b2, b3, b4 = st.columns(4)
with b1:
    st.button("Primary", use_container_width=True)
with b2:
    st.button("Secondary", use_container_width=True, type="secondary")
with b3:
    st.button("Tertiary", use_container_width=True, type="tertiary")
with b4:
    st.link_button("Open Docs ↗", "https://docs.streamlit.io/develop/concepts/configuration/theming", use_container_width=True)

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.divider()
st.caption(
    f"Accent swatch from sidebar: **{accent}** · "
    "Built with [Streamlit](https://streamlit.io)"
)
