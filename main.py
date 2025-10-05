import warnings
import sys
warnings.filterwarnings('ignore')

sys.path.insert(0, 'src')

from data_preprocessing import DataPreprocessor
from clustering_analysis import ClusteringAnalysis
from cluster_profiling import ClusterProfiler
from visualization import ClusterVisualizer
from intervention_recommendations import InterventionRecommender

def main():
    print("\n" + "=" * 80)
    print(" " * 20 + "LEARNER ENGAGEMENT CLUSTERING ANALYSIS")
    print(" " * 80)
    print("=" * 80)
    
    dataset_path = 'attached_assets/EROLP Dataset_1759650613911.csv'
    
    print("\n[STEP 1/6] DATA PREPROCESSING")
    preprocessor = DataPreprocessor(dataset_path)
    preprocess_results = preprocessor.preprocess_pipeline()
    
    df_original = preprocess_results['df_original']
    X_scaled = preprocess_results['X_scaled']
    feature_cols = preprocess_results['feature_cols']
    
    print("\n[STEP 2/6] CLUSTERING ANALYSIS")
    clustering = ClusteringAnalysis(X_scaled, df_original, feature_cols)
    
    print("\nDetermining optimal number of clusters...")
    clustering.elbow_method(k_range=range(2, 8))
    clustering.silhouette_analysis(k_range=range(2, 8))
    
    cluster_labels = clustering.fit_kmeans()
    
    cluster_stats = clustering.get_cluster_statistics()
    print("\n" + "=" * 60)
    print("CLUSTER STATISTICS SUMMARY")
    print("=" * 60)
    print(cluster_stats.to_string(index=False))
    
    df_clustered = clustering.add_clusters_to_dataframe()
    
    print("\n[STEP 3/6] CLUSTER PROFILING")
    profiler = ClusterProfiler(df_clustered)
    cluster_profiles = profiler.profile_clusters()
    
    high_risk_cluster = profiler.identify_high_risk_cluster()
    
    dropout_rates, baseline_dropout = profiler.calculate_dropout_rate()
    
    profiles_df = profiler.export_cluster_profiles()
    
    print("\n[STEP 4/6] VISUALIZATION GENERATION")
    visualizer = ClusterVisualizer(df_clustered)
    visualizer.generate_all_visualizations()
    
    print("\n[STEP 5/6] INTERVENTION RECOMMENDATIONS")
    recommender = InterventionRecommender(df_clustered, cluster_profiles, high_risk_cluster)
    recommendations = recommender.generate_recommendations()
    recs_df = recommender.export_recommendations()
    
    print("\n[STEP 6/6] EXPORTING RESULTS FOR TABLEAU")
    tableau_export_path = 'learner_clusters_tableau.csv'
    df_clustered.to_csv(tableau_export_path, index=False)
    print(f"Full clustered dataset exported to '{tableau_export_path}'")
    print(f"This file can be imported into Tableau for interactive dashboard creation.")
    
    print("\n" + "=" * 80)
    print("ANALYSIS COMPLETE - SUMMARY OF OUTPUTS")
    print("=" * 80)
    print("\nGenerated Files:")
    print("  1. elbow_method.png - Elbow plot for optimal k selection")
    print("  2. silhouette_analysis.png - Silhouette scores for cluster validation")
    print("  3. cluster_distribution.png - Learner distribution across clusters")
    print("  4. engagement_by_cluster.png - Engagement patterns by cluster")
    print("  5. performance_by_cluster.png - Pre/post-test scores and knowledge gain")
    print("  6. demographic_patterns.png - Age, gender, location, socioeconomic breakdown")
    print("  7. behavioral_patterns.png - Learning pace, medium, platform, content preferences")
    print("  8. cluster_heatmap.png - Cluster characteristics heatmap")
    print("  9. cluster_profiles.csv - Statistical profiles of each cluster")
    print(" 10. intervention_recommendations.csv - Targeted intervention strategies")
    print(" 11. learner_clusters_tableau.csv - Full dataset with cluster labels for Tableau")
    
    print("\n" + "=" * 80)
    print("KEY FINDINGS")
    print("=" * 80)
    print(f"\nTotal Learners Analyzed: {len(df_clustered):,}")
    print(f"Number of Clusters Identified: {len(cluster_profiles)}")
    print(f"High-Risk Cluster: Cluster {high_risk_cluster}")
    print(f"Baseline Dropout Rate: {baseline_dropout:.2f}%")
    print(f"High-Risk Cluster Dropout Rate: {dropout_rates[high_risk_cluster]:.2f}%")
    
    print("\nCluster Summary:")
    for cluster_id, profile in cluster_profiles.items():
        priority = recommendations[cluster_id]['intervention_priority']
        print(f"  Cluster {cluster_id}: {profile['size']} learners - {priority}")
    
    print("\n" + "=" * 80)
    print("NEXT STEPS FOR TABLEAU DASHBOARD")
    print("=" * 80)
    print("\n1. Import 'learner_clusters_tableau.csv' into Tableau")
    print("2. Create visualizations using the Cluster field as a dimension")
    print("3. Build interactive filters for demographics and behavioral metrics")
    print("4. Design drill-down dashboards for each cluster segment")
    print("5. Add calculated fields for dropout risk indicators")
    print("6. Create executive summary dashboard with key KPIs")
    
    print("\n" + "=" * 80)
    print("ANALYSIS SESSION COMPLETED SUCCESSFULLY!")
    print("=" * 80 + "\n")

if __name__ == "__main__":
    main()
