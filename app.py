from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline


application = Flask(__name__)
app = application
import sys
# Route for home page
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    print(f"Request Method: {request.method}")  # Check the request method
    sys.stdout.flush()
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Create CustomData instance from form inputs
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            
            # Convert to DataFrame
            pred_df = data.get_data_as_data_frame()
            print("Input DataFrame:")
            print(pred_df)

            # Make predictions
            predict_pipeline = PredictPipeline()
            print("Starting Prediction...")
            results = predict_pipeline.predict(pred_df)
            print("Prediction Completed:", results)

            # Render results on home.html
            return render_template('home.html', results=results[0])

        except ValueError as ve:
            print(f"ValueError during prediction: {ve}")
            return render_template('home.html', results="Invalid data format. Please check your inputs.")

        except KeyError as ke:
            print(f"KeyError during prediction: {ke}")
            return render_template('home.html', results="Missing data. Please fill in all fields.")

        except TypeError as te:
            print(f"TypeError during prediction: {te}")
            return render_template('home.html', results="Data type mismatch. Please check your inputs.")

        
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug =True)
