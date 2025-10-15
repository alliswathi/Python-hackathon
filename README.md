# Team2_NumPioneers_PythonHackathon_August25
<h2>Project Title: 
  Data-Driven Insights: Sleep, CGM, and Glycemic Event Prediction in T1DM</h2>
<h2>Project Description</h2>  
  <p>This project focuses on analyzing a unique dataset that integrates Continuous Glucose Monitoring (CGM) data, insulin administration, carb intake, physical              activity, heart rate, and sleep quality/quantity from 25 individuals with Type 1 Diabetes Mellitus (T1DM).</p>           
        <p>The data was collected using:</p>         
               <p><ul>FreeStyle Libre 2 CGMs for glucose monitoring.</p></ul>  
              <p><ul>Fitbit Ionic smartwatches for steps, calories burned, heart rate, and sleep tracking.</p>            
              <p>Each participant was monitored for a minimum of 14 consecutive days.</p> </ul>        
        <p>This rich, multi-dimensional dataset allows researchers and developers to:</p>            
            <p><ul>Build glucose prediction models.</p>          
           <p>Develop hypoglycemia and hyperglycemia detection algorithms.</p>         
            <p>Explore the impact of sleep, activity, and lifestyle factors on glucose variability.</p>          
            <p>Use either the raw data for customized pipelines or the preprocessed version for immediate model development.</p>         
            <p>By combining physiological, behavioral, and clinical variables, this project provides a foundation for advancing data-driven diabetes management,     personalized healthcare solutions, and predictive modeling in T1DM research.</p></ul>
  <h2> Dataset</h2>
  <h3>Dataset name: HUPA-UCM Diabetes Dataset</h3>
  <p><b>Source:</b> https://data.mendeley.com/datasets/3hbcscwz44/1</P>
  <h3>Data files:</h3>
      <ul>Preprocessed/ and raw data/ containing demographics and 25 patients file in csv format.</ul>
      <ul>Each file contains Continuous Glucose Monitoring (CGM) data,steps, calories burned, heart rate, and sleep tracking of each patients.</ul>
  <h3>File description:</h3>
      <p>The csv file contains entries for :</p>
           <ul><b>Continuous Glucose Monitoring (CGM):</b> Blood glucose level measurements every five minutes</ul>
          <ul><b>Insulin: </b>Bolus and basal insulin doses, with details on the type and amount administered</ul>
          <ul><b>Carb intake:</b> Recorded carbohydrate intake</ul>
          <ul><b>Steps :</b> Steps count taken by Fitbit Ionic smartwatches</ul>
          <ul><b>Heart Rate :</b> Heart rate taken by Fitbit Ionic smartwatches for evey 5 mins</ul>
  <h3> Code structure</h3>
      <p>The project's code is organized into the following directories and files:
        <p><ul><b>Diabetes_dataset:</b> Contains HUPA-UCM Diabetes Dataset</ul>
        <ul><p><b>Notebooks:</b> Jupyter notebooks used for data exploration and model development
          <ul><p>Team2_NumPioneers_Data Cleaning.ipynb: Notebook for data cleaning and</p> </ul>
          <ul><p>Team2_NumPioneers_Descriptive_Analysis II.ipynb: Notebook for  Visualizations and summary statistics.</ul>
          <ul><p>Team2_NumPioneers_Prescriptive_Analysis III.ipynb: Notebook for Implementation of recommendations and optimization.</ul>
          <ul><p>Team2_NumPioneers_Predective_Analysis IV.ipynb: Notebook for Model training, validation, and evaluation.</ul></ul>
         <ul> <b>requirements.txt:</b> Lists all Python dependencies required to run the project. </ul>
<h2> Methodology:</h2>
<h3> Data cleaning and preparation:</h3>
        <ul><p>Setting Clinical Ranges & Checking Outliers.</p>
         <p>Patient information (names, emails) was removed and replaced with unique identifiers.</p>
        <p>Identify rows in the dataset where values fall outside the defined acceptable ranges.</p>
        <p>Capping Outliers with Defined Clinical Ranges</p>
        <p>Convert time to proper datetime format</P></ul>
<h3> Descriptive Analysis:</h3>
        <ul><b>Objective:</b> To understand the basic characteristics of the T1D patient population and the dynamics of their disease over time.</ul>
         <ul><b>Key Activities:</b>
        <ul><b>Exploratory Data Analysis (EDA):</b> Visualizations and statistical summaries of patient data.</ul>
        <ul><b>Trend Analysis:</b> Identifying patterns in glucose levels, insulin usage, and activity levels over time.</ul>
        <ul><b>Patient Segmentation:</b> Grouping patients based on their demographic information, health metrics, or lifestyle factors.</ul></ul>
   <ul><b>Outputs:</b>
        <ul>Notebooks detailing the data exploration.</ul>
        <ul>Visualizations (charts, graphs) showing trends and distributions.</ul>
       <ul> Summary statistics of key health indicators.</ul></ul>
<h3> Prescriptive Analysis</h3>
      <ul><b>Objective:</b> To provide actionable, data-driven recommendations for T1D management.</ul>
      <ul><b>Key Activities:</b>
      <ul><b>Rule-Based Systems:</b> Creating clear, interpretable rules based on predictive insights (e.g., "If glucose is predicted to drop below X, and the patient has     been active, reduce insulin dose by Y units").</ul>
      <ul><b>Optimization Algorithms:</b> Developing algorithms to suggest optimal treatment plans, such as adjusting insulin dosage based on predicted glucose response.</ul>
      <ul><b>Treatment Pathway Simulation:</b> Using a combination of descriptive and predictive sources to simulate different treatment scenarios and recommend the best course of action.</ul></ul>
       <ul><b>Outputs:</b>
      <Implementation of a prototype Clinical Decision Support System (CDSS).</ul>
      <ul>Documentation of the rules and logic for actionable insights.</ul>
      <ul>A report detailing the effectiveness of recommended strategies against actual outcomes.</ul></ul>
<h3> Predictive Analysis</h3>
      <ul><b>Objective:</b> To build models that can forecast future events and patient outcomes.</ul>
     <ul> <b>Key Activities:</b>
      <ul><b>Feature Engineering:</b> Creating new variables from the raw data to improve model performance.</ul>
      <ul><b>Model Training:</b> Developing and training machine learning models such as:</ul>
      <ul><b>Time-Series Models:</b> To predict future blood glucose levels based on historical CGM data.</ul>
      <ul><b>Classification Models:</b> To forecast the risk of complications (e.g., hypoglycemia, diabetic ketoacidosis).</ul>
     <ul> <b>Model Evaluation:</b> Assessing model accuracy using appropriate metrics like F1-score or RMSE.</ul></ul>
       <ul><b>Outputs:</b>
      <ul>Jupyter notebooks with the predictive modeling workflow.</ul>
      <ul>Pickled model files for future use.</ul>
      <ul>Performance metrics and validation results.</ul></ul>
<h3> How to Run the Project</h3>
      <ul><b>Clone the repository:</b>
        <ul>https://github.com/sdeshp34/Team2_NumPioneers_PythonHackathon_August25</ul></ul>
      <ul><b>Navigate to the project directory:</b>
        <ul>cd Team2_NumPioneers_PythonHackathon_August25 </ul></ul>
      <ul><b>Install the required dependencies:</b>
        <ul>pip install -r requirements.txt </ul></ul>
      <ul><b>Explore the Jupyter notebooks:</b>
        <ul>jupyter notebook </ul>
       <ul>Follow the notebooks in numerical order to walk through the complete analytical process. </ul></ul>     



        
