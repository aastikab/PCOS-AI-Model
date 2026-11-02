
# PCOS-Driven Gut Microbiome AI Model for Prediabetes Prediction


**Aastika Banstola**  
Department of Computer and Mathematics, Fisk University  
Dr. Qi Li  


## Research Information
**Research Paper Title:** A Generative AI-Powered Approach to Personalized Gut Health  
**Research Mentor:** Dr. Karl Walker

## 1. Project Description
PCOS is a very common endocrine disorder affecting millions of women and often characterized by insulin resistance and prediabetes. Recently, evidence on the role of the gut microbiome has been emerging in both PCOS and metabolic health. However, no AI system links PCOS, gut microbiome composition, and prediabetes risk.

This project aims at the development of a Generative AI-enhanced prediction model, which will be able to:
- Predict the risk of prediabetes in PCOS patients using gut microbiome sequencing data
- Utilizes LLM and RAG in combining the newest research on microbiomes into one
- Generates personalized dietary and probiotic recommendations using AI

## 2. Project Goals
- Develop a machine learning model that predicts prediabetes risk based on gut microbiome data
- Integrate Generative AI for providing personalized diet and probiotic recommendations
- Implement an LLM-powered assistant that will explain AI insights in user-friendly terms
- Make sure the AI system auto-updates by pulling in new microbiome research via RAG

## 3. New Knowledge to be Obtained
- **Scientific Insights:** Identification of gut microbiome markers associated with insulin resistance in PCOS
- **AI Advancements:** Evaluation of the role of GenAI in Healthcare recommendation systems
- **Data Science Contributions:** Development of synthetic data augmentation techniques for microbiome data
- **Health Innovations:** Investigation of gut-based, non-invasive prediabetes prevention strategies

## 4. Objectives
1. Develop a machine learning model based on gut microbiome sequencing data for the prediction of prediabetes risk
2. Incorporate LLM + RAG to ensure AI recommendations are based on up-to-date research
3. Leverage Generative AI to suggest diet and probiotic recommendations as per the unique profiles of individuals
4. Deploy an AI-powered assistant to explain results in a user-friendly, interactive way
5. Determine model accuracy and effectiveness through on-the-ground implementation and feedback

## 5. Overview of Current Knowledge
- **PCOS and Gut Microbiome:** Evidence shows that quite often, women with PCOS have disturbed gut bacteria that add to insulin resistance
- **Prediabetes Risk Prediction:** AI has some usage in the prediction of prediabetes, but gut microbiome-based models remain under-explored
- **Generative AI in Healthcare:** While the applications of LLMs in medical chatbots are many, linking to gut microbiome research and providing recommendations in real time is relatively new
- **Gap in Research:** No AI system has ever connected PCOS, microbiome data, and prediabetes prediction with integrated Generative AI for recommendations

## 6. Impact
- **Healthcare Innovation:** Non-invasive AI-driven strategy for the prediction of prediabetes in PCOS patients
- **Personalized Treatment:** AI-driven probiotics and dietary guidance according to one's gut microbiome profile
- **Bridging AI & Medicine:** Integrating LLMs, RAG, and ML models for self-updating, AI-powered healthcare solutions
- **Women's Health Advocacy:** Using AI Research in Approach to Metabolic Disorders resulting from PCOS

## 7. Research Plan
### Phase 1: Data Collection & Literature Review (Weeks 1-3)
- Gather the datasets of gut microbiome sequencing for PCOS and non-PCOS patients
- Identify clinical data on insulin resistance, glucose levels, dietary habits
- Extract recent microbiome studies using RAG-based AI

### Phase 2: AI Model Development (Weeks 4-7)
- Feature Engineering: Identification of microbiome patterns associated with the risk of prediabetes
- Train ML models to predict prediabetes risk using Random Forest, XGBoost, and DNNs
- Assess model accuracy against clinical datasets of real-world encounters

### Phase 3: Generative AI Integration (Weeks 8-9)
- Develop an LLM-powered chatbot to explain AI insights in user-friendly language
- Add here GenAI functionality to provide personalized dietary and probiotic plans
- Deploy self-learning AI that updates its recommendations automatically as new microbiome research comes along

### Phase 4: Web App Development & Testing (Weeks 10-11)
- Deploy AI to a web assistant with Flask and React
- Usability testing, refinement of AI responses by including user feedback

### Phase 5: Deployment & Evaluation (Week 12)
- Validate the AI model's performance on real microbiome data
- Assess user satisfaction and feedback about medical professionals
- Publish results and discuss potential clinical use

## 8. Project Timeline (12 Weeks)

| Week | Phase | Key Tasks |
|------|-------|-----------|
| 1-3 | Data Collection & Research | Collect microbiome datasets, clinical data, and the latest research papers |
| 4-7 | AI Model Training | Develop ML models, train them with microbiome data, and predict |
| 8-9 | Generative AI Features | Implement AI chatbot and GenAI-powered recommendations |
| 10-11 | Web App Development | Deploy the AI assistant as an easy-to-use platform |
| 12 | Final Testing & Evaluation | Test performance and provide feedback toward improvement |

## 9. Conclusion
The AI model will, for the first time, connect the dots between PCOS, gut microbiome, and prediabetes risk prediction. The integration of LLMs, RAG, and Generative AI makes this a game-changing project in personalized, gut-based interventions for patients with PCOS. The outcome will be a self-learning AI assistant to help individuals make informed health decisions based on their unique microbiome profile.

## 10. References
1. Zhao, X., et al. (2022). Gut microbiota and insulin resistance in PCOS: A review. Journal of Endocrinology.
2. Kashyap, P. et al. (2023). AI-driven prediction models for metabolic disorders. Nature Machine Intelligence.
3. Brown, C. et al. (2024). Role of RAG-based AI in medical research. Journal of Artificial Intelligence in Healthcare.
4. Lee, S. et al. (2021). Probiotics as a treatment for insulin resistance in PCOS patients. Frontiers in Microbiology.

## Project Structure

\`\`\`
src/
├── charts/
│   ├── timeline.py          # Project timeline visualization
│   ├── dataset_viz.py       # Dataset analysis visualizations
│   └── model_performance.py # Model performance charts
├── utils/                   # Utility functions
└── generate_images.py       # Main script to generate all visualizations
\`\`\`

## Setup and Usage

1. Install dependencies:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

2. Generate visualizations:
\`\`\`bash
python src/generate_images.py
\`\`\`
EOL
