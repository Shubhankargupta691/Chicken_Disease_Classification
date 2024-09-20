	function sendRequest(base64Data) {
      var url = $("#url").val();
      $("#loading").show();
      $.ajax({
        url: url,
        type: "post",
        cache: false,
        async: true,
        crossDomain: true,
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*",
        },
        data: JSON.stringify({ image: base64Data }),
        success: function (res) {
          $("#json-output").hide(); // Hide the output box initially
          $("#json-output").html(""); // Clear previous output
  
          var textOutput = '';
  
          try {
            if (Array.isArray(res)) {
              // Handle array response
              res.forEach(function(item) {
                if (typeof item === 'object') {
                  for (var key in item) {
                    if (item.hasOwnProperty(key)) {
                      textOutput += "<strong>Chicken has a disease called:</strong> " + item[key] + '<br>';
                    }
                  }
                } else {
                  textOutput += item + '<br>';
                }
              });
            } else if (typeof res === 'object') {
              // Handle object response
              for (var key in res) {
                if (res.hasOwnProperty(key)) {
                  textOutput += "<strong>Chicken has a disease called:</strong> " + res[key] + '<br>';
                }
              }
            } else {
              textOutput = 'Unexpected response format';
            }
          } catch (e) {
            console.error('Error processing result', e);
            textOutput = 'Error processing result';
          }
  
          // Add formatted text to the output box
          $("#json-output").append("<div>" + textOutput.trim() + "</div>");
          $("#json-output").show(); // Show the output box
          $("#loading").hide();
        },
        error: function (xhr, status, error) {
          $("#json-output").html("<p>Error: " + error + "</p>");
          $("#json-output").show(); // Show the output box on error
          $("#loading").hide();
        }
      });
    }
  
    $(document).ready(function () {
      $("#loading").hide();
  
      $("#send").click(function (evt) {
        sendRequest(base_data);
      });
  
      $("#uload").click(function (evt) {
        $("#fileinput").focus().trigger("click");
      });
  
      $("#fileinput").change(function () {
        if (this.files && this.files[0]) {
          var reader = new FileReader();
          reader.onload = function (e) {
            var url = e.target.result;
            var img = new Image();
            img.crossOrigin = "Anonymous";
            img.onload = function () {
              var canvas = document.createElement("CANVAS");
              var ctx = canvas.getContext("2d");
              canvas.height = this.height;
              canvas.width = this.width;
              ctx.drawImage(this, 0, 0);
              base_data = canvas
                .toDataURL("image/jpeg", 1.0)
                .replace(/^data:image.+;base64,/, "");
              canvas = null;
            };
            img.src = url;
            $("#photo").attr("src", url);
            $("#photo").show();
          };
          reader.readAsDataURL(this.files[0]);
        }
      });
    });

  
  