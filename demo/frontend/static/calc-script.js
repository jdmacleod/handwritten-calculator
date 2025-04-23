const predictButton = document.getElementById("predictButton");
const clearButton1 = document.getElementById("clearButton1");
const clearButton2 = document.getElementById("clearButton2");
const clearButton3 = document.getElementById("clearButton3");
const clearAllButton = document.getElementById("clearAllButton");
const predictionAllEl = document.getElementById("predictionAll");
const confidenceAllEl = document.getElementById("confidenceAll");
const prediction1El = document.getElementById("prediction1");
const confidence1El = document.getElementById("confidence1");
const prediction2El = document.getElementById("prediction2");
const confidence2El = document.getElementById("confidence2");
const prediction3El = document.getElementById("prediction3");
const confidence3El = document.getElementById("confidence3");
const messageEl = document.getElementById("message");

let context1, canvas1, context2, canvas2, context3, canvas3;

$(document).ready(function () {
  initialize_canvas1();
  initialize_canvas2();
  initialize_canvas3();
});

// works out the X, Y position of the click inside the canvas from the X, Y position on the page

function getPosition(mouseEvent, sigCanvas) {
  var rect = sigCanvas.getBoundingClientRect();
  return {
    X: mouseEvent.clientX - rect.left,
    Y: mouseEvent.clientY - rect.top,
  };
}

function initialize_canvas1() {
  // get references to the canvas element as well as the 2D drawing context
  var sigCanvas1 = document.getElementById("canvas1");
  canvas1 = sigCanvas1;
  context1 = sigCanvas1.getContext("2d");
  context1.fillStyle = "#fff";
  context1.strokeStyle = "#000";
  context1.lineJoin = "round";
  context1.lineWidth = 7;

  context1.fillRect(0, 0, sigCanvas1.width, sigCanvas1.height);

  var is_touch_device = "ontouchstart" in document.documentElement;

  if (is_touch_device) {
    // create a drawer which tracks touch movements
    var drawer = {
      isDrawing: false,
      touchstart: function (coors) {
        context1.beginPath();
        context1.moveTo(coors.x, coors.y);
        this.isDrawing = true;
      },
      touchmove: function (coors) {
        if (this.isDrawing) {
          context1.lineTo(coors.x, coors.y);
          context1.stroke();
        }
      },
      touchend: function (coors) {
        if (this.isDrawing) {
          this.touchmove(coors);
          this.isDrawing = false;
        }
      },
    };

    // create a function to pass touch events and coordinates to drawer
    function draw(event) {
      // get the touch coordinates.  Using the first touch in case of multi-touch
      var coors = {
        x: event.targetTouches[0].pageX,
        y: event.targetTouches[0].pageY,
      };

      // Now we need to get the offset of the canvas location
      var obj = sigCanvas1;

      if (obj.offsetParent) {
        // Every time we find a new object, we add its offsetLeft and offsetTop to curleft and curtop.
        do {
          coors.x -= obj.offsetLeft;
          coors.y -= obj.offsetTop;
        } while (
          // The while loop can be "while (obj = obj.offsetParent)" only, which does return null
          // when null is passed back, but that creates a warning in some editors (i.e. VS2010).
          (obj = obj.offsetParent) != null
        );
      }

      // pass the coordinates to the appropriate handler
      drawer[event.type](coors);
    }

    // attach the touchstart, touchmove, touchend event listeners.
    sigCanvas1.addEventListener("touchstart", draw, false);
    sigCanvas1.addEventListener("touchmove", draw, false);
    sigCanvas1.addEventListener("touchend", draw, false);

    // prevent elastic scrolling
    sigCanvas1.addEventListener(
      "touchmove",
      function (event) {
        event.preventDefault();
      },
      false
    );
  } else {
    // start drawing when the mousedown event fires, and attach handlers to
    // draw a line to wherever the mouse moves to
    $("#canvas1").mousedown(function (mouseEvent) {
      var position = getPosition(mouseEvent, sigCanvas1);
      context1.moveTo(position.X, position.Y);
      context1.beginPath();

      // attach event handlers
      $(this)
        .mousemove(function (mouseEvent) {
          drawLine(mouseEvent, sigCanvas1, context1);
        })
        .mouseup(function (mouseEvent) {
          finishDrawing(mouseEvent, sigCanvas1, context1);
        })
        .mouseout(function (mouseEvent) {
          finishDrawing(mouseEvent, sigCanvas1, context1);
        });
    });
  }
}

function initialize_canvas2() {
  // get references to the canvas element as well as the 2D drawing context
  var sigCanvas2 = document.getElementById("canvas2");
  canvas2 = sigCanvas2;
  context2 = sigCanvas2.getContext("2d");
  context2.fillStyle = "#fff";
  context2.strokeStyle = "#000";
  context2.lineJoin = "round";
  context2.lineWidth = 7;

  context2.fillRect(0, 0, sigCanvas2.width, sigCanvas2.height);

  var is_touch_device = "ontouchstart" in document.documentElement;

  if (is_touch_device) {
    // create a drawer which tracks touch movements
    var drawer = {
      isDrawing: false,
      touchstart: function (coors) {
        context2.beginPath();
        context2.moveTo(coors.x, coors.y);
        this.isDrawing = true;
      },
      touchmove: function (coors) {
        if (this.isDrawing) {
          context2.lineTo(coors.x, coors.y);
          context2.stroke();
        }
      },
      touchend: function (coors) {
        if (this.isDrawing) {
          this.touchmove(coors);
          this.isDrawing = false;
        }
      },
    };

    // create a function to pass touch events and coordinates to drawer
    function draw(event) {
      // get the touch coordinates.  Using the first touch in case of multi-touch
      var coors = {
        x: event.targetTouches[0].pageX,
        y: event.targetTouches[0].pageY,
      };

      // Now we need to get the offset of the canvas location
      var obj = sigCanvas2;

      if (obj.offsetParent) {
        // Every time we find a new object, we add its offsetLeft and offsetTop to curleft and curtop.
        do {
          coors.x -= obj.offsetLeft;
          coors.y -= obj.offsetTop;
        } while (
          // The while loop can be "while (obj = obj.offsetParent)" only, which does return null
          // when null is passed back, but that creates a warning in some editors (i.e. VS2010).
          (obj = obj.offsetParent) != null
        );
      }

      // pass the coordinates to the appropriate handler
      drawer[event.type](coors);
    }

    // attach the touchstart, touchmove, touchend event listeners.
    sigCanvas2.addEventListener("touchstart", draw, false);
    sigCanvas2.addEventListener("touchmove", draw, false);
    sigCanvas2.addEventListener("touchend", draw, false);

    // prevent elastic scrolling
    sigCanvas2.addEventListener(
      "touchmove",
      function (event) {
        event.preventDefault();
      },
      false
    );
  } else {
    // start drawing when the mousedown event fires, and attach handlers to
    // draw a line to wherever the mouse moves to
    $("#canvas2").mousedown(function (mouseEvent) {
      var position = getPosition(mouseEvent, sigCanvas2);
      context2.moveTo(position.X, position.Y);
      context2.beginPath();

      // attach event handlers
      $(this)
        .mousemove(function (mouseEvent) {
          drawLine(mouseEvent, sigCanvas2, context2);
        })
        .mouseup(function (mouseEvent) {
          finishDrawing(mouseEvent, sigCanvas2, context2);
        })
        .mouseout(function (mouseEvent) {
          finishDrawing(mouseEvent, sigCanvas2, context2);
        });
    });
  }
}

function initialize_canvas3() {
  // get references to the canvas element as well as the 2D drawing context
  var sigCanvas3 = document.getElementById("canvas3");
  canvas3 = sigCanvas3;
  context3 = sigCanvas3.getContext("2d");
  context3.fillStyle = "#fff";
  context3.strokeStyle = "#000";
  context3.lineJoin = "round";
  context3.lineWidth = 7;

  context3.fillRect(0, 0, sigCanvas3.width, sigCanvas3.height);

  var is_touch_device = "ontouchstart" in document.documentElement;

  if (is_touch_device) {
    // create a drawer which tracks touch movements
    var drawer = {
      isDrawing: false,
      touchstart: function (coors) {
        context3.beginPath();
        context3.moveTo(coors.x, coors.y);
        this.isDrawing = true;
      },
      touchmove: function (coors) {
        if (this.isDrawing) {
          context3.lineTo(coors.x, coors.y);
          context3.stroke();
        }
      },
      touchend: function (coors) {
        if (this.isDrawing) {
          this.touchmove(coors);
          this.isDrawing = false;
        }
      },
    };

    // create a function to pass touch events and coordinates to drawer
    function draw(event) {
      // get the touch coordinates.  Using the first touch in case of multi-touch
      var coors = {
        x: event.targetTouches[0].pageX,
        y: event.targetTouches[0].pageY,
      };

      // Now we need to get the offset of the canvas location
      var obj = sigCanvas3;

      if (obj.offsetParent) {
        // Every time we find a new object, we add its offsetLeft and offsetTop to curleft and curtop.
        do {
          coors.x -= obj.offsetLeft;
          coors.y -= obj.offsetTop;
        } while (
          // The while loop can be "while (obj = obj.offsetParent)" only, which does return null
          // when null is passed back, but that creates a warning in some editors (i.e. VS2010).
          (obj = obj.offsetParent) != null
        );
      }

      // pass the coordinates to the appropriate handler
      drawer[event.type](coors);
    }

    // attach the touchstart, touchmove, touchend event listeners.
    sigCanvas3.addEventListener("touchstart", draw, false);
    sigCanvas3.addEventListener("touchmove", draw, false);
    sigCanvas3.addEventListener("touchend", draw, false);

    // prevent elastic scrolling
    sigCanvas3.addEventListener(
      "touchmove",
      function (event) {
        event.preventDefault();
      },
      false
    );
  } else {
    // start drawing when the mousedown event fires, and attach handlers to
    // draw a line to wherever the mouse moves to
    $("#canvas3").mousedown(function (mouseEvent) {
      var position = getPosition(mouseEvent, sigCanvas3);
      context3.moveTo(position.X, position.Y);
      context3.beginPath();

      // attach event handlers
      $(this)
        .mousemove(function (mouseEvent) {
          drawLine(mouseEvent, sigCanvas3, context3);
        })
        .mouseup(function (mouseEvent) {
          finishDrawing(mouseEvent, sigCanvas3, context3);
        })
        .mouseout(function (mouseEvent) {
          finishDrawing(mouseEvent, sigCanvas3, context3);
        });
    });
  }
}

// draws a line to the x and y coordinates of the mouse event inside
// the specified element using the specified context
function drawLine(mouseEvent, sigCanvas, context) {
  var position = getPosition(mouseEvent, sigCanvas);
  context.lineTo(position.X, position.Y);
  context.stroke();
}

// draws a line from the last coordinates in the path to the finishing
// coordinates and unbind any event handlers which need to be preceded
// by the mouse down event
function finishDrawing(mouseEvent, sigCanvas, context) {
  // draw the line to the finishing coordinates
  drawLine(mouseEvent, sigCanvas, context);
  context.closePath();
  // unbind any events which could draw
  $(sigCanvas).unbind("mousemove").unbind("mouseup").unbind("mouseout");
}

// Clear the canvas context using the canvas width and height
function clearCanvas1() {
  context1.clearRect(0, 0, canvas1.width, canvas1.height);
  context1.fillRect(0, 0, canvas1.width, canvas1.height);
}
function clearCanvas2() {
  context2.clearRect(0, 0, canvas2.width, canvas2.height);
  context2.fillRect(0, 0, canvas2.width, canvas2.height);
}
function clearCanvas3() {
  context3.clearRect(0, 0, canvas3.width, canvas3.height);
  context3.fillRect(0, 0, canvas3.width, canvas3.height);
}

// Clear the individual predictions
function clearPrediction1() {
  clearCanvas1();
  prediction1El.textContent = "?";
  confidence1El.textContent = "";
  messageEl.textContent = "";
  messageEl.style.display = "none";
}

function clearPrediction2() {
  clearCanvas2();
  prediction2El.textContent = "?";
  confidence2El.textContent = "";
  messageEl.textContent = "";
  messageEl.style.display = "none";
}

function clearPrediction3() {
  clearCanvas3();
  prediction3El.textContent = "?";
  confidence3El.textContent = "";
  messageEl.textContent = "";
  messageEl.style.display = "none";
}

// Clear all input and prediction results
function clearAll() {
  clearCanvas1();
  clearCanvas2();
  clearCanvas3();

  prediction1El.textContent = "?";
  confidence1El.textContent = "";
  prediction2El.textContent = "?";
  confidence2El.textContent = "";
  prediction3El.textContent = "?";
  confidence3El.textContent = "";

  predictionAllEl.textContent = "?";
  confidenceAllEl.textContent = "";
  messageEl.textContent = "";
  messageEl.style.display = "none";
}

function predictDigit1() {
  var image = canvas1.toDataURL("image/png");
  return axios.post("/predict-digit", {
    image,
  });
}

function predictSymbol() {
  var image = canvas2.toDataURL("image/png");
  return axios.post("/predict-symbol", {
    image,
  });
}

function predictDigit3() {
  var image = canvas3.toDataURL("image/png");
  return axios.post("/predict-digit", {
    image,
  });
}

function predictAll() {
  Promise.all([predictDigit1(), predictSymbol(), predictDigit3()]).then(
    function (results) {
      const response1 = results[0];
      const response2 = results[1];
      const response3 = results[2];
      var prediction1 = response1.data.prediction;
      var confidence1 = response1.data.confidence;
      var message1 = response1.data.message;

      prediction1El.textContent = prediction1;
      confidence1El.textContent = `${parseInt(parseFloat(confidence1) * 100)}%`;

      var prediction3 = response3.data.prediction;
      var confidence3 = response3.data.confidence;
      var message3 = response1.data.message;

      prediction3El.textContent = prediction3;
      confidence3El.textContent = `${parseInt(parseFloat(confidence3) * 100)}%`;

      var prediction2 = response2.data.prediction;
      var confidence2 = response2.data.confidence;
      var message2 = response2.data.message;

      // display message only when there is a message
      // display the first message that is not empty
      if (message1 || message2 || message3) {
        messageEl.textContent = message1 || message2 || message3;
        messageEl.style.display = "block";
      } else {
        messageEl.style.display = "none";
      }

      // map prediction index to arithmetic symbols
      var prediction2Int = parseInt(prediction2);
      var symbolHTML = "";
      switch (prediction2Int) {
        case 0: // addition_plus
          symbolHTML = "&plus;";
          break;
        case 1: // division_obelus
          symbolHTML = "&divide;";
          break;
        case 2: // division_slash
          symbolHTML = "&#8725;";
          break;
        case 3: // multiplication_cross
          symbolHTML = "&times;";
          break;
        case 4: // multiplication_dot
          symbolHTML = "&sdot;";
          break;
        case 5: // subtraction_minus
          symbolHTML = "&minus;";
          break;
        default:
          symbolHTML = "?";
      }
      prediction2El.innerHTML = symbolHTML;
      confidence2El.textContent = `${parseInt(parseFloat(confidence2) * 100)}%`;

      // compute the expression
      var prediction1Int = parseInt(prediction1);
      var prediction3Int = parseInt(prediction3);

      switch (prediction2Int) {
        case 0: // addition_plus
          prediction = prediction1Int + prediction3Int;
          break;
        case 1: // division_obelus
        case 2: // division_slash
          var quotient = Math.floor(prediction1Int / prediction3Int);
          var remainder = prediction1Int % prediction3Int;
          prediction = quotient;
          if (remainder > 0) {
            prediction += "r" + remainder.toString();
          }
          break;
        case 3: // multiplication_cross
        case 4: // multiplication_dot
          prediction = prediction1Int * prediction3Int;
          break;
        case 5: // subtraction_minus
          prediction = prediction1Int - prediction3Int;
          break;
        default:
          prediction = "?";
      }
      predictionAllEl.textContent = prediction;
      confidenceAllEl.textContent = `${parseInt(
        parseFloat(confidence1) *
          parseFloat(confidence2) *
          parseFloat(confidence3) *
          100
      )}%`;
    }
  );
}

clearButton1.addEventListener("click", clearPrediction1);
clearButton2.addEventListener("click", clearPrediction2);
clearButton3.addEventListener("click", clearPrediction3);

clearAllButton.addEventListener("click", clearAll);
predictButton.addEventListener("click", predictAll);
