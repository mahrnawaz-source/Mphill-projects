# Multi-Omics Integration and Biomarker Discovery using DIABLO

## Project Overview
This project was completed as part of my MS/MPhil Bioinformatics coursework. The project focused on integrating multi-omics datasets from breast cancer patients using the DIABLO framework from the mixOmics R package.

## Dataset
- TCGA-BRCA breast cancer cohort
- Data source: LinkedOmics
- Omics layers used:
  - mRNA expression
  - miRNA expression
  - RPPA protein abundance
  - Clinical metadata

## Objectives
- To retrieve and preprocess multi-omics breast cancer datasets.
- To match common samples across mRNA, miRNA, protein, and clinical data.
- To integrate multi-omics datasets using DIABLO.
- To identify correlated molecular features across omics layers.
- To explore biomarker discovery and breast cancer subtype classification.

## Methods
- Data loading in R
- Sample ID matching
- Dataset transposition
- Common sample extraction
- Log2 transformation
- Low-variance feature filtering
- Scaling and centering
- DIABLO analysis using mixOmics
- Latent component correlation analysis
- Multi-omics visualization

## Tools Used
- R
- RStudio
- mixOmics
- DIABLO
- LinkedOmics
- TCGA-BRCA dataset

## Key Findings
- Common samples were retained across mRNA, miRNA, RPPA, and clinical datasets.
- DIABLO identified strong correlation between omics layers.
- mRNA–miRNA correlation: 0.85
- mRNA–protein correlation: 0.89
- miRNA–protein correlation: 0.79
- The results showed coordinated regulation across transcriptomic, miRNA, and protein-level data.

## Skills Demonstrated
- Multi-omics data integration
- Biomarker discovery workflow
- R-based bioinformatics analysis
- Cancer subtype analysis
- Data preprocessing
- Feature filtering and normalization
- Scientific report writing
