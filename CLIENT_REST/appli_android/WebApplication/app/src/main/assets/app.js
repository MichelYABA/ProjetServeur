function SendFile() {
  var InputCSV = $("#InputCSV")[0].files[0]; //this is the input where I can choose the file
  var formData = new FormData();
  formData.append("InputCSV", InputCSV);

  var xhr = new XMLHttpRequest();
 xhr.open("POST", "http://0.0.0.0:5000/inputcsv");

  xhr.send(formData);
}