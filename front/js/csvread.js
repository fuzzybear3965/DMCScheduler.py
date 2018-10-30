// The following taken from https://www.html5rocks.com/en/tutorials/file/dndfiles/
// Check for the various File API support.
if (window.File && window.FileReader && window.FileList && window.Blob) {
    // Great success! All the File APIs are supported.
    function handleFileSelect(evt) {
        var file = evt.target.files[0]; // FileList object

        // files is a FileList of File objects. List some properties.
        var reader = new FileReader();
        reader.onload = (function(f) {
            return function(e) {
                Papa.parse(f, {
                    delimiter: "|",
                    header: true,
                    complete: insertTable,
                    skipEmptyLines: true,
                })
            }
        })(file)

        reader.readAsText(file);

        var output = (
            'Template uploaded: ' + file.name
        );

        document.getElementById('filename').innerHTML = '<strong>' + output + '</strong>';
    }

    document.getElementById('file-upload').addEventListener('change', handleFileSelect, false);
} else {
    alert('The File APIs are not fully supported in this browser.');
}
// from https://gist.github.com/hurjas/2660489
function timeStamp() {
// Create a date object with the current time
  var now = new Date();

// Create an array with the current month, day and time
  var date = [ now.getMonth() + 1, now.getDate(), now.getFullYear() ];

// Create an array with the current hour, minute and second
  var time = [ now.getHours(), now.getMinutes(), now.getSeconds() ];

// Determine AM or PM suffix based on the hour
  var suffix = ( time[0] < 12 ) ? "AM" : "PM";

// Convert hour from military time
  time[0] = ( time[0] < 12 ) ? time[0] : time[0] - 12;

// If hour is 0, set it to 12
  time[0] = time[0] || 12;

// If seconds and minutes are less than 10, add a zero
  for ( var i = 1; i < 3; i++ ) {
    if ( time[i] < 10 ) {
      time[i] = "0" + time[i];
    }
  }

// Return the formatted string
  return date.join("-") + " " + time.join("_") + " " + suffix;
}

var cb = function() {
    console.log("hey");
}

function downloadTemplate(e) {
    table.download('csv', 'schedule-template-' + timeStamp() + '.csv', {'delimiter':'|'})
}

dlEl = document.getElementById('download')
dlEl.addEventListener('click', downloadTemplate)
