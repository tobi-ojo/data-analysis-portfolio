# Billionaires Data Analysis
# Python Data Analysis Project

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

print("=" * 60)
print("GLOBAL BILLIONAIRES ANALYSIS - PYTHON PROJECT")
print("=" * 60)

# Load data
print("\n Loading billionaires data...")
df = pd.read_csv('Billionaires Statistics Dataset - Billionaires Statistics Dataset.csv')
print(f"✓ Loaded {len(df)} billionaire records")
print(f"✓ Columns: {list(df.columns)[:5]}...")

# Basic statistics
print("\n=== BILLIONAIRES STATISTICS ===")
print(f"Total Billionaires: {len(df)}")

if 'country' in df.columns:
    print(f"\nTop 10 Countries by Billionaire Count:")
    print(df['country'].value_counts().head(10))

if 'industries' in df.columns:
    print(f"\nTop 5 Industries:")
    print(df['industries'].value_counts().head(5))

if 'finalWorth' in df.columns:
    print(f"\nWealth Statistics:")
    print(f"  Average Net Worth: ${df['finalWorth'].mean():.2f}B")
    print(f"  Highest Net Worth: ${df['finalWorth'].max():.2f}B")
    print(f"  Total Wealth: ${df['finalWorth'].sum():.2f}B")

# Create visualizations
print("\n Creating visualizations...")

# Chart 1: Top 10 Countries
if 'country' in df.columns:
    plt.figure(figsize=(12, 6))
    top_countries = df['country'].value_counts().head(10)
    top_countries.plot(kind='barh', color='steelblue')
    plt.title('Top 10 Countries by Billionaire Count', fontsize=16, fontweight='bold')
    plt.xlabel('Number of Billionaires', fontsize=12)
    plt.ylabel('Country', fontsize=12)
    plt.tight_layout()
    plt.savefig('top_countries.png', dpi=300, bbox_inches='tight')
    print("✓ Created: top_countries.png")
    plt.close()

# Chart 2: Industry Distribution
if 'industries' in df.columns:
    plt.figure(figsize=(10, 10))
    top_industries = df['industries'].value_counts().head(8)
    plt.pie(top_industries.values, labels=top_industries.index, autopct='%1.1f%%', startangle=90)
    plt.title('Billionaires by Industry (Top 8)', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('industry_distribution.png', dpi=300, bbox_inches='tight')
    print("✓ Created: industry_distribution.png")
    plt.close()

# Chart 3: Wealth Distribution by Country
if 'country' in df.columns and 'finalWorth' in df.columns:
    plt.figure(figsize=(12, 6))
    country_wealth = df.groupby('country')['finalWorth'].sum().sort_values(ascending=False).head(10)
    country_wealth.plot(kind='bar', color='green')
    plt.title('Top 10 Countries by Total Wealth', fontsize=16, fontweight='bold')
    plt.xlabel('Country', fontsize=12)
    plt.ylabel('Total Net Worth (Billions $)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('wealth_by_country.png', dpi=300, bbox_inches='tight')
    print("✓ Created: wealth_by_country.png")
    plt.close()

# Create summary report
summary = f"""
GLOBAL BILLIONAIRES ANALYSIS
Python Data Analysis Project
======================================

DATASET OVERVIEW
----------------
Total Billionaires: {len(df)}
Analysis Date: February 2026

TOP COUNTRIES
-------------
{df['country'].value_counts().head(10).to_string() if 'country' in df.columns else 'N/A'}

WEALTH STATISTICS
-----------------
Average Net Worth: ${df['finalWorth'].mean():.2f}B
Highest Net Worth: ${df['finalWorth'].max():.2f}B
Total Global Wealth: ${df['finalWorth'].sum():.2f}B

TECHNICAL DETAILS
-----------------
Tools Used:
- Python 3.14
- Pandas (data manipulation)
- Matplotlib (visualization)

Analysis Type:
- Descriptive statistics
- Geographic analysis
- Industry breakdown
- Wealth distribution

DELIVERABLES
------------
1. top_countries.png - Top 10 countries bar chart
2. industry_distribution.png - Industry pie chart
3. wealth_by_country.png - Wealth by country bar chart
4. analysis_summary.txt - This report

======================================
Analyst: Victor Ojo
Project: Data Analysis Portfolio
======================================
"""

with open('analysis_summary.txt', 'w') as f:
    f.write(summary)

print("✓ Created: analysis_summary.txt")

print("\n" + "=" * 60)
print(" ANALYSIS COMPLETE!")
print("=" * 60)
print("\nGenerated Files:")
print("  • top_countries.png")
print("  • industry_distribution.png")
print("  • wealth_by_country.png")
print("  • analysis_summary.txt")
print("\n Python project ready for portfolio!")