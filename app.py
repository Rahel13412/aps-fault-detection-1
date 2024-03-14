# from sensor.pipeline.training_pipeline import start_training_pipeline
# from sensor.pipeline.batch_prediction import start_batch_prediction

# file_path="aps_dataset.csv"

# print(__name__)
# if __name__=="__main__":
#      try:
#           #start_training_pipeline()
#           output_file = start_batch_prediction(input_file_path=file_path)
#           print(output_file)


#      except Exception as e:
#           print(e)

from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
from sensor.pipeline.batch_prediction import start_batch_prediction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            return "No file part"
        
        file = request.files['file']
        
        # Check if the file is empty
        if file.filename == '':
            return "No selected file"
        
        # Check if the file is a CSV
        if file and file.filename.endswith('.csv'):
            file_path = secure_filename(file.filename)
            file.save(file_path)
            
            # Start batch prediction
            try:
                output_file = start_batch_prediction(input_file_path=file_path)
                return send_file(output_file, as_attachment=True)
            except Exception as e:
                return str(e)
        
        return "Invalid file format. Please upload a CSV file."
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
