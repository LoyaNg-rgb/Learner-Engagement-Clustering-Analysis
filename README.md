# 📊 Learner Engagement Clustering Analysis

A comprehensive machine learning pipeline for analyzing learner engagement patterns, identifying at-risk students, and generating data-driven intervention recommendations using unsupervised clustering techniques.

## 🎯 Project Overview

This project performs advanced clustering analysis on educational data to segment learners based on engagement patterns, demographic characteristics, and performance metrics. It identifies high-risk clusters and provides actionable intervention strategies to improve learning outcomes.

### Key Features

- **Automated Data Preprocessing**: Handles missing values, encodes categorical variables, and scales features
- **Clustering Analysis**: Implements K-Means clustering with optimal cluster determination
- **Cluster Profiling**: Generates detailed statistical profiles for each learner segment
- **Risk Identification**: Identifies high-risk clusters based on dropout rates and engagement metrics
- **Visualization Suite**: Creates 8+ publication-ready visualizations
- **Intervention Recommendations**: Provides targeted, evidence-based intervention strategies
- **Tableau Integration**: Exports processed data for interactive dashboard creation

## 📁 Project Structure

```
learner-engagement-clustering/
│
├── main.py                          # Main execution script
├── requirements.txt                 # Python dependencies
├── README.md                        # This file
├── LICENSE                          # Project license
├── .gitignore                      # Git ignore rules
│
├── src/                            # Source code modules
│   ├── __init__.py
│   ├── data_preprocessing.py       # Data cleaning and feature engineering
│   ├── clustering_analysis.py      # K-Means clustering implementation
│   ├── cluster_profiling.py        # Statistical profiling and risk analysis
│   ├── visualization.py            # Visualization generation
│   └── intervention_recommendations.py  # Intervention strategy generator
│
├── attached_assets/                # Input data directory
│   └── EROLP Dataset_1759650613911.csv
│
├── outputs/                        # Generated outputs
│   ├── visualizations/            # PNG charts and plots
│   ├── cluster_profiles.csv       # Cluster statistics
│   ├── intervention_recommendations.csv
│   └── learner_clusters_tableau.csv
│
├── docs/                          # Documentation
│   ├── methodology.md             # Analysis methodology
│   ├── cluster_interpretation.md  # Guide to interpreting results
│   └── tableau_guide.md           # Tableau dashboard setup
│
└── notebooks/                     # Jupyter notebooks (optional)
    └── exploratory_analysis.ipynb
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/learner-engagement-clustering.git
   cd learner-engagement-clustering
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare your data**
   - Place your dataset in the `attached_assets/` directory
   - Update the `dataset_path` in `main.py` if using a different filename

### Usage

Run the complete analysis pipeline:

```bash
python main.py
```

The script will execute all six stages:
1. Data Preprocessing
2. Clustering Analysis
3. Cluster Profiling
4. Visualization Generation
5. Intervention Recommendations
6. Tableau Export

## 📊 Outputs

### Visualizations
- `elbow_method.png` - Optimal cluster number determination
- `silhouette_analysis.png` - Cluster quality validation
- `cluster_distribution.png` - Learner distribution across clusters
- `engagement_by_cluster.png` - Engagement pattern analysis
- `performance_by_cluster.png` - Academic performance metrics
- `demographic_patterns.png` - Demographic breakdowns
- `behavioral_patterns.png` - Learning behavior analysis
- `cluster_heatmap.png` - Multi-dimensional cluster comparison

### Data Files
- `cluster_profiles.csv` - Statistical summaries for each cluster
- `intervention_recommendations.csv` - Targeted intervention strategies
- `learner_clusters_tableau.csv` - Full dataset with cluster labels

## 🔍 Methodology

### Clustering Algorithm
- **Algorithm**: K-Means Clustering
- **Optimization**: Elbow Method + Silhouette Analysis
- **Feature Scaling**: StandardScaler normalization
- **Validation**: Silhouette Score, Within-Cluster Sum of Squares (WCSS)

### Features Used
- Engagement metrics (sessions, duration, completion rates)
- Academic performance (pre/post-test scores, knowledge gain)
- Demographic characteristics (age, gender, location, SES)
- Behavioral patterns (learning pace, medium preferences, platform usage)

### Risk Assessment
High-risk clusters are identified based on:
- Dropout rates
- Low engagement scores
- Poor performance indicators
- Session completion patterns

## 📈 Tableau Dashboard Integration

1. Import `learner_clusters_tableau.csv` into Tableau
2. Use the `Cluster` field as your primary dimension
3. Create calculated fields for risk indicators
4. Build interactive filters for demographic segmentation
5. Design drill-down views for each cluster

See `docs/tableau_guide.md` for detailed instructions.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Loyanganba Ngathem** - (https://github.com/LoyaNg-rgb)

## 🙏 Acknowledgments

- Educational institutions providing anonymized learner data
- Open-source contributors to scikit-learn, pandas, and matplotlib
- Research community for clustering methodology insights

## 📧 Contact

For questions or feedback, please open an issue or contact: loyanganba.ngathem@gmail.com

## 🗺️ Roadmap

- [ ] Add support for hierarchical clustering
- [ ] Implement DBSCAN for density-based clustering
- [ ] Add time-series analysis for engagement trends
- [ ] Create automated report generation
- [ ] Build web-based dashboard interface
- [ ] Add predictive modeling for early dropout detection

---

**Note**: This project analyzes anonymized educational data. Ensure compliance with data privacy regulations (FERPA, GDPR) when working with learner information.
