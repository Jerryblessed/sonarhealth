---

## To Train Your Own Model from Scratch

To train your own model on Google Colab:

1. **Copy each file to Colab** (e.g., `ct_train.py` or `histo_train.py`)

   * Run the files individually. Each script will automatically download the dataset from Kaggle and train a model, saving the output in `.keras` format.
   * Example:

     ```bash
     !python ct_train.py  
     !python histo_train.py
     ```

2. **Get the trained models**

   * Running `ct_train.py` will produce `densenet121.keras`.
   * Running `histo_train.py` will generate three models: `densenet121.keras`, `mobilenetv2.keras`, and `inceptionv3.keras`.
   * You may choose any of these, but for this project, **Densenet121** was used. Rename the chosen histopathology model to `histo_densenet121_model.keras`.
   * Final expected filenames:

     * `ctscan_densenet121.keras`
     * `histo_densenet121_model.keras`

You can also train on your own computer:

* **Log in** securely via a role-based viewer list.
* **Upload** CT or histopathology images (Benign, Adenocarcinoma, Squamous Cell Carcinoma).
* **Receive** instant AI predictions and confidence scores.
* **Interact** with an embedded chatbot for explanations and guidance.

All model building, tagging, and evaluation are handled through Azure's portal—clinicians need zero programming skills.

---

