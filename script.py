
  def categorise_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    gender = self.gender_textbox.text
    age = self.age.text
    hypertension = self.hypertension_textbox.text
    disease = self.disease_textbox.text
    married = self.married_textbox.text
    work = self.work_textbox.text
    residence = self.residence_textbox.text
    glucose = self.glucose_textbox.text
    bmi = self.bmi_textbox.text
    smoking = self.smoking_textbox.text

    stroke = anvil.server.call('predict_stroke', 
                               gender,
                               age, 
                               hypertension, 
                               disease, 
                               married, 
                               work, 
                               residence, 
                               glucose, 
                               bmi, 
                               smoking)
    if stroke==1:
      self.stroke_label.visible = True
      self.stroke_label.text = 'High chances of a stroke'
      self.low_image.visible = True
      self.low_image.source = 'https://www.seekpng.com/png/detail/123-1237134_sad-man-png-jpg-free-download-sad-man.png'
    else:
      self.stroke_label.visible = True
      self.low_image.visible = True
      self.stroke_label.text = 'Low chances of a stroke'
      self.low_image.source = 'https://media.istockphoto.com/photos/happy-man-showing-thumb-up-picture-id611778400?k=20&m=611778400&s=170667a&w=0&h=a7474VZ08UvIb1jtyNAeNFRvfGvudJ2N1OZt-lbniLc='
    
      

