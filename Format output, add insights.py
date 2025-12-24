import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Load & prepare data
# -------------------------------
df = pd.read_csv("cleaned_sales_data.csv")
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

df["revenue"] = df["quantity"] * df["price"]

product_revenue = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

# KPIs
total_revenue = df["revenue"].sum()
total_orders = len(df)
total_products = df["product"].nunique()
best_product = product_revenue.idxmax()

# -------------------------------
# Figure setup
# -------------------------------
fig = plt.figure(figsize=(16, 9))
fig.patch.set_facecolor("white")

fig.text(
    0.5, 0.95,
    "Sales Performance Dashboard",
    ha="center",
    fontsize=22,
    fontweight="bold"
)

# -------------------------------
# KPI CARD FUNCTION
# -------------------------------
def kpi_card(x, y, w, h, title, value):
    ax = fig.add_axes([x, y, w, h])
    ax.axis("off")
    ax.add_patch(plt.Rectangle((0, 0), 1, 1, fill=False))
    ax.text(0.05, 0.65, title, fontsize=12, alpha=0.7)
    ax.text(0.05, 0.25, value, fontsize=20, fontweight="bold")

# -------------------------------
# KPI GRID
# -------------------------------
card_width = 0.21
card_height = 0.12
y_pos = 0.78
gap = 0.02

kpi_card(0.05, y_pos, card_width, card_height, "Total Revenue", f"₹{total_revenue:,.0f}")
kpi_card(0.05 + (card_width + gap), y_pos, card_width, card_height, "Total Orders", f"{total_orders}")
kpi_card(0.05 + 2*(card_width + gap), y_pos, card_width, card_height, "Total Products", f"{total_products}")
kpi_card(0.05 + 3*(card_width + gap), y_pos, card_width, card_height, "Best Product", best_product)

# -------------------------------
# BAR CHART (Different colors)
# -------------------------------
ax_bar = fig.add_axes([0.05, 0.08, 0.58, 0.6])

# Power BI–style color palette
colors = plt.cm.tab10(range(len(product_revenue)))

bars = ax_bar.bar(
    product_revenue.index,
    product_revenue.values,
    color=colors
)

ax_bar.set_title("Revenue by Product", fontweight="bold")
ax_bar.set_xlabel("Product")
ax_bar.set_ylabel("Revenue")
ax_bar.grid(axis="y", linestyle="--", alpha=0.4)
ax_bar.tick_params(axis="x", rotation=30)

# Value labels
for bar in bars:
    height = bar.get_height()
    ax_bar.text(
        bar.get_x() + bar.get_width() / 2,
        height,
        f"₹{height:,.0f}",
        ha="center",
        va="bottom",
        fontsize=9
    )

# -------------------------------
# DONUT CHART
# -------------------------------
ax_pie = fig.add_axes([0.67, 0.15, 0.28, 0.45])

ax_pie.pie(
    product_revenue.values,
    labels=product_revenue.index,
    autopct="%1.1f%%",
    startangle=120,
    wedgeprops={"edgecolor": "white"}
)

centre_circle = plt.Circle((0, 0), 0.65, fc="white")
ax_pie.add_artist(centre_circle)

ax_pie.set_title("Revenue Contribution", fontweight="bold")

# -------------------------------
# Save Dashboard
# -------------------------------
plt.savefig("powerbi_grid_sales_dashboard.png", dpi=300)
plt.show()

print("✅ Dashboard with colored bars saved as 'powerbi_grid_sales_dashboard.png'")
