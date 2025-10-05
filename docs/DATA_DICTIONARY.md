# 📖 Data Dictionary

Complete reference for all data fields used in the Learner Engagement Clustering Analysis.

## Table of Contents
1. [Input Data Fields](#input-data-fields)
2. [Derived Fields](#derived-fields)
3. [Output Data Fields](#output-data-fields)
4. [Data Types](#data-types)
5. [Data Quality Guidelines](#data-quality-guidelines)

---

## Input Data Fields

### Identifiers

| Field Name | Type | Description | Example | Required |
|------------|------|-------------|---------|----------|
| `Learner_ID` | String | Unique identifier for each learner | "L001", "STU_12345" | ✅ Yes |

### Demographics

| Field Name | Type | Description | Valid Values | Required |
|------------|------|-------------|--------------|----------|
| `Age` | Integer | Age in years | 15-100 | ✅ Yes |
| `Gender` | String | Gender identity | "Male", "Female", "Other" | ✅ Yes |
| `Location` | String | Geographic location type | "Urban", "Rural", "Suburban" | ✅ Yes |
| `Socioeconomic_Status` | String | Economic background | "Low", "Middle", "High" | ✅ Yes |

**Notes**:
- Age outliers (< 15 or > 100) are flagged for review
- Missing demographic values are imputed using mode
- Socioeconomic status is ordinal-encoded (Low=0, Middle=1, High=2)

### Engagement Metrics

| Field Name | Type | Description | Range | Required |
|------------|------|-------------|-------|----------|
| `Learning_Sessions_Completed` | Integer | Number of completed learning sessions | 0-1000 | ✅ Yes |
| `Total_Time_Spent_Minutes` | Float | Total learning time in minutes | 0-100000 | ✅ Yes |
| `Course_Completion_Percentage` | Float | Percentage of course completed | 0.0-100.0 | ✅ Yes |
| `Days_Since_Last_Login` | Integer | Days since last platform access | 0-365 | ✅ Yes |
| `Average_Session_Duration` | Float | Average minutes per session | 0-600 | ⚪ Optional |

**Calculations**:
- If `Average_Session_Duration` is missing: `Total_Time_Spent_Minutes / Learning_Sessions_Completed`
- Sessions with duration > 8 hours are flagged as potential data errors

### Performance Metrics

| Field Name | Type | Description | Range | Required |
|------------|------|-------------|-------|----------|
| `Pre_Test_Score` | Float | Score before course | 0-100 | ✅ Yes |
| `Post_Test_Score` | Float | Score after course | 0-100 | ✅ Yes |

**Validation Rules**:
- Scores must be between 0-100
- Post-test scores significantly lower than pre-test (> 20 points) are flagged
- Missing scores are imputed with median

### Status Indicators

| Field Name | Type | Description | Valid Values | Required |
|------------|------|-------------|--------------|----------|
| `Dropout` | Boolean | Whether learner dropped out | True, False | ✅ Yes |
| `Enrollment_Date` | Date | Course enrollment date | YYYY-MM-DD | ⚪ Optional |
| `Completion_Date` | Date | Course completion date | YYYY-MM-DD | ⚪ Optional |

**Notes**:
- `Dropout=True` if `Course_Completion_Percentage < 100` and no activity for 30+ days
- Missing dropout status is inferred from completion percentage

### Behavioral Attributes

| Field Name | Type | Description | Valid Values | Required |
|------------|------|-------------|--------------|----------|
| `Learning_Pace` | String | Speed of progress | "Slow", "Moderate", "Fast" | ✅ Yes |
| `Learning_Medium` | String | Primary learning mode | "Online", "Offline", "Hybrid" | ✅ Yes |
| `Platform_Used` | String | Device preference | "Mobile", "Desktop", "Both", "Tablet" | ✅ Yes |
| `Content_Type_Preferred` | String | Content preference | "Video", "Text", "Interactive", "Audio" | ✅ Yes |

**Encoding**:
- `Learning_Pace`: Ordinal (Slow=0, Moderate=1, Fast=2)
- Other behavioral fields: One-hot encoded

---

## Derived Fields

These fields are calculated during preprocessing:

| Field Name | Type | Formula | Description |
|------------|------|---------|-------------|
| `Knowledge_Gain` | Float | `Post_Test_Score - Pre_Test_Score` | Points gained |
| `Knowledge_Gain_Percentage` | Float | `(Knowledge_Gain / Pre_Test_Score) × 100` | % improvement |
| `Engagement_Rate` | Float | `Learning_Sessions_Completed / Total_Possible_Sessions` | Session completion rate |
| `Average_Daily_Time` | Float | `Total_Time_Spent_Minutes / Days_Enrolled` | Daily time investment |
| `Sessions_Per_Week` | Float | `(Learning_Sessions_Completed / Days_Enrolled) × 7` | Weekly session frequency |

**Usage**: These derived fields are used for clustering and profiling.

---

## Output Data Fields

### Cluster Assignments

| Field Name | Type | Description | Example | Source File |
|------------|------|-------------|---------|-------------|
| `Cluster` | Integer | Assigned cluster ID | 0, 1, 2, 3 | `learner_clusters_tableau.csv` |
| `Cluster_Label` | String | Descriptive cluster name | "High Performers" | Generated during profiling |
| `Risk_Level` | String | Risk assessment | "High", "Medium", "Low" | Calculated based on dropout |

### Cluster Statistics (cluster_profiles.csv)

| Field Name | Type | Description |
|------------|------|-------------|
| `Cluster_ID` | Integer | Cluster identifier |
| `Size` | Integer | Number of learners in cluster |
| `Percentage` | Float | % of total learners |
| `Avg_Age` | Float | Mean age |
| `Avg_Sessions` | Float | Mean sessions completed |
| `Avg_Time_Spent` | Float | Mean time in minutes |
| `Avg_Completion` | Float | Mean completion % |
| `Avg_Pre_Test` | Float | Mean pre-test score |
| `Avg_Post_Test` | Float | Mean post-test score |
| `Avg_Knowledge_Gain` | Float | Mean knowledge gain |
| `Dropout_Rate` | Float | % of learners who dropped out |
| `Dominant_Gender` | String | Most common gender |
| `Dominant_Location` | String | Most common location |
| `Dominant_Pace` | String | Most common learning pace |
| `Risk_Category` | String | Overall risk level |

### Intervention Recommendations (intervention_recommendations.csv)

| Field Name | Type | Description |
|------------|------|-------------|
| `Cluster_ID` | Integer | Target cluster |
| `Intervention_Priority` | String | "High", "Medium", "Low" |
| `Primary_Strategy` | String | Main intervention approach |
| `Specific_Actions` | String | Detailed action items |
| `Expected_Impact` | String | Anticipated outcomes |
| `Implementation_Complexity` | String | "Low", "Medium", "High" |
| `Estimated_Cost` | String | Relative cost indicator |

---

## Data Types

### Numeric Types

```python
# Integer fields
int_fields = [
    'Age',
    'Learning_Sessions_Completed',
    'Days_Since_Last_Login',
    'Cluster'
]

# Float fields
float_fields = [
    'Total_Time_Spent_Minutes',
    'Course_Completion_Percentage',
    'Pre_Test_Score',
    'Post_Test_Score',
    'Knowledge_Gain',
    'Average_Session_Duration'
]
```

### Categorical Types

```python
# Nominal (no order)
nominal_fields = [
    'Gender',
    'Location',
    'Learning_Medium',
    'Platform_Used',
    'Content_Type_Preferred'
]

# Ordinal (ordered)
ordinal_fields = [
    'Socioeconomic_Status',  # Low < Middle < High
    'Learning_Pace',         # Slow < Moderate < Fast
    'Risk_Level'             # Low < Medium < High
]
```

### Boolean Types

```python
boolean_fields = [
    'Dropout'  # True/False
]
```

---

## Data Quality Guidelines

### Required Data Quality Standards

1. **Completeness**
   - Critical fields: < 5% missing values
   - Non-critical fields: < 20% missing values
   - Overall: < 10% missing values

2. **Accuracy**
   - Numeric ranges validated
   - Categorical values match allowed list
   - No logical inconsistencies (e.g., completion > 100%)

3. **Consistency**
   - Date formats: ISO 8601 (YYYY-MM-DD)
   - Decimal precision: 2 decimal places
   - Text casing: Title Case for categories

4. **Uniqueness**
   - Learner_ID must be unique
   - No duplicate records

### Data Validation Checks

```python
# Example validation code
def validate_dataset(df):
    """Validate input dataset quality."""
    
    # Check required columns
    required_cols = [
        'Learner_ID', 'Age', 'Gender', 
        'Learning_Sessions_Completed', 'Pre_Test_Score'
    ]
    missing_cols = set(required_cols) - set(df.columns)
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    # Check for duplicates
    if df['Learner_ID'].duplicated().any():
        raise ValueError("Duplicate Learner_IDs found")
    
    # Validate ranges
    if (df['Age'] < 0).any() or (df['Age'] > 150).any():
        print("Warning: Age values outside expected range")
    
    if (df['Pre_Test_Score'] < 0).any() or (df['Pre_Test_Score'] > 100).any():
        raise ValueError("Pre_Test_Score must be 0-100")
    
    return True
```

### Missing Value Handling

| Field Type | Strategy | Rationale |
|------------|----------|-----------|
| Numeric (continuous) | Median imputation | Robust to outliers |
| Numeric (count) | Mode imputation | Preserves distribution |
| Categorical | Mode imputation | Most common value |
| Boolean | Logical inference | Based on related fields |

### Outlier Treatment

| Field | Lower Bound | Upper Bound | Action |
|-------|-------------|-------------|--------|
| Age | 10 | 100 | Flag for review |
| Sessions | 0 | 1000 | Cap at 99th percentile |
| Time Spent | 0 | 100000 min | Flag > 10000 |
| Test Scores | 0 | 100 | Reject out of range |

---

## Example Data Structure

### Input CSV Format

```csv
Learner_ID,Age,Gender,Location,Socioeconomic_Status,Learning_Sessions_Completed,Total_Time_Spent_Minutes,Course_Completion_Percentage,Pre_Test_Score,Post_Test_Score,Dropout,Days_Since_Last_Login,Learning_Pace,Learning_Medium,Platform_Used,Content_Type_Preferred
L001,25,Male,Urban,Middle,45,2700.5,75.0,60,82,False,3,Moderate,Online,Desktop,Video
L002,30,Female,Rural,Low,80,4800.0,100.0,55,88,False,1,Fast,Hybrid,Both,Interactive
L003,22,Male,Urban,High,15,450.0,25.0,70,72,True,45,Slow,Online,Mobile,Text
```

### Output CSV Format (Tableau Export)

```csv
Learner_ID,Age,Gender,Cluster,Risk_Level,Knowledge_Gain,Engagement_Rate,...
L001,25,Male,0,Low,22,0.45,...
L002,30,Female,1,Low,33,0.80,...
L003,22,Male,2,High,2,0.15,...
```

---

## Field Dependencies

### Logical Relationships

1. **Completion and Dropout**:
   - If `Course_Completion_Percentage = 100`, then `Dropout = False`
   - If `Dropout = True`, then `Course_Completion_Percentage < 100`

2. **Time and Sessions**:
   - `Average_Session_Duration = Total_Time_Spent_Minutes / Learning_Sessions_Completed`
   - If `Learning_Sessions_Completed = 0`, then `Total_Time_Spent_Minutes = 0`

3. **Performance**:
   - `Knowledge_Gain = Post_Test_Score - Pre_Test_Score`
   - Typical range: -30 to +70 points

4. **Activity**:
   - If `Days_Since_Last_Login > 30` and `Course_Completion_Percentage < 100`, likely `Dropout = True`

---

## Data Privacy & Ethics

### Anonymization Requirements

- **Remove**: Names, email addresses, student IDs (unless anonymized)
- **Generalize**: Exact ages → age groups, specific locations → regions
- **Aggregate**: When reporting, use group statistics

### Compliance

- Ensure FERPA compliance (US)
- Follow GDPR guidelines (EU)
- Obtain proper consent for data usage
- Document data retention policies

---

## FAQ

**Q: What if my dataset doesn't have all fields?**
A: Minimum required fields are: Learner_ID, engagement metrics (sessions, time, completion), and performance scores (pre/post test). Other fields can be omitted or set to default values.

**Q: Can I add custom fields?**
A: Yes! Add them to the CSV. Update `src/data_preprocessing.py` to include them in the feature set.

**Q: How do I handle different test scoring systems?**
A: Normalize all scores to 0-100 scale before input.

**Q: What about learners with incomplete courses?**
A: They're included in the analysis. The `Dropout` field helps identify patterns in incomplete learners.

---

## Version History

- **v1.0** (2025-10-05): Initial data dictionary
- Future: Will add fields for temporal analysis, course-specific metrics

---

For questions about data formatting or field definitions, open an issue on GitHub or consult the [SETUP guide](../SETUP.md).
